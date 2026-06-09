# Evaluation Results — The Unofficial Guide

Fill in **Accuracy judgment** and **Notes** for each question after reviewing.

## Question 1

**Question:** Which UCSC CSE classes do students mention as especially important for CS majors?

**Top-k:** 5

**Expected answer:**
Students mention CSE 130 with Harrison as useful for systems, CSE 113 with Sorensen for multithreading, CSE 186/CSE 187 with Harrison for full-stack web development, and CSE 138 with Kuper for distributed systems, microservices, and REST APIs. The strongest recommendations are CSE 138 and full-stack web development because students say those apply to a broader set of jobs. Other recommended classes depend on interest area, such as CSE 150/156 for networking, CSE 140/144 for AI/ML, CSE 160/164/168 for graphics/computer vision, CSE 104/105 for math, and CSE 180/181 for databases.

**System answer:**
According to the provided context, the following UCSC CSE classes are mentioned as important for CS majors: 
CSE 101 - Introduction to Data Structures and Algorithms (reddit_example_cs_path.txt), 
which is also mentioned as a required course. 
Other classes mentioned in the context that are likely important for CS majors include CSE 102, CSE 103, CSE 110A, CSE 111, CSE 114A, CSE 120, CSE 130, CSE 140, CSE 160, CSE 180 (github_ucsc_cs_student_guide.txt). 
However, only CSE 101 is explicitly mentioned by a student as a required course (reddit_example_cs_path.txt).

Sources used:
- reddit_example_cs_path.txt
- reddit_how_is_ucsc_cs_program.txt
- github_ucsc_cs_student_guide.txt

**Sources used:**
- reddit_example_cs_path.txt
- reddit_how_is_ucsc_cs_program.txt
- github_ucsc_cs_student_guide.txt

**Retrieved chunks:**
**Rank:** 1
**Distance:** 0.513622
**Source:** reddit_example_cs_path.txt
**Chunk ID:** reddit_example_cs_path_0001

**Text preview:**
```text
Post:
The classes I took for my Computer Science B.S. degree at UC Santa Cruz
I transferred to UCSC in Fall 2020 from a community college, so I'll only be giving my experience with the CSE upper-division courses I took each quarter. Every class I took was remote, but I think some people might find this useful.
I want to post this for people who want to see what CSE upper-division courses you would take as a Computer Science student and hopefully answer some questions about the Computer Science degree at UCSC.
This is my review about each class and professor. If you disagree with what I said, please be respectful.
Fall 2020:
CSE 101: Data Structures and Algorithms
Professor: Patrick Tantalo
Rating: 10/10
Required course
```

**Rank:** 2
**Distance:** 0.568959
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0001

**Text preview:**
```text
Post:
CS major: How is UCSC program?
I was accepted into pre-CS major. How is the program? Difficult to get classes? How's campus life and housing? Pros/cons?
Comments:
- ClassroomUnit003:
Everyone enters in proposed status. This just means there are a handful of classes you need to complete to declare. I have really enjoyed CS. CS major status at UCSC gives you really high priority for classes. I never had issues getting into any of the classes I needed. On top of that, UCSC prioritizes having the necessary CS classes you need to graduate every quarter. Some majors only offer a class once a quarter, but most CS classes are offered every quarter.
```

**Rank:** 3
**Distance:** 0.583572
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0013

**Text preview:**
```text
.
Classes
The classes at UCSC are structured such that the subject comes first, followed by their course number, followed by the course title. In other words,
subject course_number - course_title
. Lower division courses range from 1 - 99, upper division courses from 100 - 199, and seminars/graduate courses are 200+. Some common subjects can be seen in the chart below.
Subject
Acronym
Computer Science & Engineering
CSE
Computational Media
CMPM
Mathematics
MATH
Statistics
STAT
Writing
WRIT
List of Classes:
AM 10 - Mathematical Methods for Engineers I
CMPM 120 - Game Development Experience
CMPM 147 - Generative Design
CMPM 170-172 - Game Design Studio
CSE 12 - Computer Systems and Assembly Language and Lab
CSE 13S - Comp Sys and C Program
CSE 16 - Applied Discrete Mathematics
CSE 20 - Beginning Programming in Python
CSE 30 - Programming Abstractions: Python
CSE 101 - Introduction to Data Structures and Algorithms
CSE 102 - Introduction to Analysis of Algorithms
CSE 103 - Computational Mo...
```

**Rank:** 4
**Distance:** 0.621097
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0001

**Text preview:**
```text
GitHub - williamsantosa/ucsc-cs: Guide to UCSC's Computer Science Majors 🖥⌨ · GitHub
williamsantosa
/
ucsc-cs
Public
You must be signed in to change notification settings
3
28
Name
Name
Latest commit
History
89 Commits
89 Commits
Classes
Classes
Media
Media
Professors
Professors
LICENSE
LICENSE
README.md
README.md
A Guide to the University of California, Santa Cruz's Computer Science Majors
The University of California, Santa Cruz's campus
```

