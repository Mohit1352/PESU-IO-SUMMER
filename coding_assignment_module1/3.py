#userinput list and element for binary search
l=input("Enter number list (comma separated, small to big)\n").split(",")
l=list(map(lambda x:int(x),l))
el=int(input("Enter search element :"))
beg=0;end=len(l);flag=0
while beg<=end and flag==0:
	mid=int((beg+end)/2);
	if(l[mid]==el):
		print("Found element at ",mid)
		flag=1
	elif l[mid]>el:
		end=mid-1
	else:
		beg=mid+1
if (flag==0):
	print("Element is not found in the list.")
	