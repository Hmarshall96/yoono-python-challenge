import json

class StudentRecords:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Load student data from a JSON file."""
        with open(self.file_path, "r") as f:
            self.data = json.load(f)

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


file_path = "data/year-2020.json"

records = StudentRecords(file_path)
records.load_data()

# print(records.calculate_average_grade_for_student("Alice"))
# print(records.calculate_average_grade_for_student("Bob"))
# print(records.calculate_average_grade_for_student("Henry"))

# print(records.filter_students_by_grade(90))

# print(records.calculate_average_grade_for_class("Science"))
# print(records.calculate_average_grade_for_class("Maths"))

# print(records.calculate_average_grade_for_class("Science", ["2020"]))
# print(records.calculate_average_grade_for_class("Maths", [])