**Rank:** 5
**Distance:** 0.639321
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0014

**Text preview:**
```text
CSE 103 - Computational Models
CSE 110A - Fundamentals of Compiler Design I
CSE 111 - Advanced Programming
CSE 114A - Foundations of Programming Languages
CSE 120 - Computer Architecture
CSE 130 - Principles of Computer Systems Design
CSE 140 - Artificial Intelligence
CSE 160 - Introduction to Computer Graphics
CSE 180 - Database Systems I
CSE 185S - Technical Writing and Communication in Computer Science
CSE 186 - Full Stack Web Development I
MATH 19A - Calculus for Science, Engineering, and Mathematics
MATH 19B - Calculus for Science, Engineering, and Mathematics
MATH 23A - Vector Calculus
STAT 131 - Introduction to Probability Theory
Professors
There are plenty of Professors at UCSC, all of which are notable in their own field of study. Below are some of the Professors you may meet.
List of Professors:
Darrell Long
David Harrison
Gerald Moulds
Lindsey Kuper
Sagnik Nath
Patrick Tantalo
Preparing for University
Having come into University with minimal Computer Science experience, ther...
```

**Accuracy judgment:** Partially accurate

**Notes:** The system answered with some relevant CS classes, especially CSE 101 and a general list including CSE 130, CSE 140, CSE 160, CSE 180, and CSE 186. Although it missed a few key classes from the expected answer, including CSE 113, CSE 138, CSE 186/CSE 187 as full-stack job-focused courses, and the interest-area groupings from the Reddit source. The main issue was retrieval: the most relevant `reddit_important_cs_classes.txt` chunk was not retrieved for this query, so generation could not include the strongest expected evidence. 

---

## Question 2

**Question:** What are common pros and cons students mention about UCSC CS?

**Top-k:** 5

**Expected answer:**
Students describe UCSC CS positively overall, saying the program has good younger professors, interesting classes, high class-enrollment priority for declared CS majors, and many required CS classes offered frequently. Students also say it is possible to build strong skills if you choose challenging classes and professors carefully. Common negatives are that students do not get to specialize until later in the major, the core classes may not clearly show what area of CS to pursue, housing in Santa Cruz is limited and expensive, and students need to plan early for both classes and housing.

**System answer:**
Based on the provided context, some common pros mentioned by students about UCSC CS include: 
- High priority for CS classes, making it easy to get into necessary classes (reddit_how_is_ucsc_cs_program.txt | Chunk ID: reddit_how_is_ucsc_cs_program_0001)
- Fantastic professors who are really into the material they teach (reddit_how_is_ucsc_cs_program.txt | Chunk ID: reddit_how_is_ucsc_cs_program_0013)
- Most CS classes are offered every quarter, helping students graduate in 4 years (reddit_how_is_ucsc_cs_program.txt | Chunk ID: reddit_how_is_ucsc_cs_program_0001)

Some common cons mentioned by students include:
- Some professors expecting more from students due to prior lack of rigor (reddit_how_is_ucsc_cs_program.txt | Chunk ID: reddit_how_is_ucsc_cs_program_0013)
- Some topics being tough, with assumptions of prior knowledge that may not have been taught (reddit_how_is_ucsc_cs_program.txt | Chunk ID: reddit_how_is_ucsc_cs_program_0013)

Sources used:
- reddit_how_is_ucsc_cs_program.txt
- github_ucsc_cs_student_guide.txt
- reddit_example_cs_path.txt

**Sources used:**
- reddit_how_is_ucsc_cs_program.txt
- github_ucsc_cs_student_guide.txt
- reddit_example_cs_path.txt

**Retrieved chunks:**
**Rank:** 1
**Distance:** 0.540999
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0001

**Text preview:**
```text
Post:
CS major: How is UCSC program?
I was accepted into pre-CS major. How is the program? Difficult to get classes? How's campus life and housing? Pros/cons?
Comments:
- ClassroomUnit003:
Everyone enters in proposed status. This just means there are a handful of classes you need to complete to declare. I have really enjoyed CS. CS major status at UCSC gives you really high priority for classes. I never had issues getting into any of the classes I needed. On top of that, UCSC prioritizes having the necessary CS classes you need to graduate every quarter. Some majors only offer a class once a quarter, but most CS classes are offered every quarter.
```

**Rank:** 2
**Distance:** 0.774753
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0013

