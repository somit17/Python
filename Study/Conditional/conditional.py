# False Values:
    # False
    # None
    # Zero of any numeric type 0 = false
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')




if True:
    print('Conditional was true')

if False:
    print('Conditional was true')

#Using var
lang = 'C#'
if lang=='Python':
    print('Language is Python')
else:
    print('No match')



# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'C#'
if language == 'Python':
    print('Language is Python')
elif language == 'C#':
    print('Language is c#')
else:
    print('No match')

#Python does not have switch case because of elif




#and
#or
#not
user = 'Admin'
logged_In = False
if user == 'Admin' and logged_In:
    print('Admin Page')
else:
    print('Bad Creds')


if not logged_In:
    print('Please Log In')
else:
    print('Welcome')


# Object Identity:  is
a =[1,2,3]
b=[1,2,3]
print(a==b)
print(f'Memory of A   = {id(a)}')
print(f'Memory of B   = {id(b)}')
print(a is b) #False - > Different memory location checks same objects are same or not


c =[1,2,3]
d=c
print(f'Memory of C   = {id(c)}')
print(f'Memory of D  = {id(d)}')
print(c is d)




