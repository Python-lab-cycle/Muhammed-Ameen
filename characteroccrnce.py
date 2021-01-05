#store a list of names.Count the occurance of 'a' within the list
Astr=input("enter the string\n")
char=input("enter the character")
print("Given String:\n",Astr)
print("Given Character:\n",char)
res=0
for i in range(len(Astr)):
    if(Astr[i]==char):
        res=res+1
        print("Number of time character is present in string:\n",res)
