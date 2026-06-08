"""Scrape webpage sources listed in planning.md and save raw text to data/raw/."""

import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PLANNING_FILE = PROJECT_ROOT / "planning.md"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"

MIN_USEFUL_CHARS = 200
REQUEST_TIMEOUT = 30
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

LOCAL_PATH_PATTERN = re.compile(
    r"^(?:sources/|data/raw/).*\.(?:pdf|txt|docx?)$",
    re.IGNORECASE,
)


def parse_documents_table(planning_path: Path) -> list[dict]:
    """Extract rows from the Documents table in planning.md."""
    lines = planning_path.read_text(encoding="utf-8").splitlines()
    in_documents = False
    rows = []

    for line in lines:
        if line.strip() == "## Documents":
            in_documents = True
            continue
        if in_documents and line.startswith("## "):
            break
        if not in_documents or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*[-#]", line):
            continue

        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0].lower() in {"#", "no."}:
            continue

        rows.append(
            {
                "source": cells[1],
                "description": cells[2],
                "url": cells[3].strip(),
            }
        )

    return rows


def is_local_file_source(url_or_path: str) -> bool:
    """Return True for local PDF/file paths that should not be scraped."""
    value = url_or_path.strip()
    if value.startswith(("http://", "https://")):
        return False
    if LOCAL_PATH_PATTERN.match(value):
        return True
    return value.lower().endswith((".pdf", ".txt", ".doc", ".docx"))


def make_filename(source: str, description: str) -> str:
    """Build a safe lowercase filename from source and description."""
    combined = f"{source} {description}".lower()
    combined = re.sub(r"[^a-z0-9]+", "_", combined)
    combined = combined.strip("_")
    return f"{combined}.txt"


def clean_html(html: str) -> str:
    """Remove boilerplate tags and return readable plain text."""
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "button", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    cleaned_lines = []
    previous_blank = False
    for line in lines:
        if not line:
            if not previous_blank:
                cleaned_lines.append("")
            previous_blank = True
        else:
            cleaned_lines.append(line)
            previous_blank = False

    return "\n".join(cleaned_lines).strip()


def fetch_page_text(url: str) -> tuple[str | None, str | None]:
    """Fetch a webpage and return cleaned text, or (None, error_message)."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, str(exc)

    content_type = response.headers.get("Content-Type", "")
    if "html" not in content_type.lower() and "<html" not in response.text[:500].lower():
        return None, f"unexpected content type: {content_type or 'unknown'}"

    text = clean_html(response.text)
    if len(text) < MIN_USEFUL_CHARS:
        return None, f"returned too little text ({len(text)} characters)"

    return text, None


def write_output_file(
    path: Path,
    source: str,
    description: str,
    url: str,
    body: str | None = None,
    manual_copy: bool = False,
    error: str | None = None,
) -> None:
    """Write a scraped (or failed) source file with a standard header."""
    lines = [
        f"Source: {source}",
        f"Description: {description}",
        f"URL: {url}",
        "",
    ]

    if manual_copy:
        lines.append("MANUAL COPY NEEDED: scraping failed or returned too little text.")
        if error:
            lines.append(f"Reason: {error}")
    else:
        lines.append(body or "")

    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> int:
    if not PLANNING_FILE.exists():
        print(f"Error: planning file not found at {PLANNING_FILE}")
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sources = parse_documents_table(PLANNING_FILE)
    scraped_ok = 0
    manual_copy = 0
    skipped_local = 0

    print(f"Found {len(sources)} sources in planning.md\n")

    for entry in sources:
        source = entry["source"]
        description = entry["description"]
        url = entry["url"]
        filename = make_filename(source, description)
        output_path = OUTPUT_DIR / filename

        if is_local_file_source(url):
            skipped_local += 1
            print(f"  SKIP (local file): {source} — {description}")
            continue

        print(f"  Scraping: {source} — {description}")
        text, error = fetch_page_text(url)

        if text is None:
            manual_copy += 1
            write_output_file(
                output_path,
                source=source,
                description=description,
                url=url,
                manual_copy=True,
                error=error,
            )
            print(f"    -> manual copy needed ({error})")
        else:
            scraped_ok += 1
            write_output_file(
                output_path,
                source=source,
                description=description,
                url=url,
                body=text,
            )
            print(f"    -> saved {filename} ({len(text)} characters)")

    webpage_count = len(sources) - skipped_local

    print("\n" + "=" * 60)
    print("SCRAPE SUMMARY")
    print("=" * 60)
    print(f"Sources found in planning.md:     {len(sources)}")
    print(f"Local files skipped:              {skipped_local}")
    print(f"Webpages attempted:               {webpage_count}")
    print(f"Successfully scraped:             {scraped_ok}")
    print(f"Need manual copy/paste:           {manual_copy}")
    print(f"Output directory:                 {OUTPUT_DIR}")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
