def GCD(n,m,a,b,result):
    assert n >= 1, 'say no to negative values'
    if m == n:
        return result
    else:
        if a % m == 0 and b % m == 0 and m > result:
            result = m
        return GCD(n,m+1,a,b,result)


def min1(a,b):
    result =0
    n = min(a,b)
    print(GCD(n,1,a,b,result))


min1(8,12)