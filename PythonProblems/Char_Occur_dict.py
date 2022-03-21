# Read characters from file
list_of_values_in_file = list(open('C:/Users/AmarnathMaddala/Downloads/sample1.txt').read())
# Dictionary to store values and there count
values_dict = {}
# Empty list to store occurred values
list_of_values_occurred = []
# loop to verify the count
for i in list_of_values_in_file:
    # change character to Upper and lower case
    cap = i.capitalize()
    low = i.lower()

    # condition to ignore characters other than letters
    if 65 <= ord(cap) <= 90 and cap not in list_of_values_occurred:
        # add character to list if letter is checked
        list_of_values_occurred.append(cap)

        # add all lower and upper case characters in list
        result = list_of_values_in_file.count(cap) + list_of_values_in_file.count(low)

        # add values to dictionary
        values_dict[cap] = result

print(values_dict)