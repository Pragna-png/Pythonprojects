# Student Management System

# 1. Variables and Datatypes
name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
college = input("Enter college name: ")

# 2. Strings and Text
print("\n----- STRING INFORMATION -----")

print("Student Name:", name)
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())

# 3. String Length
print("Name Length:", len(name))

# 4. String Indexing
print("First Character:", name[0])
print("Last Character:", name[-1])

# 5. String Slicing
print("First 3 Characters:", name[0:3])
print("Name in Reverse:", name[::-1])

# 6. Lists
subjects = ["Python", "Java", "SQL", "HTML"]

subjects.append("CSS")

print("\n----- SUBJECT DETAILS -----")
print("Subjects:", subjects)
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# 7. Tuples
personal_details = (name, age, course)

print("\n----- PERSONAL DETAILS -----")
print("Personal Details:", personal_details)

# 8. Dictionary
student = {
    "Name": name,
    "Age": age,
    "Course": course,
    "College": college,
    "Subjects": subjects
}

print("\n----- STUDENT DETAILS -----")

print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
print("College:", student["College"])

# 9. Sets
skills = {"Python", "SQL", "HTML", "Python", "Java"}

print("\n----- STUDENT SKILLS -----")
print("Skills:", skills)
print("Unique Skills Count:", len(skills))

# 10. Final Student Report
print("\n========== STUDENT REPORT ==========")

print("Student Name:", name.title())
print("Age:", age)
print("Course:", course.upper())
print("College:", college.title())

print("Subjects:", ", ".join(subjects))
print("Skills:", ", ".join(sorted(skills)))

print("====================================")
print("Student Report Generated Successfully!")
