import json

# 读取 JSON 文件
with open('students.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

# 访问学生列表
students = data['students']

# 遍历学生列表并打印详细信息
for student in students:
	print(f"ID: {student['id']}")
	print(f"Name: {student['name']}")
	print(f"Age: {student['age']}")
	print(f"Grades: {student['grades']}")
	print()

# 计算每个学生的平均成绩
for student in students:
	grades = student['grades']
	average_grade = sum(grades.values()) / len(grades)
	print(f"Name: {student['name']}, Average Grade: {average_grade}")
	
