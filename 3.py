def end_corona(a,b,c):
    k=a-b
    cnt=0
    for i in range(0,c,k):
        cnt+=1
    return cnt
a=int(input())
b=int(input())
c=int(input())
print(end_corona(a,b,c))