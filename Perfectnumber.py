a=int(input('enter the number : '))
sum=0
rem=0
for i in range(1,a):
    rem=a%i
    if(rem==0):
        sum=sum+i
if(sum==a):
    print(a,'is a perfect number')
else:
    print(a,'is not a perfect number')
