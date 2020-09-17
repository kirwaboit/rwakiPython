counts = dict()
name = input("Enter file:")
emailAddresses = dict()
if len(name) < 1:name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From: '):
        selectedLine = line.split()
        lineSelected = selectedLine[1]
        counts[lineSelected] = counts.get(lineSelected, 0) + 1    # assigns a value to a dictionary

# Now we have a dictionary that is like a histogram of values above,
# but we want to do a sort on this

# make a list and add the key values from the dictionary to it,BUT make sure to add
# the values in reverse form to ensure the numric value comes first in the tuple pair

######################################################
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

# not take the list values and do a revers sort to have the highest value first
lst = sorted(lst,reverse=True)

# finally we print the values again, BUT this time in a way to ensure the key comes first
# for readability
for val,key in lst[:10]:
    #print(key, val)
    continue

#########################################################
'''THE ABOVE CODE CAN ALSO BE DONE IN ONE LINE USING LIST COMPREHENSION '''
c ={'a':10,'b':1,'c':22}

print(sorted ([(v,k)for k,v in c.items()]))





# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)

