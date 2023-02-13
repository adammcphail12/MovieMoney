
MAXTICKET = 3
ticketsSold = 0
customers = []

while MAXTICKET > ticketsSold :
    name = input('\nPlease Input your Name to purchase a ticket, OR , if you \nwould like to quit please enter XXX ').lower()
    if name == 'xxx':
        break
    else:
        ticketsSold  += 1
        customers.append(name)

print('\nTickets sold tonight: {} '.format(ticketsSold))
print('Tickets Remaining: {}'.format(MAXTICKET - ticketsSold))
print('Attendance at tonights showing: {}'.format(customers))


