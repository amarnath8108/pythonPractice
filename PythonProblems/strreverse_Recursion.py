def strreve(str):
    if len(str) == 1:
        return str
    else:
        return strreve(str[1:])+str[0]


print(strreve("appmillers"))