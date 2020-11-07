def change_sring(str):
    return str[-1:] + str[1:-1] + str[:1]
str=str(input("enter the string"))
print(change_sring(str))