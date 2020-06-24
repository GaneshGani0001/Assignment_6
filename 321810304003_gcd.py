i,a,b=1,int(input("enter 2 no:")),int(input())
if a>b:
 a,b=b,a
while(i<=b):
 if(a%i==0 and b%i==0):
  gcd=i
 i+=1
print("gcd:",gcd)