#! Python3
import re

resume=('''Jesse Kendall
1801 Fayetteville Street, Durham, NC 27702
C: 919-530-6337 | H: 919-555-5555
jessek@nccu.edu
PROFILE: Results-driven education and organization leadership professional with expertise in developing support
services and instructional programs that improve low performing elementary schools
EDUCATION
North Carolina Central University Durham, NC
Master of School Administration May 2014
Strayer University Cary, NC
Masters Certificate in HR Strategic Organization Leadership May 2005
Villanova University Villanova, PA
Bachelor of Arts in English May 2002
PROFESSIONAL EXPERIERNCE
ABC Public Schools Durham, NC
Principal Intern, BCD Elementary School September 2013 – Present
 Collaborated with teachers and administrators to devise a school schedule that maximized math instruction time.
 Restructured the daily schedule to better utilize extracurricular staff and provide additional support for students
not meeting benchmarks in math and reading.
 Designed a curriculum map to connect the teaching of social studies and reading, which also resolved the lack of
time issue to teach social studies content.
 Partnered with on-site afterschool program director to implement new marketing strategies, which increase
student participation by 40%.
 Formed a committee of teachers and parents to reduce referrals and special education placements by 10%.
XYZ Public Schools Raleigh, NC
Teacher, Alphabet Elementary School September 2010 – May 2013
 Developed lessons plans and instructional materials for 2nd and 3rd graders, which provided individualized and
group instruction in order to adapt to the curriculum needs of each student.
 Utilized various instructional strategies such as inquiry, group discussion, and discovery projects to engage
students.
 Established a student behavior point system to achieve a functional learning atmosphere in the classroom.
 Administered group standardized tests in accordance with the state testing program.
Teacher Assistant, Dr. Seuss Elementary School September 2009 – August 2010
 Tutored children individually or in small groups to reinforce learning concepts.
 Prepared lesson materials, bulletin board display, exhibits, equipment and demonstrations.
 Observed students' performance, and record relevant data to assess progress.
 Provided disabled students with assistive devices, supportive technology, and assistance accessing facilities.
ADDITIONAL EXPERIENCE
Cisco Systems Durham, NC
Human Resources, Talent Developer September 2002 – June 2009
 Created an organizational effectiveness program for Cisco’s Customer Advocacy Group, which improved
employee engagement by 13% in one quarter.
 Scaled internal counseling program to include executive coaching, group development sessions, one-on-one
career counseling, and self-service materials available to all employees.
TECHNICAL SKILLS/CERTIFICATIONS
Proficient in Microsoft Office Suite (Word, Excel, Access, PowerPoint, Outlook)
North Carolina Environmental Certification, May 2012''')

lyrics=('''12 drummers drumming
11 pipers piping
10 lords-a-leaping
9 ladies dancing
8 maids-a-milking
7 swans-a-swimming
6 geese-a-laying
5 golden rings
4 calling birds
3 French hens
2 turtle doves
and 1 partridge in a pear tree.''')

#Search resume for Regex
phoneRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo1=phoneRegex.search(resume)
print(mo1)

#Search resume for all Regex
phoneRegex2 = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo2=phoneRegex2.findall(resume)
print(mo2)

#Search resume for all Regex in groups
phoneRegex3 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)' )
mo3=phoneRegex3.findall(resume)
print(mo3)

#Search resume for all Regex in group of groups
phoneRegex4 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo4=phoneRegex4.findall(resume)
print(mo4)

#Search for count and nouns in lyrics
lyricsRegex = re.compile(r'(\d?\d)\s(\w+)')
mo5=lyricsRegex.findall(lyrics) 
print(mo5)
                         
