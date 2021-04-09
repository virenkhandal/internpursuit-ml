from os import major
import pandas as pd

def round1_filter(students, employer):
    employer_majors = employer['Majors/Minors'].values[0].split(';')
    filtered = students
    drop = set()

    """
    Majors/Minors filter
    """
    for index in range(len(filtered.index)):
        row = filtered.iloc[[index]]
        if isinstance(row['Majors/Minors'].values[0], str):
            student_majors = row['Majors/Minors'].values[0].split(';')
            bool = False
            for i in student_majors:
                if i in employer_majors:
                    bool = True
                    break
            if set(student_majors).isdisjoint(set(employer_majors)):
                drop.add(index)

    """
    Citizenship filter
    """
    employer_citizenship = employer['Citizenship'].values[0].split(';')
    for index in range(len(filtered.index)):
        row = filtered.iloc[[index]]
        student_citizenship = row['Citizenship'].values[0]
        if student_citizenship[0:3] == "Int":
            student_citizenship = "International Student"
        if student_citizenship not in employer_citizenship:
            drop.add(index)

    """
    Work hours filter
    """
    employer_hours = employer['Full Time or Part Time (Choose weekly hours)'].values[0].split(';')
    for index in range(len(filtered.index)):
        row = filtered.iloc[[index]]
        student_hours = row['Full Time or Part Time Student'].values[0]
        if student_hours == "Part Time Student (3-11 hours)":
            student_hours = "Part time (3-11 hours)"
        if student_hours == "Full Time Student (12+ hours)":
            student_hours = "Full time (12 + hours)"
        if student_hours not in employer_hours:
            drop.add(index)

    """
    Flexible schedule filter
    """
    employer_flex = employer['Flex Schedule (check all that apply)'].values[0].split(';')
    for index in range(len(filtered.index)):
        row = filtered.iloc[[index]]
        student_flex = row['Remote, Onsite, Flex Options - Check your preferences'].values[0].split(';')
        if len(student_flex) == 1 and student_flex[0] == "Flex Hours - adjust to student school & work schedule":
            if "Flex Hours - adjust to student school & work schedule" not in employer_flex:
                drop.add(index)
    
    """
    Work location filter
    """

    """
    School credit filter
    """

    """
    Academic calendar filter
    """
    filtered = filtered.drop(list(drop))
    filtered.reset_index(inplace=True)
    return filtered