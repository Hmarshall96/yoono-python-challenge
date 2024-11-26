year_2020 = {
    "students": [
        {"name": "Alice", "grades": [85, 90, 78]},
        {"name": "Bob", "grades": []},
        {"name": "Charlie", "grades": [95, 100]}
    ]
}

class StudentRecords:
    def __init__(self, student_data):
        self.data = student_data

    def calculate_average_grade_for_student(self, name):
        """Calculate the average grade of a student."""
        for student in self.data["students"]:
            if student["name"] == name:
                return sum(student["grades"]) / len(student["grades"])
        return None

    def filter_students_by_grade(self, threshold):
        """Return students with an average grade above a threshold."""
        result = []
        for student in self.data["students"]:
            avg = sum(student["grades"]) / len(student["grades"])
            if avg > threshold:
                result.append(student["name"])
        return result


records = StudentRecords(year_2020)

# print(records.calculate_average_grade_for_student("Alice"))
# print(records.calculate_average_grade_for_student("Bob"))
# print(records.calculate_average_grade_for_student("Henry"))

# print(records.filter_students_by_grade(90))

# print(records.calculate_average_grade_for_class("Science"))
# print(records.calculate_average_grade_for_class("Maths"))

# print(records.calculate_average_grade_for_class("Science", ["2020"]))
# print(records.calculate_average_grade_for_class("Maths", [])
