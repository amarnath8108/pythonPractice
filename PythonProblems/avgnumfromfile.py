

temp = open('C:/Users/AmarnathMaddala/Desktop/numbers.txt').read().splitlines()
result =0
for i in temp:
    result = result + int(i)
print(result/len(temp))
