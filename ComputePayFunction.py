def computepay (h, r):
    if h <= 40:
        pay = (h * r)

    elif h > 40:
        r1 = 1.5 * r
        pay = (40 * r) + ((h-40) * r1)

    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print(p)