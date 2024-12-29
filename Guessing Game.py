import random

print('LETS SEE HOW MUCH YOU CAN PREDICT')
COUNT=0
FAIL=0
print('You have 10 chances')
for i in range(10):
    number=random.randint(1,10)
    guess=int(input('Guess a number between 1 to 10:'))

    if guess==number:
        print('YOU WON!')
        COUNT=COUNT+1
    else:
        print('TRY AGAIN')
        print('It was', number)
        FAIL=FAIL+1
x=(COUNT/10)*100
print('Prediction % =',x)
if x<40:
    print('PRACTICE MORE')
if x<70 and x>40:
    print('THAT WAS GOOD')
if x>70:
    print('YOU CAN BE AN ASTROLOGER')
