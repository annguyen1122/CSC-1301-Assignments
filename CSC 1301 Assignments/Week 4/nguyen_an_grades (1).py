
#Stores grades
examGrades = {83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 81}
#Stores students attended on days one and two
dayOneStudents = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica", "Trent", "Mahmoud"}
dayTwoStudents = {"Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"}

#Calculates the average grade 
averageGrade = (sum(examGrades) / len(examGrades))

#Combines both sets
bothStudents = dayOneStudents.union(dayTwoStudents)
#Combines both sets and finds the duplicates
bothAttendedStudents = dayOneStudents.intersection(dayTwoStudents)
#Finds the difference between all students and students that attended both classes
attendedOneClassStudents = bothStudents.difference(bothAttendedStudents)

#prints out the number of students that took the exam
print(f"{len(examGrades)} Students took the exam")
#prints the highest grade
print(f"The highest grade was a {max(examGrades)}")
#prints the lowest grade
print(f"The lowest grade was a {min(examGrades)}")
#prints the average grade calculated on line 9, and reports any floating-point values to 1 decimal place
print(f"The average grade for the exam was a {averageGrade:.1f}")

#prints the total unique students that attended class on day one and two
print(f"{len(bothStudents)} students attended the class")
#prints the students that attended both days
print(bothAttendedStudents, "attended both class days.")
#prints the students that attended one class day
print(attendedOneClassStudents, "attended one class day.")