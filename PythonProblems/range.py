User_points = int(input())
if User_points >= 30 and User_points <= 50:
    print("Average")
elif User_points >= 51 and User_points <= 60:
    print("Good")
elif User_points >= 61 and User_points <= 80:
    print("Excellent")
else:
    print("Outstanding")