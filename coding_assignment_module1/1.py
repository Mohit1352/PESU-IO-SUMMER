#Comma separated numbers to tuple and list

a=input("Enter Comma Separated numbers:\n").split(",")
b=list(map((lambda x:int(x)),a))
print(b)
c=tuple(b)
print(c)