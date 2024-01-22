string=input("enter the string:")
x=string[0]
string=string.replace(x,'$')
print(x+string[1:])
