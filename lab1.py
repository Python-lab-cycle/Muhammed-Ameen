def fileRead(fname):
    with open(fname,"r")as myfile:
        list1=myfile.readlines()
        print(list1)
fileRead('1text.txt')
