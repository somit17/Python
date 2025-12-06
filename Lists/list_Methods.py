courses  = ['History', 'Math', 'Physics', 'CompSci']


#Append
courses.append('Art_3')


#insert specific position
courses.insert(0,'Art')
print(courses)


#Add multiple values  list1 to list2 --Extend Method
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = ['Edu','AI']
list_1.extend(list_2)
print(list_1)


#Remove value
popped = courses.pop() #By default removes last value'
print(popped)
print(courses)



#Reverse
courses.reverse()
print(courses)

#sorting
nums = [1,5,4,6]
nums.sort()
print(nums)


#Sorting in reverse
nums.sort(reverse=True)
print(nums)

#Sorted function - returns sorted list
courses_2 = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses_2)
print(sorted_courses)


#Min and Max value from List
nums_2 = [1,5,4,6]
print(f'Minimum - {min(nums_2)}')
print(f'Maximum - {max(nums_2)}')

#Sum
print(f'Total - {sum(nums_2)}')


#Index
print(f'Index - {courses_2[2]}')

#In Operator
print(f"{'Math' in courses_2}")


for course in courses_2:
    print(course)

#Returns index and assigns index value if used start
for index,course in enumerate(courses_2,start=1):
    print(index,course)



#Join Method
courses_str = '-'.join(courses_2)
print(courses_str)









