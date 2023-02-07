sentence="Infosys Limited; Chenna 123"
sentence=sentence.replace(" ","")
sentence=sentence.replace(";","")
sentence=sentence.replace("-","")
count=0
count1=0
resultlist=[]
for i in sentence:
    if i.isdigit():
        count=count+1
    else:
        count1=count1+1
resultlist.append(count1)
resultlist.append(count)

print(resultlist)
