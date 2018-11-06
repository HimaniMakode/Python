hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)

if h <= 40:
    pay = (h * r)
    print(pay)
elif h > 40:
    r1 = 1.5 * r
    pay = (40 * r) + ((h-40) * r1)
    print(pay)