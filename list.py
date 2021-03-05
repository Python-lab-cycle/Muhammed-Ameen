list=[10,20,30,40,120]
result=[]
for i in list:
    if i > 100:
        result.append('over')
    else:
        result.append(i)
for i in result:
    print(i)
