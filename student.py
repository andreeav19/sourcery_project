class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is between 0 and 100

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 <= new_grade and new_grade <= 100:
            self.grade = new_grade
        else:
            print("Invalid grade. It should be between 0 and 100.")

    def is_passing(self):
        if (self.grade >= 60):
            return True
        else:
            return False


    def __str__(self):
        return "Student " + self.name + ", Age: " + str(self.age) + ", Grade: " + str(self.grade)


student1 = Student("Alice", 20, 85)
print(student1)               # Output: Student Alice, Age: 20, Grade: 85
print(student1.is_passing())  # Output: True
student1.set_grade(95)
print(student1.get_grade())   # Output: 95
