import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_distances, cosine_similarity
from termcolor import colored


def round1_match(students, employer):
    filtered = students
    drop = set()
    employer_majors = employer['Majors/Minors'].values[0].split(', ')
    employer_citizenship = employer['Citizenship'].values[0].split(',')
    employer_hours = employer['Full Time or Part Time (Choose weekly hours)'].values[0].split(',')
    employer_flex = employer['Flex Schedule (check all that apply)'].values[0].split(',')
    employer_cred = employer['Credit or Non-Credit '].values[0].split(',')
    employer_cal = employer['Which semester are you seeking interns working with you'].values[0].split(',')
    employer_cal = [x.lower() for x in employer_cal]
    employer_details = [1, 1, 1, 1, 1, 1]
    scores = []
    for index in range(len(filtered.index)):
        # print(index)
        row = filtered.iloc[[index]]

        """
        Majors/Minors matching
        """
        major_score = 0
        # print(row.keys())
        majors = row['Your Major '].values[0]
        minors = row['Your Minor (if applicable)'].values[0]
        print(row['Name'].values[0], " : ", majors)
        # if row['Name'].values[0] == 'dorsi.jesse@gmail.com':
            # print(type(majors))
        if not isinstance(majors, str):
            # print(row["Name"].values[0])
            print(colored("nan", "red"))
            drop.add(index)
        else:
            # print(employer_majors)
        # print(minors)
            majors = majors.split(", ")
            minors = minors.split(", ")
            if len(minors) == 0:
                student_majors = majors
            else:
                student_majors = majors.append(minors)
            print("student_majors: ", student_majors)
            inside = False
            for i in student_majors:
                print("i: ", i, " , ", i in employer_majors)
                if i in employer_majors:
                    student_majors = 1
                    inside = True
                    print(colored("match", "green"))
                    break
            if not inside:
                drop.add(index)
                print(colored("no match", "red"))
                student_majors = 0
        # student_set = set(student_majors)
        # if not student_set.isdisjoint(set(employer_majors)):
        #     major_score = 1
        # else:
        #     major_score = 0
            # print(student_majors)
            # print(employer_majors)
        """
        Citizenship matching
        """
        student_citizenship = row['Citizenship'].values[0]
        # print(employer_citizenship)
        # print(student_citizenship)
        if student_citizenship[0:3] == "Int":
            student_citizenship = "International Student"
        if student_citizenship in employer_citizenship:
            student_citizenship = 1
        else:
            student_citizenship = 0

        """
        Working hours matching
        """
        student_hours = row['Full Time or Part Time Student'].values[0]
        # print(employer_hours)
        if student_hours == "Part Time Student (3-11 hours)":
            student_hours = "Part time (3-11 hours)"
        if student_hours == "Full Time Student (12+ hours)":
            student_hours = "Full time (12 + hours)"
        # student_hours = 0
        # print(student_hours)

        if student_hours in employer_hours:
            student_hours = 1
        else:
            student_hours = 0

        """
        Flexibility matching
        """
        student_flex = row['Remote, Onsite, Flex Options - Check your preferences'].values[0].split(',')
        # print(employer_flex)
        # print(student_flex)
        inside = False
        for i in student_flex:
            if i in employer_flex:
                student_flex = 1
                inside = True
                break
        if not inside:
            student_flex = 0
        
        """
        Academic credit matching
        """
        s = 'Credit or Noncredit Internship (Requires a full semester commitment)'
        if str(row[s].values[0]) == 'nan':
            row[s].values[0] = 'Non-Credit - Think of this like a volunteer role'
        cred_score = 0
        student_cred = row['Credit or Noncredit Internship (Requires a full semester commitment)'].values[0].split(';')
        # print(employer_cred)
        # print(student_cred)
        if student_cred[0] in employer_cred:
            cred_score = 1


        """
        Academic calendar matching
        """
        student_cal = row['Which semester are you seeking an internship?'].values[0].split(',')
        student_set = set(student_cal)
        # print(employer_cal)
        # print(student_cal)
        if 'Flexible' in student_cal:
            student_cal = 1
        else:
            inside = False
            for i in student_cal:
                if i in employer_cal:
                    student_cal = 1
                    inside = True
                    break
            if not inside:
                student_cal = 0
        # if not student_set.isdisjoint(set(employer_cal)):
        #     student_cal = 1
        # else:
        #     student_cal = 0


        details = [student_majors, student_citizenship, student_hours, student_flex, cred_score, student_cal]
        details = np.array(details)
        employer_details = np.array(employer_details)
        # print("employer details: ", employer_details)
        # if row['Name'].values[0] == 'sngraciak7@gmail.com':
        #     print("student details: ", details)
        score = np.dot(employer_details, details)
        # print(score)
        scores.append(score)
        if score == 0:
            drop.add(index)
    # print(scores)
    m = pd.Series(scores)
    filtered.insert(len(filtered.columns), "Scores", m)
    # print(filtered['Scores'])
    # filtered = filtered[filtered['Scores'] != np.nan]
    # filtered.reset_index(inplace=True)
    filtered = filtered.drop(list(drop))
    filtered.reset_index(inplace=True)
    return filtered