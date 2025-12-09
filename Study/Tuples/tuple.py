course_1  = ('History', 'Math', 'Physics', 'CompSci')
course_2 = course_1
print(f'Course_1 : - {course_1}')
print(f'Course_2 : - {course_2}')

course_1[0]='ART'
print(f'It will give error since it is immutable assignment cannot be done{course_1}')