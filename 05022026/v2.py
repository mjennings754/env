class Student:
    count = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f"The # of students {Student.count}"
    
Harry = Student("Harry", "3.9")

print(Student.get_count())