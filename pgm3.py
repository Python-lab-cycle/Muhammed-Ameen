file=input("enter file name")
file1=open(file,"r")
line=file1.read()
print("Line",line)
file1.close()