# Grade Calculator Program

marks = []

# input marks for 5 subjects

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# display the marks

print("\nMarks in each subjects:") 
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")
    
#total and percentage calculation

total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print(f"\nTotal Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

# grade calculation

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A' 
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")

# pass or fail check (all subjects >= 40)

if all(mark >= 40 for mark in marks):
    print("Result: Pass")
else:
    print("Result: Fail")
