import random
random_number_value = random.randint(1, 100)
guessed = 0

while True:
    print(random_number_value)
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == random_number_value and guessed == 0:
        print("Congratulations! You guessed the correct number. Only one try.")
        break
    elif guess == random_number_value:
        print("Congratulations! You guessed the correct number.")
        print("Your Guess is :", guessed)
        break

    elif guess < random_number_value:
        print("Too low! Try again.")
        clue_a = random_number_value + random.randint(1,10)
        print("Your Guess is :", clue_a)

    elif guess > random_number_value:
        print("Too high! Try again.")
        clue_s = random_number_value + random.randint(1,14)
        print("Your Guess is :", clue_s)

    guessed += 1