**Text preview:**
```text
The issue of some professors expecting more while students are not prepared due to prior lack of rigor is constantly being worked on by adding new CS prerequisites and teachers like Long retiring, so the CS department is trying to help alleviate that.
Not to say that lack of rigor is a bad thing, because some topics are just tough. But as someone who started as a freshman here, I can say there were classes where things were assumed that I knew, like makefiles in CSE 13S, that just did not get taught to us, so it was a struggle. Eventually they fixed that in later versions of the course, but it is still a work in progress.
I have very few bad things to say about the UCSC CSE program, as it has mostly fantastic professors who are really into the material they teach. There is a reason more than half of them have a 4 or higher on Rate My Professor.
- gwendlynn123:
Thanks for all the feedback. This is very helpful. I will be at admit day and am looking forward to learning more about the pro...
```

**Rank:** 3
**Distance:** 0.824965
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0021

**Text preview:**
```text
Thank you to our Professors for the wonderful education.
Further Learning Material
Overleaf LaTeX Tutorial
Learn Python
References
https://www.ratemyprofessors.com/
https://courses.soe.ucsc.edu/
https://lookout.co/santacruz/education/higher-ed/story/2021-03-07/ucsc-local-governments-approach-collision-over-enrollment-growth
https://registrar.ucsc.edu/catalog/archive/15-16/programs-courses/program-statements/cmps.html
About
Guide to UCSC's Computer Science Majors 🖥⌨
Topics
computer-science
education
algorithms
guide
data-structures
ucsc
game-design
ucsc-classes
ucsc-courses
Resources
Readme
License
GPL-3.0 license
.
Activity
Stars
28
stars
Watchers
1
watching
Forks
3
forks
Report repository
Contributors
.
```

**Rank:** 4
**Distance:** 0.828845
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0001

**Text preview:**
```text
GitHub - williamsantosa/ucsc-cs: Guide to UCSC's Computer Science Majors 🖥⌨ · GitHub
williamsantosa
/
ucsc-cs
Public
You must be signed in to change notification settings
3
28
Name
Name
Latest commit
History
89 Commits
89 Commits
Classes
Classes
Media
Media
Professors
Professors
LICENSE
LICENSE
README.md
README.md
A Guide to the University of California, Santa Cruz's Computer Science Majors
The University of California, Santa Cruz's campus
```

**Rank:** 5
**Distance:** 0.832054
**Source:** reddit_example_cs_path.txt
**Chunk ID:** reddit_example_cs_path_0001

**Text preview:**
```text
Post:
The classes I took for my Computer Science B.S. degree at UC Santa Cruz
I transferred to UCSC in Fall 2020 from a community college, so I'll only be giving my experience with the CSE upper-division courses I took each quarter. Every class I took was remote, but I think some people might find this useful.
I want to post this for people who want to see what CSE upper-division courses you would take as a Computer Science student and hopefully answer some questions about the Computer Science degree at UCSC.
This is my review about each class and professor. If you disagree with what I said, please be respectful.
Fall 2020:
CSE 101: Data Structures and Algorithms
Professor: Patrick Tantalo
Rating: 10/10
Required course
```

**Accuracy judgment:** Partially accurate

**Notes:** The system correctly identified several major pros, including high priority for CS classes, frequent CS course offerings, and strong professors. It also mentioned some cons related to rigor, uneven preparation, and assumed prior knowledge. Although it missed  expected negatives such as housing problems, late specialization, and core classes not helping students decide their CS focus, the provided answer was extremely accurate. But even though the answer is grounded and accurate, it is incomplete because retrieval mostly surfaced one Reddit thread and did not retrieve the chunks with the full housing/specialization discussion.

---

## Question 3

**Question:** Which professors or teachers are recommended by students in the collected sources?

**Top-k:** 5

**Expected answer:**
Students recommend Sesh, Fremont, Harrison, Sorensen, Kuper, Tantalo, De Alfaro, Miller, Qian, and Alvaro. Harrison receives the strongest mixed recommendation: students say his classes are hard and demanding, but that students "level up" as software engineers after taking his classes, especially full-stack or systems courses. Sorensen and Kuper are recommended for interesting upper-division electives, and Alvaro is mentioned positively for CSE 138.

**System answer:**
According to the collected sources, the following professors are recommended by students: 
- Sesh (reddit_best_professors.txt)
- Fremont (reddit_best_professors.txt)
- Harrison (reddit_best_professors.txt)
- Sorensen (reddit_best_professors.txt)
- Kuper (reddit_best_professors.txt)
- Tantalo (reddit_best_professors.txt)

These professors are mentioned as being good for various classes, with some students having strong preferences for certain professors, such as Harrison and Sorensen (reddit_best_professors.txt).

Sources used:
- github_ucsc_cs_student_guide.txt
- reddit_best_professors.txt

**Sources used:**
- github_ucsc_cs_student_guide.txt
- reddit_best_professors.txt

**Retrieved chunks:**
**Rank:** 1
**Distance:** 1.069123
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0018

