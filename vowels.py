data=str(input("enter the string"))
count=0
vowels="a,e,i,o,u,A,E,I,O,U"
for char in data:
    if char in vowels:
        count=count+1
print('There are  vowels in the string:'+str(count))


