#sum of digits of an integer
i=int(input("Enter a number: "))
d=0;sum=0;n=i;
while n!=0:
	d=n%10;
	sum=sum+d;
	n=n//10;
	if(d==i%10):
		print(d,sep="",end="");
	else:
		print(" + ",d,sep="",end="")
print(" = ",sum)