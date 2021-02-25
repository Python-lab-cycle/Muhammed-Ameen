line="najukka muthmani a funny boi"
file=input("Enter file name")
f1=open(file,"w")
f1.write(line)
f1.close()
f1=open(file,"r")
f1.read()
print(line)
f1.close()
