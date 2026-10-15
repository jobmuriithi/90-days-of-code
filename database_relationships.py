#student_id    student_name      course_name
 #  1               Job           101        Cs
  # 2               Paul          101        CS
   #3               Freshier      102        IT
   #4               Jole          101        CS


#Primary Keys 

#student_id INTEGER PRIMARY KEY

#Foreign Keys
#course_id INTEGER, FOREIGN KEY (course_id) REFERENCES Courses(course_id)



#One to many relationships
 #One record in atable can be related to many records in another table

#Many to many realationships
 #Many records in one table can be related to many records in another table


#students
#   |
 #  |  one-to-many
  # |
   #|
#Enrollments
    #|
    #| many-to-many
    #|
    #|
#Units

#//CREATE TABLE units(
 #   unit_id INTEGER PRIMARY KEY,
#    unit_name TEXT NOT NULL,
#);

#//CREATE TABLE enrollments(
   # student_id  INTEGER NOT NULL,
    #unit_id INTEGER NOT NULL,

 #   P#RIMARY KEY(student_id,unit_id),
#)#

 #   FOREIGN KEY (student_id)
  #      REFERENCES

#students(Student_id),

    #FOREIGN KEY (unit_id)
 #       REFERENCES units(unit_id)

#)//




