course = 'Python for Beginners'

print("In Upper case : ", course.upper())
print("Course Name : ", course)

print("In lower case : ", course.lower())

print("Capitalize : ", course.capitalize())

print("Title : ", course.title())

print(course.find('for'))

print(course.replace('for', '4'))

print('Python' in course)

print('Python' in course)

course = "Python's course for Beginners"
print(course)

course = 'Python for "Beginners"'
print(course)

# Multiline Strings :

print("\nMultiline Strings :\n")
course = """Python for Beginners
Python for Intermediate
Python for Advanced"""

print(course)

course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:5])

name = "Anand"
print(name[1:-1])

# FORMATTED STRINGS

print("\nFORMATTED STRINGS :\n")

course = "Python for Beginners"
print(f"Course Name : {course[0:11]} [{course[11:]}]")

first = "Purushottam"
last = "Anand"
msg = f'{first} [{last}] is a Programmer'
print(msg)
