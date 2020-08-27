'''
zoradovanie pomocou rekurzie, skusim si debugnut
'''

def merge(lst0, lst1):
    '''spojenie dvoch listov'''
    ret = []
    while lst0 and lst1:
        if lst0[0] <= lst1[0]:
            ret.append(lst0.pop(0))
        else:
            ret.append(lst1.pop(0))
    ret.extend(lst0)
    ret.extend(lst1)
    return ret


def mergesort(lst):
    '''samotne rozdelovanie'''

    if len(lst) <= 1:
        return lst
    r = lst[len(lst) // 2]
    left, mid, right = [], [], []
    for i in lst:
        if i < r:
            left.append(i)
        elif i == r:
            mid.append(i)
        else:
            right.append(i)
    left = mergesort(left)
    left.extend(mid)
    right = mergesort(right)
    ret = merge(left, right)
    return ret


# neviem co sa mu nezda na printe, tak som ho zmazal


print(mergesort([1, 7, 3, 200, 3000, 290, 40, 30, 2200]))
print('skvele \n')
