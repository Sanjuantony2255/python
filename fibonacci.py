num=int(input("enter range:"))
f0=0
f1=1
if(num==0):
    print("no sequence")
elif(num==1):
    print(f0)
else:
    print(f0)
    print(f1)
    for i in range(1,num-1):
        f=f0+f1
        f0=f1
        f1=f
        print(f)
