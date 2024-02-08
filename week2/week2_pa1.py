#using binary search on a 2d sorted array

t=int(input())
for i in range(t):
    n,m,j=list(map(int,input().split()))
    arr=[]
    for m in range(n):
        subarr=list(map(int,input().split()))
        arr.append(subarr)
    
    found=False
    for x in range(len(arr)):
        try:
            y=arr[x].index(j)
            print(x,y)
            found=True
            break
        except ValueError:
            continue
    if found==False:
        print(-1,-1)    