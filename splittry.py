string=input("enter the line of text:")
words=string.split()
for i in words:
    if(words[i]==words[i+1]):
        count=count+1
    else:
        count=0
print(count)
        
