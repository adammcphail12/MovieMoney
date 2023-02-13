# ------- functions -----------------

#Statement_Gen is for all the fancy decorations and and stuff.
def statement_gen(statement, decoration,lines,dec_num,del_num) :
    #(Statement is what you say)(This is the charecter for your lines to be "^")(This is how many rows.)(This is how long the decor4ation is on either side)(This is how many charecters need to be deleted)
    sides = decoration * dec_num
    statement = ("{} {} {}".format(sides,statement,sides))
    if lines == 3:
        #this is what happens when you wantg three rows
        
        topbottomlenth = len(statement) - del_num # Number cannot * a string in the same variable
        topbottomv2 = topbottomlenth * decoration 

        print(topbottomv2)
        print(statement)
        print(topbottomv2)

        #This is what happens when you want only one row
        
    else:
        print(statement)
    
    return ""


# Yes / No Check
def yesNo(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')


# ------- main routine

statement_gen('\x1B[33mM \x1B[32mM \x1B[31mF\x1B[0m', '#', 3 ,10,19)

instructions = yesNo('\nWould you like to read the Instructions? ')
if instructions == 'yes':
    print('Insert Instructions Here\n')
print('Ok Lets Continue.')