e,o,i=0,0,0
n=int(input("enter total no:"))
print("enter no in series:\n")
while i<n:
	if(int(input())%2==0):
		e+=1
	else:
		o+=1	
	i+=1
print("total no of even :",e,"\ntotal no of odd:",o)	