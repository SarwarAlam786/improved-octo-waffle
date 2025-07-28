#Task 1: Create a Dictionary of Student Marks
'''
student_marks = {
    "Sarwar": 97,
    "Firoz": 95,
    "Farida": 90,
    "Parbin": 85,
    "Sunana": 82
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(name,'s marks: ',student_marks[name])
else:
    print("Student not found")
'''

#Task 2: Demonstrate List Slicing
'''
List=[1,2,3,4,5,6,7,8,9,10]
print("Original list:",(List))
print("Extracted first five elements:",List[0:5])
List1=List[0:5]
List1.reverse()
print("Reversed extracted elements",List1)
'''