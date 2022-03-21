def rangesum(n):
    assert n>0, 'Say Big no to negative values'
    if n == 1:
        return 1
    else:
        return n+rangesum(n-1)


print(rangesum(-10))