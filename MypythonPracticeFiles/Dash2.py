x,y=3,4

#print(x)


d=dict()
d['csev'] = 2
d['cwen'] = 4

tups = d.items()
#print(tups)

c ={'a':10,'b':1,'c':22}

#print(sorted ([(v,k)for k,v in c.items()]))
#######################################################################


##################################################################
'''FINAL ASSIGNMENT
In this assignment Read data from  a text file, load it into python, 
parse through it line by line and  and if a line starts with 'From' ,
 then split it up by space, select the 5 string in the line, then split that by 
 colon, then select the first part of that string then add it to a dictionary 
 along with the number of times it shows up in the entire document,essentially 
 creating a histogram'''

counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From '):
        selectedLine = line.split()
        #print(selectedLine)
        lineSelected = selectedLine[5]
        hourSplit = lineSelected.split(':')
        hourString = hourSplit[0]
        #print(hourString)
        counts[hourString] = counts.get(hourString, 0) + 1    # assigns a value to a dictionary

#print(counts)
#sortedString = (sorted ([(k,v)for k,v in counts.items()]))

for k,v in sorted ([(k,v)for k,v in counts.items()]):
    print(k,v)

