def feet_to_inches():
    #get no of feets from user
    feet_value = int(input("No. of feets : "))

    #Convert feet to inches
    #one feet equals to 12 inches
    inches = feet_value * 12

    print("Total inches of the given feet value : {0}".format(inches))


feet_to_inches()