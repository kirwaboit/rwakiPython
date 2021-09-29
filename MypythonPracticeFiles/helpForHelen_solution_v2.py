# AUTHOR:     Helen Boit
# COURSE:     ANLY 615
# PROGRAM:    HW 1, Problem 2 Monopoly Railroads
# PURPOSE:    Display the names of the four Monopoly railroad properties
#             and ask the user to identify the property that is not real
# INPUT:      user entry for the railroad property identified as unreal
#             then user is given an option to continue guessing or exit
# PROCESS:    display names of the four Monopoly railroad properties 
#             and ask the user to identify the property that is not real
#             provide an option to continue guessing
# OUTPUT:     display if user selection is correct
#             provide an option to continue guessing or exit
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.


# HEADER

print ("\n The Monopoly Railroads Guessing Game")
print ("+-" * 40)
print (" The names of the four Monopoly railroads are:")
railroads_names = [ "1. Reading Railroad", "2. Pennsylvania Railroad", "3. B&O Railroad", "4. Short Line"]
for ---x in railroads_names:
    print (x)
print ("+-" *40)



# gather input
option = "y"
while option.lower () == "y":
    guessing = input ("Enter the railroad that you think is not real (1-4):\t")

# program ends if user input is correct
    if guessing == "4":
        print ("You are correct! Short Line was not real.\n")
        break
    
# validate user input and provide an option to try again
    elif guessing == "1" or guessing == "2" or guessing == "3":
        option = input ("You are incorrect. Try again? (y/n)\t\t\t")
		
		
		
# I AM TRYING TO VALIDIFY USER INPUT Y OR N, PROMPT FOR RE-ENTRY. BUT I COULDN'T GET IT TO WORK!!!!		
#   while option != "y" and option != "n":
#        input(f'You entered {option}. Please enter either y to continue and n to exit.')
#        continue
 


 
    else:
        option = input ("Entry is invalid. Please only enter a number from 1 to 4. \nTry again? (y/n)\t\t\t")
        continue
   
   
print ()
print ("Bye!")