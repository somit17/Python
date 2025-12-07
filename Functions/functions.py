from Lists.lists import courses


def hello_func():
    return 'Hello Function !'



def hello_greeting(greeting,name = 'You'): #Default value
    return f'Hi {greeting} {name}!'

#pass keyword to keep function empty
print(hello_func) #Returns address <function hello_func at 0x1059793a0>
print(hello_func().upper())

print(hello_greeting('Function','Test'))
print(hello_greeting('Function_2'))




def student_info(*args,**kwargs): #Argument(Tuple) and Keyword-Arguments(Dictionary)
    print(args)
    print(kwargs)


course= ['Math','Art']
info = {'name':'A','age':15}
print(student_info(course,info))

#output  --Unpacks differently
#(['Math', 'Art'], {'name': 'A', 'age': 15})
#{}


print(student_info(*course,**info))

#Output  Unpacks proper arguments and keyword arguments
#('Math', 'Art')
#{'name': 'A', 'age': 15}