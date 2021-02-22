n=int(input())
arr=[]
dict={}
for i in range(n):
    arr.append(input())
counted=[]
for i in arr:
    if i not in counted:
        if i not in counted:
            counted.append(i)

            x=arr.count(i)
            print(i,len(i),x)
