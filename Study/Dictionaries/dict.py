#Dictionary just like C# key value pair

student ={'name':'John','age':25,'courses':['Math','CompSci']}

print(student)

#If no key found by default gives exception
#ex - student['phone'] = ---> Error


print(student.get('phone','Not Found Key')) #2nd Param returns if no key found as message

student['phone'] = '76376623'
student['name'] = 'Jane' #Updated
print(student)


# To update multiple values
student.update({'name':'Jane_2','age':37})
print(student)


#Delete del keyword but better to use pop method
age = student.pop('age')
print(student)


#Get Keys
print('KEYS - ',student.keys())

#Values
print(f'Values - {student.values()}')


#Key - Values - Items Method
print(f'Items {student.items()}')


#Looping - Need to use Items because by default it will return keys only
for key,value in student.items():
    print(f'Key - {key}, Value- {value}')
