Rainfall_list=[]
month_list=['January','February','March','April','May','June','July','August','September','October','November','December']


# Read the rain fall data of every month into list
for i in range(12):
    Rainfall_list.append(int(input("Enter the rainfall for the month {0}".format(i+1))))

total_rainfall = sum(Rainfall_list)
# Total rainfall in the year
print("Total rainfall in the year : {0}".format(total_rainfall))

# Display average rainfall of the month
print("Average rainfall of the month : {0}".format(total_rainfall/12))

# get the minimum rainfall month index and print the value of the same index in month list for minimum rainfall month
print("The minimum rainfall month is : " + month_list[Rainfall_list.index(min(Rainfall_list))])


# get the maximum rainfall month index and print the value of the same index in month list for maximum rainfall month
print("The maximum rainfall month is : " + month_list[Rainfall_list.index(max(Rainfall_list))])



