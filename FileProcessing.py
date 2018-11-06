fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    ipos = line.find(':')
    piece = line[ipos+2:]
    value = float(piece)
    tot = tot + value

print("Average spam confidence:", tot/count)