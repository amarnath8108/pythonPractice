# Read values from the file by splitting each line
file_open = list(open('C:/Users/AmarnathMaddala/Downloads/sample1.txt').read())

# list to store occurred values
list_to_store_occurred_values = []

# for loop to get count of values
for i in file_open:
    # use upper letters and lower case letters to get the count
    a=i.capitalize()
    b=i.lower()

    # ignore special characters by verifying with ascii values
    if 65 <= ord(a) <= 90 and a not in list_to_store_occurred_values:

        # add values to list if it occurred
        list_to_store_occurred_values.append(a)

        # count occurrence of upper and lower case letters and add them
        result = file_open.count(a) + file_open.count(b)

        # print total value
        print("{0} : {1}".format(a, result))
