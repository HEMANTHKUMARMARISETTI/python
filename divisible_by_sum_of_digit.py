#lex_auth_0127136251125350401190

def divisible_by_sum(number):
    length=len(str(number))
    sum=0
    rem=0
    temp=number
    for i in range(length):
       rem=temp%10
       sum=sum+rem
       temp=temp//10
    if(number%sum==0):
       return True
    else:
       return False

    
number=42
print(divisible_by_sum(number))