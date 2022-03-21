
def population(num,per,value):
    for i in range(1,num+1):
        print("{0} \t\t\t\t\t {1}".format(i, value))
        value = value + (value / 100) * per


if __name__ == '__main__':
    max1 = int(input("Starting number of organisms: "))
    avg = int(input("Avegrage daily increase: "))
    days = int(input("Number of days to multiply: "))
    print("Day Approximate"+"     "+"Population")
    population(days,avg,max1)