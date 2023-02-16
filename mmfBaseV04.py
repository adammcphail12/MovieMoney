# functions -------

# notblankinput
def not_blank (question,error ):
    while  True:
        name = input(question).lower()
        if name == '':
            print(error)
        else:
            return name

#num check so that you dont crash
def num_check(question, error):

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
def string_check(question, valid_1 , valid_2, valid_3, valid_4, error):
    
    while True:
        user = input('{} '.format(question)).lower()
        if user == valid_1 or user == valid_2:
            return valid_1
        elif user == valid_3 or user == valid_4:
            return valid_3
        else:
            print(error)
    

# variables -------
MAX_TICKET = 3
tickets_sold = 0
customers = []
ticket_price= 0



# main routine -------

# This intiates the instruction sequeence. 
# asks the user if they would like the read the instructions using the yes no checker.
instructions = string_check('\nWould you like to read the Instructions? ','yes','y','no','n','Please Enter Yes Or No.')
# this is the instructions loop, the instructions will repeat untill the user states that they understandthe instructions and would liuke to continue
while instructions == 'yes':
    print('Insert Instructions Here\n')
    #user can choose to read the instructions again using the YES NO Function
    instructions = string_check('\nWould you like to read the Instructions again? ','yes','y','no','n','Please Enter Yes Or No.')

# The user has now finnished the instructions sequence and is ready to continue inbto purchasing the tickets.
print('\nOk Lets Continue.')


# Begins the ticket sale sequence 
while MAX_TICKET > tickets_sold :
    #this loop runs while not all of the tickets have been sold.
    name = not_blank('\nPlease Input your Name to purchase a ticket, OR , if you \nwould like to quit please enter XXX ', 'Sorry blank is not a valid answer, please enter either your name,\nor xxx to quit.')
    #if they enter xxx the loop will end.
    if name == 'xxx':
        break
    else:
        age  = num_check('What is your age? ', 'Please enter a interger')
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
            ticket_price += 7.50
            print('That will be $7.50 Please')
        elif age >= 65: 
            ticket_price += 6.50
            print('That will be $6.50 Please')
        else:
            ticket_price += 10.50
            print('That will be $10.50 Please')
        # this tells the system that one more rticket has beem sold 
        tickets_sold  += 1
        print('Total Cost: ${}'.format(ticket_price))
        # this  adds the customer to the list of customers.
        customers.append(name)
        
payment_method = string_check('Would you like to pay with Cash or Credit? ','cash', 'ca','credit', 'cr','Sorry That is not a valid input. Valid inputs include Cash or Credit')

print('Ok {} sounds good.'.format(payment_method))
print('\nTickets sold tonight: {} '.format(tickets_sold))
print('Tickets Remaining: {}'.format(MAX_TICKET - tickets_sold))
print('Attendance at tonights showing: {}'.format(customers))
