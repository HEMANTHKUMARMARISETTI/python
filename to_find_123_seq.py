#lex_auth_0127135869481369601150

def list123(nums):
    #start writing your code here
    newstr=""
    for i in range(len(nums)):
       newstr=newstr+str(nums[i])
    if '123' in newstr:
       return True
    else:
       return False
    

nums=[1,2,3,4,5]
print(list123(nums))