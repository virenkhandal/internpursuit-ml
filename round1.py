import pandas as pd

def round1_filter(students, employer):
    employer_majors = employer['Majors/Minors'].values[0].split(';')
    filtered = students
    print(len(filtered.index))

    for index, row in students.iterrows():
        if isinstance(row[11], str):
            student_majors = row[11].split(',')
            bool = False
            for i in student_majors:
                if i in employer_majors:
                    bool = True
            if not bool:
                filtered = filtered.drop([index])
    print(len(filtered.index))

    employer_citizenship = employer['Citizenship'].values[0].split(';')
    for i in range(len(filtered.index)):
        row = filtered.iloc[[i]]
        student_citizenship = row['Citizenship'].values[0]
        if student_citizenship[0:3] == "Int":
            student_citizenship = "International Student"
        if student_citizenship not in employer_citizenship:
            filtered = filtered.drop([i])
    print(len(filtered.index))



    """
    Work hours filter
    # employer_hours = employer['Full Time or Part Time (Choose weekly hours)'].values[0].split(';')
    # for i in range(len(filtered.index)):
    #     row = filtered.iloc[[i]]
    #     student_hours = row['Full Time or Part Time Student'].values[0]
    #     if student_hours != employer_hours:
    #         filtered = filtered.drop([i])
    # print(len(filtered.index))
    """

    """
    Flexible Schedule filter
    # employer_flex = employer['Flex Schedule (check all that apply)'].values[0].split(';')
    # # print(employer_flex)
    # for i in range(len(filtered.index)):
    #     row = filtered.iloc[[i]]
    #     student_flex = row['Remote, Onsite, Flex Options - Check your preferences'].values[0].split(';')
    #     if len(student_flex) == 1 and student_flex[0] == "Flex Hours - adjust to student school & work schedule":
    #         if "Flex Hours - adjust to student school & work schedule" not in employer_flex:
    #             filtered = filtered.drop([i])
    """
    
    
    filtered.reset_index(inplace=True)
    print(len(filtered.index))
    return filtered