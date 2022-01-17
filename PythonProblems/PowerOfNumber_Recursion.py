def Powerofnumber(n, m):
    assert n >= 0 and m >= 0, 'say no to negative values'
    if m == 1:
        return n
    elif m == 0:
        return 1
    else:
        return n * Powerofnumber(n,m-1)


print(Powerofnumber(2, 1))
