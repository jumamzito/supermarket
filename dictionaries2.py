'''
a) Create a list of 100 students whose records will be stored in this format:

{
    'name': 'Alice',
    'homework':[100.0,92.0,98.0,100.0],
    'quizzes':'[82.0,83.0,91.0],
    'tests':[89.0,97.0]
}
NOTE:
the numbers should be randomly generated btn 30 and 95
the student names should all be unique

b) Create 2 functions that can return
The student with highest grade given either the arguement of homework, quizes, test
(Output: STudent Name - Marks)

c) Average score of the top n students given the of homework, quizes, test
(Output: [Student name - Average, ...])


# '''

# name= []

# for x in range(1,101):
#     name.append('Student_'+str(x))

# #print(student_name[:5])    

import random
# homework=[]

# for x in range(1,101):
#     homework.append(round(random.uniform(30,95), 1))

# # print(homework)

# quizez=[]

# for x in range(1,101):
#     quizez.append(round(random.uniform(30,95), 1))

# tests=[]

# for x in range(1,101):
#     tests.append(round(random.uniform(30,95), 1))

def random_marks(n):
    store =[]
    for x in range(1,n+1):
        store.append(round(random.uniform(30,95), 1))

    return store

students_list=[]

for x in range(1,101):
    students_list.append(
        {
        'name':'Student {}'.format(x),
        'homework':random_marks(4),
        'quizzes':random_marks(3),
        'tests':random_marks(2)
    }

    )

print(students_list[:4])

# def grade_calc(n):
#     highest_score = max(n.iterkeys(), key=(lambda key: n[key]))

#     return highest_score


def grade_calc(marks):
    average = {}
    for key, value in marks.items():
        average[key] = sum(value) / len(value)
    return average

grade_calc(students_list)

def cal_avg(items):
    return sum(items)/len(items)


students_list_avg= students_list

for x 

# {
#     'name': 'Alice',
#     'homework':[100.0,92.0,98.0,100.0],
#     'quizzes':'[82.0,83.0,91.0],
#     'tests':[89.0,97.0]
# }

# def random_marks(n):
#     store =[]
#     for x in range(1,n+1):
#         store.append(round(random.uniform(30,95), 1))

#     return store

#list comprehension

#print([round(random.uniform(30,95), 1) for n in range(0,4)])



# print(students_list[:5])