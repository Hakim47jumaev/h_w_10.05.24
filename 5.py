def countt(itemm,list1):
    cnt=0
    for i in list1:
        if i==itemm:
            cnt+=1
    return cnt
list1=input().split()
for i in list1:
    if countt(i,list1)%2!=0:
        print(i)
