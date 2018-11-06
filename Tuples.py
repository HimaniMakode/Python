name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

stuff = dict()

for line in handle:
    line = line.rstrip()
    if (not line.startswith('From')) or (line.startswith('From:')):
        continue
    words = line.split()
    time = words[5]
    timesplit = time.split(':')
    hour = timesplit[0]

    stuff[hour] = stuff.get(hour, 0) + 1

lst = list()
for hour, Count in stuff.items():
    newtup = (hour, Count)
    lst.append(newtup)
lst = sorted(lst)
for hour, Count in lst:
    print(hour, Count)