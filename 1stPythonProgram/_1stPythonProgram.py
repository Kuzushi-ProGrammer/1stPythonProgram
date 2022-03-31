num = input ('ENTER A NUMBER BITCH: ')      #Takes input from user


num = int(num)         #Coverts input to integer for variable use
pos = True             #Setting default state for integer

if num == 69:
    print ('nice')    # If the number inputted equals 69 ot 420, an additional output is printed
elif num == 420:
    print('weed')
else:
    print (':(')    # If no number equals 69 or 420, a different additional output is printed
print (num)           #The number that was inputted is printed

if num < 0:         #Checking if the number input is below zero and setting an additional variable to false
   pos = False

if pos is False:
    print ('why so negative?')      #If the number is below zero a unique message is output

input('-Press Enter to end the inquiry-')   # Stops the program from closing immediately after the number is input
