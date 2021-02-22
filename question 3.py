inp=int(input())
arr1=list(map(int,input().spilt()))
arr2=list(map(int,input().spilt()))
alice=bob=0
for i in range(inp):
    if arr1[i] >arr2[i]:
        alice+=1
    elif arr1[i]==arr2[i]:
        pass
    else:
        bob+=1
print("alice "+str(alice))
print("bob "+str(bob))
if alice>bob:
    print("alice won the competation")
else:
    print("bob won the competition")