**Text preview:**
```text
Baskin School of Engineering (BSOE/RTA System)
The Baskin School of Engineering offers tutor and reader positions for students. Students have to apply
here
and specify the class and professor they want to work for. Applications generally open up near the end of the prior quarter.
Learning Support Services (LSS)
Learning Support Services sometimes email students with good academic standing to tutor for a recently completed class. Alternatively, students may also apply
here
to work as well.
Note Taking
Sometimes, if a student has good academic standing, they will get emailed to take notes for a currently enrolled class. They offer $25 per class unit, e.g. $125 for a 5-unit class. I would generally shy away from this offer unless you religiously take notes, as you are required to take notes on every single lecture.
RateMyProfessor
RateMyProfessor
is a useful website which has fairly accurate reviews of professors. Keep in mind, however, that most of the people who post a review either lov...
```

**Rank:** 2
**Distance:** 1.111121
**Source:** reddit_best_professors.txt
**Chunk ID:** reddit_best_professors_0001

**Text preview:**
```text
Post:
Who are the best teachers for CS at UCSC? I am aware that “best” teacher is subjective for everyone, especially since in the CS department, the harder classes make you better, while other students prefer easy classes, but I still want to know which teachers to take.
Comments:
- Sdrater3: Sesh, Fremont, and Harrison are good for the mandatory upper-division classes. Sorensen and Kuper both taught really interesting upper-division electives. If I had to pick one, Harrison. You level up as a software engineer each time you survive a Harrison class.
- Opposite-Kale1224: Tyler Sorensen, hands down.
- tony_resta: I can back this.
- ACatNamedFreddie: Tantalo was my favorite. He also gives extensions.
- domgada: Tantalo is a good time. I feel like his teaching is pretty mid, but the dude is a vibe.
```

**Rank:** 3
**Distance:** 1.177756
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0014

**Text preview:**
```text
CSE 103 - Computational Models
CSE 110A - Fundamentals of Compiler Design I
CSE 111 - Advanced Programming
CSE 114A - Foundations of Programming Languages
CSE 120 - Computer Architecture
CSE 130 - Principles of Computer Systems Design
CSE 140 - Artificial Intelligence
CSE 160 - Introduction to Computer Graphics
CSE 180 - Database Systems I
CSE 185S - Technical Writing and Communication in Computer Science
CSE 186 - Full Stack Web Development I
MATH 19A - Calculus for Science, Engineering, and Mathematics
MATH 19B - Calculus for Science, Engineering, and Mathematics
MATH 23A - Vector Calculus
STAT 131 - Introduction to Probability Theory
Professors
There are plenty of Professors at UCSC, all of which are notable in their own field of study. Below are some of the Professors you may meet.
List of Professors:
Darrell Long
David Harrison
Gerald Moulds
Lindsey Kuper
Sagnik Nath
Patrick Tantalo
Preparing for University
Having come into University with minimal Computer Science experience, ther...
```

**Rank:** 4
**Distance:** 1.212880
**Source:** reddit_best_professors.txt
**Chunk ID:** reddit_best_professors_0006

**Text preview:**
```text
- throwawayowaowa: I thought I saw Miller's name on next year's schedule. It is sad to lose two tenured professors in one go.
- Carbinkisgod: I believe Fall CSE 13S two quarters ago was Miller's last class.
- UCSC_CE_prof_M: CSE 13S in Fall 2022 was my last undergraduate class before retirement. I am teaching a graduate seminar on archival storage systems in Spring 2023. The department can ask emeritus faculty to teach classes through recall, but the department has to ask and the faculty member has to agree. I am very unlikely to teach CSE 13S again unless it is an honors section.
- Deleted commenter: Professor Miller, can you give more insight into what is happening at the university? Some students feel Professor Long and faculty from your research group were holding up department standards, and that it is not a coincidence that many of you are leaving at the same time.
```

**Rank:** 5
**Distance:** 1.233046
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0002

**Text preview:**
```text
Media
Media
Professors
Professors
LICENSE
LICENSE
README.md
README.md
A Guide to the University of California, Santa Cruz's Computer Science Majors
The University of California, Santa Cruz's campus
This guide is intended to be read by prospective computer science students and incoming freshmen; however, current students may find portions of the text to be useful as well. Includes information on the Bachelor of Science and Bachelor of Arts in Computer Science majors, as well as the Bachelor of Science in Computer Science: Computer Game Design (CSGD) major. Among other things, contains descriptions of relevant courses, discussion on programming languages you will use, requirements to graduate, as well as ratings on professors, and classes you will encounter.
Contributors
Authors:
William Santosa -
Email
|
Website
|
LinkedIn
|
GitHub
Gregory Santosa -
Email
|
LinkedIn
|
GitHub
Arrian Chi -
Email
|
Website
|
LinkedIn
|
GitHub
Media:
William Santosa -
Email
|
Website
|
LinkedIn
|
GitHub
Tab...
```

**Accuracy judgment:** Partially accurate

