class Student:
    def __init__(self, student_id, name, branch):
        self.student_id = student_id
        self.name = name
        self.branch = branch

    def to_string(self):
        return f"{self.student_id},{self.name},{self.branch}\n"


def load_students():
    students = []
    try:
        with open("data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    sid, name, branch = parts
                    students.append(Student(sid, name, branch))
    except FileNotFoundError:
        pass
    return students


def save_all_students(students):
    with open("data.txt", "w") as f:
        for student in students:
            f.write(student.to_string())