from CGPA import FileReader
from CGPA import CGPA

file_reader = FileReader("grade_history.txt")
cgpa_calculate = CGPA(file_reader.file_read())
print("CGPA: " + str(round(cgpa_calculate.calcualte_cgpa(), 2)))