print("---- Tuple Example ----")

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = (name, age, course)
print("Student Tuple:", student)

print("\n---- Set Example ----")

nums = input("Enter numbers separated by space: ").split()
numbers = set(map(int, nums))

print("Set (unique values):", numbers)

print("\n---- Dictionary Example ----")

student_dict = {
    "name": name,
    "age": age,
    "course": course
}

print("Student Dictionary:", student_dict)

print("\n---- Class Example ----")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person(name, age)
p1.display()

print("\n---- Inheritance Example ----")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

s1 = Student(name, age, course)
s1.display_student()
