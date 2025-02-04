from random import randint

number = randint(0, 100)
print('Guess number between 0 and 100')
while True:
    guess = int(input('Enter a number: '))

    if guess < number:
        print('Number is higher than input')
    elif guess > number:
        print('Number is lesser than input')
    elif guess == number:
        print('You guessed the number!')
        break