**Notes:** The system correctly identified several recommended instructors: Sesh, Fremont, Harrison, Sorensen, Kuper, and Tantalo. Although, it did miss a few professors like De Alfaro, Miller, Qian, and Alvaro from the expected answer. And although it did not fully explain the mixed nature of Harrison recommendations beyond saying students have strong preferences, it correctly answers the question asked. This is mainly a retrieval weakness: the best professor recommendation chunk appeared at rank 2, while rank 1 was a less relevant GitHub chunk about tutoring and RateMyProfessor.

---

## Question 4

**Question:** What official requirements or course categories are listed for the UCSC CS B.S.?

**Top-k:** 10

**Expected answer:**
The UCSC CS B.S. curriculum includes lower-division programming courses such as CSE 20, CSE 30, CSE 12, and CSE 13S; math courses such as calculus, discrete math, linear algebra, and probability/statistics; upper-division core courses such as CSE 101, CSE 102, CSE 103, CSE 114A, CSE 120, and CSE 130; a Disciplinary Communication requirement; a comprehensive/capstone requirement; and four upper-division electives. The curriculum chart also says upper-division electives are generally 5-credit upper-division CSE/CE courses numbered 100–189, CSE 195, or approved computational media/math electives, with some restrictions.

**System answer:**
According to the provided sources, specifically (github_ucsc_cs_student_guide.txt | Chunk ID: github_ucsc_cs_student_guide_0012) and (official_ucsc_page_ucsc_cs_major_introduction.txt | Chunk ID: official_ucsc_page_ucsc_cs_major_introduction_0008), the official requirements for the UCSC CS B.S. include:
1. General Education requirements
2. Major Requirements, which can be found in the curriculum charts for B.S in Computer Science, B.A in Computer Science, and B.S in Computer Science: Computer Game Design.
Additionally, (official_ucsc_page_ucsc_cs_major_introduction.txt | Chunk ID: official_ucsc_page_ucsc_cs_major_introduction_0008) mentions that the combined GPA in five specific courses must be at least a 3.0, and transfer students have specific requirements to complete before arriving at UC Santa Cruz.
(pdf_cs_degree_curriculum_chart.txt | Chunk ID: pdf_cs_degree_curriculum_chart_0006) also lists Physics Requirement and Grade Rules as part of the CS B.S. major requirements.

Sources used:
- github_ucsc_cs_student_guide.txt
- pdf_cs_degree_curriculum_chart.txt
- reddit_how_is_ucsc_cs_program.txt
- official_ucsc_page_ucsc_cs_major_introduction.txt
- reddit_example_cs_path.txt

**Sources used:**
- github_ucsc_cs_student_guide.txt
- pdf_cs_degree_curriculum_chart.txt
- reddit_how_is_ucsc_cs_program.txt
- official_ucsc_page_ucsc_cs_major_introduction.txt
- reddit_example_cs_path.txt

**Retrieved chunks:**
**Rank:** 1
**Distance:** 0.619538
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0013

**Text preview:**
```text
.
Classes
The classes at UCSC are structured such that the subject comes first, followed by their course number, followed by the course title. In other words,
subject course_number - course_title
. Lower division courses range from 1 - 99, upper division courses from 100 - 199, and seminars/graduate courses are 200+. Some common subjects can be seen in the chart below.
Subject
Acronym
Computer Science & Engineering
CSE
Computational Media
CMPM
Mathematics
MATH
Statistics
STAT
Writing
WRIT
List of Classes:
AM 10 - Mathematical Methods for Engineers I
CMPM 120 - Game Development Experience
CMPM 147 - Generative Design
CMPM 170-172 - Game Design Studio
CSE 12 - Computer Systems and Assembly Language and Lab
CSE 13S - Comp Sys and C Program
CSE 16 - Applied Discrete Mathematics
CSE 20 - Beginning Programming in Python
CSE 30 - Programming Abstractions: Python
CSE 101 - Introduction to Data Structures and Algorithms
CSE 102 - Introduction to Analysis of Algorithms
CSE 103 - Computational Mo...
```

**Rank:** 2
**Distance:** 0.668178
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0003

**Text preview:**
```text
Table of Contents
A Guide to the University of California, Santa Cruz's Computer Science Majors
Contributors
Table of Contents
Introduction
Quick Note for Non-CS admittees
What is Computer Science?
Bachelor of Art or Science?
Computer Science: Computer Game Design
Subjects
Languages
Graduation Requirements
General Education
Major Requirements (2022-2023)
Classes
Professors
Preparing for University
Planning for Graduate School
Talking to Professors
Maintain a good GPA
Research Experience
Tips and Tricks
Tutoring, Reading, & Note Taking
Baskin School of Engineering (BSOE/RTA System)
Learning Support Services (LSS)
Note Taking
RateMyProfessor
Best Locations
Study Locations
Overnight Areas
Bathrooms
Services
Counseling & Psychological Services (CAPS)
Slug Support Pantry
Disability Resource Center (DRC)
Acknowledgements
Further Learning Material
References
Introduction
The University of California, Santa Cruz, is well known for its beautiful campus and excellent education. The B.S in Comput...
```

