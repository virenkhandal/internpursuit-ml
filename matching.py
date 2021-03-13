from main import cluster
import pandas as pd

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
        print(filtered_students)
        for index, student in filtered_students:
            
            print(student)


# def findOptimalStudent(employers, students):
#     for index, employer in employers.iterrows():
#         cluster = employer['Cluster #']
#         filtered_students = students[students['Cluster #'] == cluster]
#         print(filtered_students)
#         for index, student in filtered_students:
#             print(student)

# if __name__ == "__matching__":
#     findOptimalStudent(clusteredEmployers, clusteredStudents)