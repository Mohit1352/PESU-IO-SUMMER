#numeric check
s=input("Enter a string:")
l=len(s);flag=0
for i in range(0,l):
	if flag==0 and (ord(s[i])<ord("0") or ord(s[i])>ord("9")):
		flag=1;
if flag==1:
	print("Non Numeric")
else:
	print("Numeric")