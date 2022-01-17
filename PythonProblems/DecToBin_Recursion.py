def dectobin(n):
    assert n >= 0, 'Say Big No to negative values'
    if n == 0:
        return 0
    else:
        m = n % 2
        return m + (10 * dectobin(int(n/2)))


print(dectobin(10))