import random
options = ('rock' , 'paper' , 'scissors')
player = input ('Enter the Player Name : ')
print()
computer_choice = random.choice (options)
player_choice = input ('Enter your choice (rock, paper, scissors ): ') .lower()

while player_choice not in options:
    player_choice = input('Invalid choice. Enter your choice (rock, paper, scissors): ')
    
print (f'{player} chose: {player_choice}')
print (f'Computer chose : {computer_choice}')

if player_choice == computer_choice:
    print ('It\'s a tie')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print ('Rock beats Scissors')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print ('Scissors beats Paper')
elif player_choice == 'paper' and computer_choice == 'rock':
    print ('Paper beats Rock')
else :
    print ('You loose ! Gmae Over!!')
print()
print ('Thanks for playing')
