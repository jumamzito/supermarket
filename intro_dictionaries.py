# '''
# dictionaries : {}
# set : ()

# tuples = : ()

# '''

# # names = ['A','B','C','B','D']

# # set_names = set(names)
# # print('A' in names)
# #set is a collection of unique items within a list


# # tuple()

# # # collection of items which is immutable

# # a=tuple((1,2,3,43))

# # print(type(a))


# # dict_results={
# #     'name':['john','jane','kelvin','Rachel'],
# #     'grade':[78,67,54,43]
# # }

# # print(dict_results['grade'])



# ##########Exercise 1: Dic,loops ,function
# names=[]
# scores=[]
# #Step1
# for x in range(1,1001):
#   names.append('student_' +str(x))

# #step2
# import random
# from unicodedata import name
# for i in range(1,1001):

#         n = random.randint(1,100)
#         scores.append(n)
#         #print(scores[:5])


# def grade_system(grade):
#     if grade >=80:
#         return 'A'
#     if 79>grade>=70:
#         return 'B'
    
#     if 69>grade>=60:

#         return 'C'
    
    
#     if 59>grade>=50:

#         return 'D'
    

#     if 49>grade>=40:
#         return 'E'
    
#     if 40>grade:
#         return 'F'

# #print(grade_system(56))


# grades=[]

# for x in scores:
#     student_grade=grade_system(x)
#     grades.append(student_grade)

# class_list=[]

# for x in names:
#     index_name=names.index(x)
#     info_dict={
#         'name':x,
#         'score':scores[index_name],
#         'grade':grades[index_name]
#     }
#     class_list.append(info_dict)

# # print(class_list[:3])

# def gender(score):
#     if score%2==0:
#         return 'male'

#     else:
#         return 'Female'
    
# for record in class_list:
#     record['Gender']=gender(record['score'])


# print(class_list[:3])


# #

# def class_results(class_list):



# #

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


'''