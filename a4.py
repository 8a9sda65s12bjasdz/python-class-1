import sys
name = input("Name of person that we are calculating the grades for: ")
ts1 = float(input("Test 1: "))
ts2 = float(input("Test 2: "))
ts3 = float(input("Test 3: "))
ts4 = float(input("Test 4: "))
ls = input("Should the lowest grade be dropped from the calculation? ")
if ts1 < 0 or ts2 < 0 or ts3 < 0 or ts4 < 0:
    print("Test scores must be greater than 0")
    sys.exit()
if ls != "Y" and ls != "N":
    print("Enter Y or N to drop the lowest grade.")
    sys.exit()
if ls == "Y":
    if ts1 <= ts2 and ts1 <= ts3 and ts1 <= ts4:
        avgs= (ts2 + ts3 + ts4) / 3
    elif ts2 <= ts1 and ts2 <= ts3 and ts2 <= ts4:
        avgs= (ts1 + ts3 + ts4) / 3
    elif ts3 <= ts1 and ts3 <= ts2 and ts3 <= ts4:
        avgs = (ts1 + ts2 + ts4) / 3
    elif ts4 <= ts1 and ts4 <= ts2 and ts4 <= ts3:
        avgs = (ts1 + ts2 + ts3) / 3
if ls == "N":
    avgs = (ts1 + ts2 + ts3 + ts4) / 4
print(f"{name} your average score is: {avgs:.1f}")
if avgs >= 97.0:
    print("Your letter grade is: A+")
elif avgs >= 94.0 and avgs <= 96.9:
    print("Your letter grade is: A")
elif avgs >= 90.0 and avgs <= 93.9:
    print("Your letter grade is: A-")
elif avgs >= 87.0 and avgs <= 89.9:
    print("Your letter grade is: B+")
elif avgs >= 84.0 and avgs <= 86.9:
    print("Your letter grade is: B")
elif avgs >= 80.0 and avgs <= 83.9:
    print("Your letter grade is: B-")
elif avgs >= 77.0 and avgs <= 79.9:
    print("Your letter grade is: C+")
elif avgs >= 74.0 and avgs <= 76.9:
    print("Your letter grade is: C")
elif avgs >= 70.0 and avgs <= 73.9:
    print("Your letter grade is: C-")
elif avgs >= 67.0 and avgs <= 69.9:
    print("Your letter grade is: D+")
elif avgs >= 64.0 and avgs <= 66.9:
    print("Your letter grade is: D")
elif avgs >= 60.0 and avgs <= 63.9:
    print("Your letter grade is: D-")
elif avgs <= 59.9:
    print("Your letter grade is: F")








