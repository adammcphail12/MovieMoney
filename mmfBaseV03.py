# functions -------

# yes/no check
def yesNo(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')

# notblankinput
def notBlank (question,error ):
    while  True:
        name = input(question).lower()
        if name == '':
            print(error)
        else:
            return name

#num check so that you dont crash
def numCheck(question, error):

    valid = False
    while not valid:
         try:
             response = int(input(question))
             if 0 < response:
                 return response
             else:
                 print(error)
         except ValueError:
             print(error)

# string check
def stringCheck(question, valid1 , valid2, valid3, valid4, error):
    
    while True:
        user = input(question).lower()
        if user == valid1 or user == valid2:
            return valid1
        elif user == valid3 or user == valid4:
            return valid3
        else:
            print(error)
    

# variables -------
MAXTICKET = 3
ticketsSold = 0
customers = []
ticketPrice= 0



# main routine -------

# This intiates the instruction sequeence. 
# asks the user if they would like the read the instructions using the yes no checker.
instructions = stringCheck('\nWould you like to read the Instructions? ','yes','y','no','n','Please Enter Yes Or No.')
# this is the instructions loop, the instructions will repeat untill the user states that they understandthe instructions and would liuke to continue
while instructions == 'yes':
    print('Insert Instructions Here\n')
    #user can choose to read the instructions again using the YES NO Function
    instructions = stringCheck('\nWould you like to read the Instructions again? ','yes','y','no','n','Please Enter Yes Or No.')

# The user has now finnished the instructions sequence and is ready to continue inbto purchasing the tickets.
print('\nOk Lets Continue.')


# Begins the ticket sale sequence 
while MAXTICKET > ticketsSold :
    #this loop runs while not all of the tickets have been sold.
    name = notBlank('\nPlease Input your Name to purchase a ticket, OR , if you \nwould like to quit please enter XXX ', 'Sorry blank is not a valid answer, please enter either your name,\nor xxx to quit.')
    #if they enter xxx the loop will end.
    if name == 'xxx':
        break
    else:
        age  = numCheck('What is your age? ', 'Please enter a interger')
        if 12 <= age <= 120:
            pass
        elif age < 12: 
            print('Sorry, you are to young to see this film')
            continue
        else:
            print("Uh Oh, That looks like a typo.")
            continue
        #Ticket price calculator
        if 12 <= age <=  15:
            ticketPrice += 7.50
            print('That will be $7.50 Please')
        elif age >= 65: 
            ticketPrice += 6.50
            print('That will be $6.50 Please')
        else:
            ticketPrice += 10.50
            print('That will be $10.50 Please')
        # this tells the system that one more rticket has beem sold 
        ticketsSold  += 1
        print('Total Cost: ${}'.format(ticketPrice))
        # this  adds the customer to the list of customers.
        customers.append(name)
        
paymentMethod = stringCheck('Would you like to pay with Cash or Credit? ','cash', 'ca','credit', 'cr','Sorry That is not a valid input. Valid inputs include Cash or Credit')

print('Ok {} sounds good.'.format(paymentMethod))
print('\nTickets sold tonight: {} '.format(ticketsSold))
print('Tickets Remaining: {}'.format(MAXTICKET - ticketsSold))
print('Attendance at tonights showing: {}'.format(customers))
