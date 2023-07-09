print ('Welcome to Bornvitta Quiz competition')
start = input('Do you want to play quiz? ') 
if start .lower() != 'yes':
    quit()
print ('Okay! let\'s play :) ')
user = input('Enter your name :')
Marks = 0

Q1 = input ('1.What does SLR Stands for? :')
if Q1.lower() ==  'statutory liquidity ratio':
    print ('correct!')
    Marks = Marks+1
else:
    print ('o ho! Incorrect')

Q2 = input ('2.How many public sectors bank in India? \n a. 15 \n b. 12 \n c. 10 \n d. 11 \n')
if Q2.lower() ==  'b':
    print ('correct!')
    Marks = Marks+1
else:
    print ('o ho! Incorrect')

Q3 = input ('3.Who is the regulator of money market :')
if Q3.upper() ==  'RBI':
    print ('correct!')
    Marks = Marks+1
else:
    print ('o ho! Incorrect')

Q4 = input ('4.What does SIP stands for? :')
if Q4.lower() ==  'systematic investment plan':
    print ('correct!')
    Marks = Marks+1
else:
    print ('o ho! Incorrect')

Q5 = input ('5.Who is the regulator of capital market? :')
if Q5.upper() ==  'SEBI':
    print ('correct!')
    Marks = Marks+1
else:
    print ('o ho! Incorrect')
print()
print (f'The marks obtained by {user} is {Marks} / 5')
print ('You got '  + str( Marks/5*100) , 'percentage')
