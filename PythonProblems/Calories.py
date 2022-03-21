
def calories_burned():
    for i in range(10,31):
        if i%5 == 0:
            total_calories = i*4.2
            print("{0}\t\t\t{1}".format(i,total_calories))


if __name__ == '__main__':
    print("{0}\t\t{1}".format("Minutes","Calories"))
    calories_burned()