**Rank:** 3
**Distance:** 0.703647
**Source:** pdf_cs_degree_curriculum_chart.txt
**Chunk ID:** pdf_cs_degree_curriculum_chart_0006

**Text preview:**
```text
- CMPM 172: Game Production Studio
Physics Requirement:
Students must complete one of the following combinations:
- PHYS 5A and PHYS 5B
- PHYS 5A and PHYS 5C
- PHYS 6A and PHYS 6B
- PHYS 6A and PHYS 6C
Note: Physics courses have co-requisite labs required for enrollment. These labs are not part of the Computer Science B.S. major requirements.
Grade Rules:
All courses being applied to Computer Science major requirements must be taken for a letter grade. Grades of P do not count toward major requirements.
Courses with grades of C-, D+, D, or D- earn credit toward graduation, but cannot be used to satisfy a major requirement, a general education requirement, or a prerequisite for another course.
Other Notes:
- Shaded boxes on the chart represent major qualification courses.
- Many graduate courses can also be used to satisfy electives, but students need instructor and department approval.
- The Baskin Engineering major declaration process requires an earlier start than the UCSC Academic/A...
```

**Rank:** 4
**Distance:** 0.705650
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0001

**Text preview:**
```text
Post:
CS major: How is UCSC program?
I was accepted into pre-CS major. How is the program? Difficult to get classes? How's campus life and housing? Pros/cons?
Comments:
- ClassroomUnit003:
Everyone enters in proposed status. This just means there are a handful of classes you need to complete to declare. I have really enjoyed CS. CS major status at UCSC gives you really high priority for classes. I never had issues getting into any of the classes I needed. On top of that, UCSC prioritizes having the necessary CS classes you need to graduate every quarter. Some majors only offer a class once a quarter, but most CS classes are offered every quarter.
```

**Rank:** 5
**Distance:** 0.710587
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0001

**Text preview:**
```text
GitHub - williamsantosa/ucsc-cs: Guide to UCSC's Computer Science Majors 🖥⌨ · GitHub
williamsantosa
/
ucsc-cs
Public
You must be signed in to change notification settings
3
28
Name
Name
Latest commit
History
89 Commits
89 Commits
Classes
Classes
Media
Media
Professors
Professors
LICENSE
LICENSE
README.md
README.md
A Guide to the University of California, Santa Cruz's Computer Science Majors
The University of California, Santa Cruz's campus
```

**Rank:** 6
**Distance:** 0.740318
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0012

**Text preview:**
```text
Graduation Requirements
Everyone wants to graduate... which means it is imperative that you plan out your classes ahead of time! Below are the requirements to graduate.
General Education
General education requirements can be found
here
at the Registrar. It is recommended that you do not rush through the GEs as they can be finished quite quickly if you take 1 or 2 per quarter. Instead, space them out throughout your undergraduate career, as they are useful in padding classes during difficult quarters.
Major Requirements (2022-2023)
The curriculum charts can be found
here
at the university's webpage. More specifically,
B.S in Computer Science
,
B.A in Computer Science
, and
B.S in Computer Science: Computer Game Design
.
Major Requirements (2023-2024)
The curriculum charts can be found
here
at the university's webpage. More specifically,
B.S in Computer Science
,
B.A in Computer Science
, and
B.S in Computer Science: Computer Game Design
.
Classes
The classes at UCSC are structured such ...
```

**Rank:** 7
**Distance:** 0.765214
**Source:** official_ucsc_page_ucsc_cs_major_introduction.txt
**Chunk ID:** official_ucsc_page_ucsc_cs_major_introduction_0008

**Text preview:**
```text
5
Plus one of the following
MATH 19B
Calculus for Science, Engineering, and Mathematics
5
MATH 20B
Honors Calculus
5
Minimum GPA
The combined GPA in the five courses above must be at least a 3.0.
Furthermore, transfer students entering in the fall must have completed at least three of these courses by the end of the fall term of the previous academic year and have a minimum 3.0 GPA over all completed CS major qualification courses at that time.
Transfer students are strongly recommended to complete one course out of
MATH 21
,
AM 10
,
MATH 23A
or
AM 30
, and most general education requirements prior to arriving at UC Santa Cruz.
Most courses in the computer science program at UC Santa Cruz have a strong theoretical component to prepare the student for designing, as opposed to simply using, computer systems. Often, courses taken at other institutions which emphasize applications of current languages and computers do not count toward the computer science major at UCSC.
At UCSC, computer s...
```

**Rank:** 8
**Distance:** 0.779344
**Source:** official_ucsc_page_ucsc_cs_major_introduction.txt
**Chunk ID:** official_ucsc_page_ucsc_cs_major_introduction_0015

