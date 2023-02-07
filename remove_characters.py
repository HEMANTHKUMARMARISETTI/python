string=str(input("enter the string : "))
print("entered string is ---->",string)
letter=str(input("enter the letter to be removed : "))
print("the letter to be removed is ",letter,"from string",string)
newstr=""
for i in range(0,len(string)):
    if string[i]!=letter:
        newstr=newstr+string[i]
    else:
        continue
print("after removal of ",letter," in ",string," is ----->",newstr)    
