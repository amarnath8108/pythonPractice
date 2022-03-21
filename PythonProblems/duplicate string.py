input1 = input()
result = []
result1 =''
for i in input1:
    if i not in result:
        result.append(i)
        result1=result1+i
print(result1)
