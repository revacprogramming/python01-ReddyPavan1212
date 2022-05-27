# Lists

#filename = "dataset/romeo.txt"
filename=input("enter the file name")
a=[]
count=0
try:
    fhandle=open(filename,"r")
except:
    print("error")
for line in fhandle:
    if line.startswith('From '):
        b=line.split()
        print(b[1])  
        count=count+1
print("There were",count,"lines in the file with From as the first word")