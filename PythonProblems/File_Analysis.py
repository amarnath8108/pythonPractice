# read the values from file1 and store into list and change all values to upper case
File_1 = list(open('C:/Users/AmarnathMaddala/Downloads/sample1.txt').read().split())
File_1 = [x.upper() for x in File_1]
# read values from file2 and store in list2 and convert to upper case values
File_2 = list(open('C:/Users/AmarnathMaddala/Downloads/sample2.txt').read().split())
File_2 = [x.upper() for x in File_2]

# To get unique values from both files use set operator
Unique_File1 = set(File_1)
Unique_File2 = set(File_2)

# Use union operator to join both the unique values from both files
print("All Uniques elements in File1 and File2 are : {0}".format(Unique_File1.union(Unique_File2)))

# Use intersection operator that helps to find the values which are in both files
print("All Elements that are in both files : {0}".format(Unique_File1.intersection(Unique_File2)))

# use '-' operator to remove values of send file in first file
print("Elements in first list but not in second list : {0}".format(Unique_File1-Unique_File2))
print("Elements in second list but not in first list : {0}".format(Unique_File2-Unique_File1))

# get all values that are unique in file and file2 and add them by using 'Union' operator to join lists
print("Elements that apper in first or second file but not both : {0}".format((Unique_File1-Unique_File2).union(Unique_File2-Unique_File1)))