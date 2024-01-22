word=input("enter a word:")
vowels=['i','o','u','a','e']
list=[]
for i in word:
    if(i in vowels and i not in list):
        list.append(i)
print("vowels in the word are:",list)
