nums = [1,2,3,4,5]
for num in nums:
    if num==3:
        print('Found!')
        continue  #o/p - 1,2,FOUND,4,5 break - > 1,2,FOUND
    print(num)


for num in nums:
    for letter in 'abc':
        print(num,letter)



x=0
while x<10:
    print('While loop',x)
    if x==5:
        print('Found 5 !')
        break
    x+=1

