a='hemanth'
b='hemanth'

a1=list(a)
b1=list(b)
count=0
count1=0
if(len(a)!=len(b)):
    print("Insufficient characters")
elif(sorted(a)==sorted(b)):
    print("strings are anagram : ")
    for i in range(0,len(a1)):
       if(a1[i]==b1[i]):
          count=count+1
       else:
          count1=count1+1
    if count>0 :
       print('not full anagram due to word position is repeated')
    else:
       print('completed Anagram with out repeatation of positions')
elif(sorted(a)!=sorted(b)):
    print('not anagram')
else:
    print('false')
       
    
       
       
     
