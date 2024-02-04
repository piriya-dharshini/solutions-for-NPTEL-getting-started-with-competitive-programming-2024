t=int(input())

for testcase in range(t):
    n=int(input())
    k=int(input())
    arr=list(map(int,input().split()))
    found = False
    l=[]
    for i in range(n - 1):
 
        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s and sorted([x, arr[i], arr[j]]) not in l :
                
                l.append(sorted([x, arr[i], arr[j]]))
                found = True
            else:
                s.add(arr[j])
    if found == False:
        print("No Triplet Found")
    print(l)