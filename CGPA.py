"""
CGPA Calc:
    1. File
        1. Format:  Grade (In letters), Credit
        2. Read --> Object
        3. grade_dictionary = {"Grade" : Grade Point
                               ...}
    ...
    2. CGPA Calc
        2. Total Grade Points : Grade Point * Credit
        3. Total Credits
        4. calculateCGPA(total_grade_point, total_credit)
"""

class FileReader:

    def __init__(self, file_name):
        self.grade_dictionary = {
            "A": 4.00,
            "A-": 3.70,
            "B+": 3.30,
            "B": 3.00,
            "B-": 2.70,
            "C+": 2.30,
            "C": 2.00,
            "C-": 1.70,
            "D+": 1.30,
            "D": 1.00,
            "F": 0.00
        }
        self.file = open(file_name, "r")

    def file_read(self):
        grades_to_send = []
        grade_history = self.file.read()

        for i in range(0, len(grade_history), 5):
            temp = [self.grade_dictionary[grade_history[i]], float(grade_history[i + 3])]
            grades_to_send.append(temp)

        return grades_to_send

class CGPA:

    def __init__(self, grades):
        self.grades = grades

    def calcualte_cgpa(self):
        total_credit = 0
        total_grade_point = 0

        for i in self.grades:
            total_grade_point += i[0] * i[1]
            total_credit += i[1]

        cgpa = total_grade_point / total_credit

        return cgpa
