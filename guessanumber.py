import random 

print('Hello. What is your name?')

UserName = input()
print('Well, '+str(UserName)+', I am thinking of a number between 1 and 10.')
print('You get 6 attempts.')

ObjectiveNumber = random.randint(1,10)

def inputNumber():
    j = 1
    while j == 1:
        try:
            AttemptNumber = int(input())
            j=0
        except ValueError:
            print('Please insert an interger')
            continue
    return AttemptNumber        

def guesses():
    for i in range(0,7):
        print('Take a guess.')
        AttemptNumber = inputNumber()
        if AttemptNumber == ObjectiveNumber:
            print('Correct. You guessed the number in ' + str(i+1) + ' attempts')
            break
        elif i==5:
            print('Sorry. I was thinking of '+str(ObjectiveNumber) )
            break
        elif AttemptNumber > ObjectiveNumber:
            print('Incorrect. Your guess is too high. Try again.')
        elif AttemptNumber < ObjectiveNumber:
            print('Incorrect. Your guess is too low. Try again.')
        else:
            print('Incorrect guess. Try again.')

guesses()

  

        
    
