# Student Result Processing System

print("=====Student Result Processing System=====")


# Taking student details
student_name=input("Enter student name: ")
roll_number=input("Enter roll number: ")


python_marks=float(input("Enter marks in Python: "))
maths_marks=float(input("Enter marks in Mathematics: "))
english_marks=float(input("Enter marks in English: "))

# Calculating total marks and percentage
total_marks=python_marks + maths_marks + english_marks
maximum_marks=300
percentage=(total_marks/maximum_marks)*100


if percentage>=40:
    result_status="Pass"
else:
    result_status="Fail"

# Printing the final result
print("\n========== Student Result ==========")
print("Student Name :",student_name)
print("Roll Number  :",roll_number)
print("Python Marks :",python_marks)
print("Maths Marks  :",maths_marks)
print("English Marks:",english_marks)
print("------------------------------------")
print("Total Marks  :",total_marks)
print("Percentage   :",percentage)
print("Result Status:",result_status)
print("====================================")
