n = int(input())
students = list()

for _ in range(n):
    students.append(input().split())

print(students)
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
