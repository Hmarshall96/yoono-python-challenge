The project is a simple student records management system. The system reads student data drom a JSON file and allows basic operations such as calculating average grades and filtering students based on their grades.

However, there are bugs in the existing implementation, and the system lacks critical features.

Tasks:
1. Fix the bugs in the existing implementation
2. Feature Addition:
    - Add a feature to calculate the average grade per class.  e.g. `records.calulate_average_grade_for_class("Science")`
    - Create a new JSON file `year-2021.json` with equivalent dummy data. Update the function which calculates the average grade per class to allow the class year to be passed in. e.g. `records.calulate_average_grade_for_class("Science", ["2020"])`
        - Multiple years should calculate the average across those years.
        - If no year(s) is passed in, default to all years.
    - Add a new student `Alice` in all years. Alter the application to account for this and ensure individuals are separated correctly.
