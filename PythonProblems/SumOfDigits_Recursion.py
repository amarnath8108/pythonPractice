def sum_of_digits(n):
    assert n >= 0, 'Say no to negative values'
    if n == 0:
        return 0
    else:
        m = int(n % 10)
        return m + sum_of_digits(int(n / 10))


print(sum_of_digits(1114))
