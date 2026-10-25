
def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

def check_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

name = input("Enter student name: ")
grade1 = float(input("Enter first term grade: "))
grade2 = float(input("Enter second term grade: "))
grade3 = float(input("Enter third term grade: "))

average = calculate_average(grade1, grade2, grade3)
status = check_status(average)

print("\nStudent Name:", name)
print("Average Grade:", round(average, 2))
print("Status:", status)
```
