import pandas
# dictionaries to hold ticket details.

all_names = ['a','b','c','d','e']
all_tickets_costs = [7.50,7.50,10.50,10.50,6.50]
surcharge = [0,0,0.53,0.53,0]


mini_movie_dict = {
    'Name' : all_names,
    'Ticket Price' : all_tickets_costs,
    'Surcharge' : surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

#calulate total cost (ticket + surcharge)
mini_movie_frame['Total'] = (mini_movie_frame['Surcharge'] +
mini_movie_frame['Ticket Price'])


mini_movie_frame['Profit'] = (mini_movie_frame['Ticket Price'] - 5)

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()


print(mini_movie_frame)

print('Total ticket sales : ${}'.format(total))
print('Total Profit : ${}'.format(profit))
