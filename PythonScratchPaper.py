
counts = dict()  #counts is a new dictionary
names = ['csev', 'cwen', 'csev' , 'zqian' , 'cwen' ]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)