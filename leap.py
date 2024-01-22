cur=int(input("enter current year:"))
fut=int(input("enter future year:"))
for year in range(cur,fut+1):
    if((year%4==0)and(year%100!=0)or(year%400==0)):
        print(year)
        
