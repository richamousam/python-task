n=int(input())
t=int(input())
chocolate=list(map(int,input.split()))
x={ }
for i in range(n-1):
    for j in range(i+1,n):
        if (chocolate[i]!=chocolate[j]) and (chocolate[i]+chocolate[j])==t:
            x.append([i+1,j+1])
print(x[0][0],x[0][1])
