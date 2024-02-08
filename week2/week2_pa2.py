t = int(input())

def findClosest(bonds, n, target, slots):
    arr = sorted(bonds)
    left, right = 0, n - 1
    while left < right:
        if abs(arr[left] - target) <= abs(arr[right] - target):
            right -= 1
        else:
            left += 1           
    m = arr[left]
    if target < arr[left]:
        loss = arr[left] - target
        m = target
    else:
        loss = target - arr[left]
    ind = bonds.index(arr[left])
    slots[ind] -= 1
    return m, loss

for i in range(t):
    x, y = map(int, input().split())
    clients = list(map(int, input().split()))
    bonds = list(map(int, input().split()))
    slots = list(map(int, input().split()))
    allocatedval = []
    losses = []
    for j in clients:
        try:
            ind = slots.index(0)
            bonds.pop(ind)
            slots.remove(0)
        except ValueError:
            pass
        m, o = findClosest(bonds, len(bonds), j, slots)
        allocatedval.append(m)
        losses.append(o)

    print(sum(allocatedval), sum(losses))
