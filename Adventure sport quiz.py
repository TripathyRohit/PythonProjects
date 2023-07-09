name = input('Enter your name :')
print (name, 'Welcome to the world of Adventure ! ')
print()
step = input ('This is a cake walk ! say I am a Rodie :' ) .lower()
print()
step_1 = input ('o ho! this is dead end you have to choose your path either left or right :') .lower()
print()
if step_1 == 'left':
    step_2 = input ('There is a river in front of you and a bridge across it, choose one of the option. \n a. swim accross \n b. walk through a bridge. \n ')
    if step_2 == 'a':
        print('There is an alligator in the river be carefull ! you ll be eaten by it and loose the game')
    elif step_2 == 'b':
        print ('This is a broken bridge you ll fall in the river,eaten by an alligator and loose the game')
    else:
        print ('wrong input you loose!!')
    
elif step_1 == 'right' :
    step_3 = input ('You come to a highway, looks very busy road . What you want to do \n a. cross the road \n b.take a subway \n' ) .lower()
    if step_3 == 'a':
        print ('Be careful!! if you hit by any vechile you gonna loose the game !')
    elif step_3 == 'b':
        print (' If you are taking a subway you ll defeat your apoonent easily and win a gold coin!')
    else:
        print ('Wrong input you loose!')

else:
    print ('wrong input you loose!!')
print()
print ('Thank You!' ,name, 'for playing this sport') 
