counts = dict()
name = input("Enter file:")
emailAddresses = dict()
if len(name) < 1:name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From: '):
        selectedLine = line.split()
        lineSelected = selectedLine[1]
        counts[lineSelected] = counts.get(lineSelected, 0) + 1    # assigns a value tro a doitionary

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)