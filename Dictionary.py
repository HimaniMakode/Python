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
    email = words[1]
    stuff[email] = stuff.get(email, 0) + 1

EmailAdd = None
EmailCounts = None
for email, Count in stuff.items():
    if EmailCounts is None or Count > EmailCounts:
        EmailAdd = email
        EmailCounts = Count
print(EmailAdd, EmailCounts)