**Text preview:**
```text
Community Colleges courses once enrolled at UCSC
Once enrolled in Baskin Engineering students who wish to take a course at a California community college must first check
Assist.org
to see if the course is equivalent at UC Santa Cruz. If the course is not listed on Assist.org, students must submit a course substitution petition to the BE Undergraduate Advising Office to have it reviewed for equivalency. Courses that need to be reviewed must be accompanied by a course description and syllabus. It is very helpful if students can provide further evidence of course content, such as examples of programming assignments, homework, or examinations. To guarantee equivalency, departments may sometimes require a grade of B or better.
If the course is approved for equivalency or was on Assist.org, then students with declared majors must also receive approval by their major department to take the class at the community college PRIOR to taking it. Undeclared students must receive prior approval from...
```

**Rank:** 9
**Distance:** 0.787466
**Source:** official_ucsc_page_ucsc_cs_major_introduction.txt
**Chunk ID:** official_ucsc_page_ucsc_cs_major_introduction_0016

**Text preview:**
```text
Undeclared students must receive prior approval from the CSE Department to substitute a course for
CSE 13S
. Undeclared students do not require prior approval for other courses listed on Assist.org. Forms and procedures for approval can be obtained from and submitted to the BE Undergraduate Advising Office.
Four-Year Institutions and the UC Education Abroad Program (UCEAP)
Students who intend to take a course at a four-year institution or UC Education Abroad, must submit a Course Substitution Petition to the BE Undergraduate Advising Office to have the course reviewed for equivalency. Courses that need to be reviewed must be accompanied by a course description and syllabus. It is very helpful if students can provide further evidence of course content, such as examples of programming assignments, homework, or examinations. To guarantee equivalency, departments may sometimes require a grade of B or better.
Double Majors and Major/Minor Combinations Policy
Students may not receive both th...
```

**Rank:** 10
**Distance:** 0.790078
**Source:** reddit_example_cs_path.txt
**Chunk ID:** reddit_example_cs_path_0001

**Text preview:**
```text
Post:
The classes I took for my Computer Science B.S. degree at UC Santa Cruz
I transferred to UCSC in Fall 2020 from a community college, so I'll only be giving my experience with the CSE upper-division courses I took each quarter. Every class I took was remote, but I think some people might find this useful.
I want to post this for people who want to see what CSE upper-division courses you would take as a Computer Science student and hopefully answer some questions about the Computer Science degree at UCSC.
This is my review about each class and professor. If you disagree with what I said, please be respectful.
Fall 2020:
CSE 101: Data Structures and Algorithms
Professor: Patrick Tantalo
Rating: 10/10
Required course
```

**Accuracy judgment:** Partially accurate

**Notes:** The system gave a grounded answer and correctly mentioned general education, major requirements, transfer qualification/GPA information, physics requirements, and grade rules. However, it did not provide the complete expected CS B.S. requirement categories: lower-division programming courses, math courses, upper-division core courses, four upper-division electives, DC requirement, and capstone/comprehensive requirement. This is the clearest failure case. The relevant curriculum chart information existed in the sources, but retrieval surfaced the wrong PDF chunk and several weaker GitHub/official chunks instead of the strongest curriculum-chart chunk.

---

## Question 5

**Question:** Does the system have enough information to compare UCSC CS to UC Davis CS?

**Top-k:** 5

**Expected answer:**
No. The collected documents focus on UCSC CS courses, professors, requirements, and student experiences. Unless one of the collected sources specifically discusses UC Davis, the system should say it does not have enough information to make a grounded comparison between UCSC CS and UC Davis CS. It should not guess using outside knowledge.

**System answer:**
I don't have enough information in the provided sources to answer that.

Sources used:
- reddit_how_is_ucsc_cs_program.txt
- reddit_example_cs_path.txt
- reddit_ucsc_cs_major_faq.txt
- github_ucsc_cs_student_guide.txt

**Sources used:**
- reddit_how_is_ucsc_cs_program.txt
- reddit_example_cs_path.txt
- reddit_ucsc_cs_major_faq.txt
- github_ucsc_cs_student_guide.txt

**Retrieved chunks:**
**Rank:** 1
**Distance:** 0.833472
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0001

**Text preview:**
```text
Post:
CS major: How is UCSC program?
I was accepted into pre-CS major. How is the program? Difficult to get classes? How's campus life and housing? Pros/cons?
Comments:
- ClassroomUnit003:
Everyone enters in proposed status. This just means there are a handful of classes you need to complete to declare. I have really enjoyed CS. CS major status at UCSC gives you really high priority for classes. I never had issues getting into any of the classes I needed. On top of that, UCSC prioritizes having the necessary CS classes you need to graduate every quarter. Some majors only offer a class once a quarter, but most CS classes are offered every quarter.
```

