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

# variables -------
MAXTICKET = 3
ticketsSold = 0
customers = []




# main routine -------

# This intiates the instruction sequeence. 
# asks the user if they would like the read the instructions using the yes no checker.
instructions = yesNo('\nWould you like to read the Instructions? ')
# this is the instructions loop, the instructions will repeat untill the user states that they understandthe instructions and would liuke to continue
while instructions == 'yes':
    print('Insert Instructions Here\n')
    #user can choose to read the instructions again using the YES NO Function
    instructions = yesNo('Would you like to read the Instructions again? ')

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
        age  = numCheck('What is your age?', 'Please enter a interger')
        if 12 <= age <= 120:
            pass
        elif age < 12: 
            print('Sorry, you are to young to see this film')
            continue
        else:
            print("Uh Oh, That looks like a typo.")
            continue

        # this tells the system that one more rticket has beem sold 
        ticketsSold  += 1
        # this  adds the customer to the list of customers.
        customers.append(name)

print('\nTickets sold tonight: {} '.format(ticketsSold))
print('Tickets Remaining: {}'.format(MAXTICKET - ticketsSold))
print('Attendance at tonights showing: {}'.format(customers))
