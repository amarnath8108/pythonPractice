def palin(str):
    if len(str) == 1:
        return str
    else:
        return palin(str[1:])+str[0]


str="madam"
print(str == palin("mada"))