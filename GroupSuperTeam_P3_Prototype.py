name = input("Enter student name: ")
grade1 = float(input("Enter first term grade: "))
grade2 = float(input("Enter second term grade: "))
grade3 = float(input("Enter third term grade: "))

average = (grade1 + grade2 + grade3) / 3

print("\nStudent Name:", name)
print("Average Grade:", average)

if average >= 75:
    print("Status: PASSED")
else:
    print("Status: FAILED")
