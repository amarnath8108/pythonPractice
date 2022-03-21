def Tax(amount):
    tip = (amount/100)*18
    sales_tax = (amount/100)*7
    total = amount+tip+sales_tax
    print("Meal cost : {0}".format(amount))
    print("Tip added : {0}".format(tip))
    print("Tax added : {0}".format(round(sales_tax,2)))
    print("Total cost : {0}".format(total))

if __name__ == '__main__':
    cost = int(input("Total purchase cost : "))
    Tax(cost)
