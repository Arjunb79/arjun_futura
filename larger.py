first_string = input("Enter the first string : ")
second_string = input("Enter the second string : ")
l1=0
l2=0
for i in first_string:
    l1=l1+1
for i in  second_string:
    l2=l2+2
if l1>l2:
    print("first string is larger tha second string")
else:
    print("second string is larger than first string")