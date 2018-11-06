score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print("Please enter number in range between 0.0 to 1.0")
if fs > 0.0 and fs < 1.0:

    if fs >= 0.9:
        print("A")
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    elif fs < 0.6:
        print("F")
else:
    print("Please enter number in range between 0.0 to 1.0")