def sum1(li):
    res = 0
    global ind1
    global ind2
    li1=[]
    for i in range(0,len(li)):
        index=0
        for n in li:
            if n == 5:
                ind1 = index
            if n == 8:
                ind2 = index
            index+=1
        res = res+li[i]  
    for j in range(ind1,ind2+1):
        res = res-li[j]
    return res
def sum2(li):
    li1=[]
    for j in range(ind1,ind2+1):
        li1.append(li[j])
    return li1
str1=input("Enter string").split(',')
li=[]
for i in str1:
    li.append(int(i))
res = sum1(li)
res1 = sum2(li)
print(res)
str1="".join(str(i) for i in res1)
print(str1)
result=int(str1)+res
print("Sum of num1 and num2=",result)
