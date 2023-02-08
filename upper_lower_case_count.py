word=str(input('enter the string : '))
count=0
count1=0
new_list=[]
for i in word:
    if i.islower():
        count=count+1
    else:
        count1=count1+1

new_list.append(count) 
new_list.append(count1)
print(new_list)
        