**Rank:** 2
**Distance:** 0.900470
**Source:** reddit_example_cs_path.txt
**Chunk ID:** reddit_example_cs_path_0001

**Text preview:**
```text
Post:
The classes I took for my Computer Science B.S. degree at UC Santa Cruz
I transferred to UCSC in Fall 2020 from a community college, so I'll only be giving my experience with the CSE upper-division courses I took each quarter. Every class I took was remote, but I think some people might find this useful.
I want to post this for people who want to see what CSE upper-division courses you would take as a Computer Science student and hopefully answer some questions about the Computer Science degree at UCSC.
This is my review about each class and professor. If you disagree with what I said, please be respectful.
Fall 2020:
CSE 101: Data Structures and Algorithms
Professor: Patrick Tantalo
Rating: 10/10
Required course
```

**Rank:** 3
**Distance:** 0.916885
**Source:** reddit_ucsc_cs_major_faq.txt
**Chunk ID:** reddit_ucsc_cs_major_faq_0005

**Text preview:**
```text
It is a basic calculator, but it also saves states and can recurse, which is pretty cool.
CSE 186: at the end of it you make a Slack clone, basically Discord without voice channels.
These are just the classes that I have taken so far.
11. 20 percent of majors at UCSC are computer science. Chances are, you will find a group of friends taking the same classes as you.
12. For the major required classes, typically 100-200 people. Some upper-division electives are pretty small. Right now I am about to take embedded operating systems with 50 people in it.
```

**Rank:** 4
**Distance:** 0.935919
**Source:** reddit_how_is_ucsc_cs_program.txt
**Chunk ID:** reddit_how_is_ucsc_cs_program_0013

**Text preview:**
```text
The issue of some professors expecting more while students are not prepared due to prior lack of rigor is constantly being worked on by adding new CS prerequisites and teachers like Long retiring, so the CS department is trying to help alleviate that.
Not to say that lack of rigor is a bad thing, because some topics are just tough. But as someone who started as a freshman here, I can say there were classes where things were assumed that I knew, like makefiles in CSE 13S, that just did not get taught to us, so it was a struggle. Eventually they fixed that in later versions of the course, but it is still a work in progress.
I have very few bad things to say about the UCSC CSE program, as it has mostly fantastic professors who are really into the material they teach. There is a reason more than half of them have a 4 or higher on Rate My Professor.
- gwendlynn123:
Thanks for all the feedback. This is very helpful. I will be at admit day and am looking forward to learning more about the pro...
```

**Rank:** 5
**Distance:** 0.958435
**Source:** github_ucsc_cs_student_guide.txt
**Chunk ID:** github_ucsc_cs_student_guide_0001

**Text preview:**
```text
GitHub - williamsantosa/ucsc-cs: Guide to UCSC's Computer Science Majors 🖥⌨ · GitHub
williamsantosa
/
ucsc-cs
Public
You must be signed in to change notification settings
3
28
Name
Name
Latest commit
History
89 Commits
89 Commits
Classes
Classes
Media
Media
Professors
Professors
LICENSE
LICENSE
README.md
README.md
A Guide to the University of California, Santa Cruz's Computer Science Majors
The University of California, Santa Cruz's campus
```

**Accuracy judgment:** Accurate

**Notes:** The system correctly refused to compare UCSC CS to UC Davis CS because the provided sources focus on UCSC and do not contain enough information for a grounded comparison. This is the expected behavior for an out-of-scope question. The answer did not hallucinate a comparison or use outside knowledge.

---

## Overall Evaluation Summary

The system performed best on grounded student-opinion questions when retrieval returned the relevant Reddit chunks. It successfully enforced grounding by citing source filenames and refusing to answer the out-of-scope UC Davis comparison question. The main weakness was retrieval quality for broad questions: sometimes the vector store returned general GitHub or official catalog chunks instead of the most directly relevant Reddit or curriculum-chart chunks. Because the generation step only answers from retrieved context, missing retrieval evidence led to incomplete answers rather than hallucinated ones.

## Failure Case

The clearest failure case was Question 4: “What official requirements or course categories are listed for the UCSC CS B.S.?” The system’s answer was only partially accurate. It mentioned general education, major requirements, transfer GPA rules, physics requirements, and grade rules, but it did not list the full expected curriculum categories such as lower-division programming courses, upper-division core courses, DC requirement, capstone/comprehensive requirement, and four upper-division electives.

The cause was retrieval, not generation. The relevant information existed in `pdf_cs_degree_curriculum_chart.txt`, but retrieval returned `pdf_cs_degree_curriculum_chart_0006`, which mostly contained physics and grade rules, instead of the stronger curriculum-chart chunk that listed lower-division courses, upper-division courses, electives, DC, and capstone requirements. Because the prompt forced the LLM to use only retrieved context, the model stayed grounded and gave an incomplete answer instead of inventing the missing requirements.

---