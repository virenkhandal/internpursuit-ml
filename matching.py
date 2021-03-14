from main import cluster
import pandas as pd
import numpy as np
import scipy
from scipy.spatial import distance

employers = pd.read_csv('fakeEmployer.csv')

# print(employers.keys())
# print(employer['Company Name'])
clusteredEmployers = cluster('fakeEmployer.csv', 2)

clusteredStudents = cluster('fakeStudent.csv', 2)
# print(clusteredEmployers)
# print(clusteredStudents)

for index, employer in clusteredEmployers.iterrows():
    cluster = employer['Cluster #']
    filtered_students = clusteredStudents[clusteredStudents['Cluster #'] == cluster]
    # print("filtered students: ")
    # print(filtered_students)
    best_student = ""
    lowest_dist = 100000
    for index, student in filtered_students.iterrows():
        arr = employer.values.tolist()
        student_arr = student.values.tolist()
        employer_values = arr[1:]
        student_values = student_arr[1:]
        # print(employer_values)
        # print(student_values)
        distance = scipy.spatial.distance.euclidean(employer_values, student_values)
        if distance < lowest_dist:
            lowest_dist= distance
            best_student = student_arr[0]
    # print(best_student, lowest_dist)
    print("The best student for " + employer['Company Name'] + " is " + best_student + ". This student has a " + str(round(100 - lowest_dist, 1)) + "% similarity to the company's preferences.")


# def findOptimalStudent(employers, students):
#     for index, employer in employers.iterrows():
#         cluster = employer['Cluster #']
#         filtered_students = students[students['Cluster #'] == cluster]
#         print(filtered_students)
#         for index, student in filtered_students:
#             print(student)

# if __name__ == "__matching__":
#     findOptimalStudent(clusteredEmployers, clusteredStudents)