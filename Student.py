***Implement a function called sort_students that takes a list of student 
objects as input and sorts the list based on their
CGPA (Cumulative Grade Point Average) in descending order. 
Each student object has the following 
attributes: name (string), roll_number (string), and
cgpa (float). Test the function with 
different input lists of students.***

class student:
def__init__(self,name,roll_number,cgpa):
self.name=name
self.rollnumber=roll_number
self.cgpa=cgpa

def sort_students(studentlist)
     sorted_students=sorted(student-list,key lambda student:student.cgpa,reverse=True)
return sorted_students
 student=[
student("Suganthi",A234,8.5), student("Gayu",A214,9.2), 
student ("Manju",A243,7.8),student("Gobi",A253,8.6)
]
sorted_students=sort_students(student)
for(student in sorted_students)
print("Name:{},RollNumber:{},CGPA:{}",
       format(student.name, student.roll_number,student.cgpa)
