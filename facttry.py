num=int(input("enter a number:"))
fact=1
if(num==0):
    print("fact is",1)
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is:",fact)    
            
