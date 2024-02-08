def mul (a,b):
    s = ''

    a = a.split()  # Splitting string a and assigning back to a
    b = b.split()  # Splitting string b and assigning back to b

    for p in range(len(a)):
        hk = (a[p]+' ') * int(b[p])
        s += hk  # Concatenating hk to s and assigning back to s

    ret = list(map(int,s.split()))

    return(ret)
  
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    a = sorted(list(map(int, input().split())),reverse=True)
    halo = sum(a)
    bond = input()
    slot = input()
    b = sorted(mul(bond,slot), reverse=  True)

    losses=0
    revenue=0
    for i in a:
        if i in b:
            b.remove(i)
            a.remove(i)
    if len(a) > len(b):
        for j in a[len(b):]:
            losses += j

        del a[len(b):]
    for i in a :

        l = i-(b[a.index(i)])


        losses += abs(l)
        revenue +=abs(i - abs(l))
    print(losses, revenue)