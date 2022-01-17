def fibonacci(max1):
    assert max1 >= 0, 'Say no to negative values'
    if max1 in [0, 1]:
        return max1
    else:
        return fibonacci(max1 - 1) + fibonacci(max1 - 2)


print(fibonacci(3))
