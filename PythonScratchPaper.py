largest = None
smallest = None
initializeInputFlag=0  # zero means the inputs have not been initialized
while True:
    num = input("Enter a number: ")
    if num == "done": break
    #print(num)
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue
    if initializeInputFlag==0:
        largest=num
        smallest=num
        initializeInputFlag = 1

    if largest<num:
        largest=num
    if smallest>num:
        smallest=num


print("Maximum is", int(largest))
print("Minimum is", int(smallest))