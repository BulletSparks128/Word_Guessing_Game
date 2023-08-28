import random

name = input("What's your name? ")

print ("These are your options: astronomy, astrophysics, biochemistry, biology, botany, chemistry, entomology, eletricity, genetics, geology, geophysics, herpetology, immunology, magnetism, laboratory, meteorologist")

print("Good Luck, ", name, "!")

words = ['astronomy', 'astrophysics', 'biochemistry', 'biology', 'botany', 'chemistry', 'entomology', 'eletricity','genetics', 'geology', 'geophysics', 'herpetology', 'immunology', 'magnetism', 'laboratory', 'meteorologist']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses: print (char, end="  ")

        else:
            print("__")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1

        print("Wrong!")

        print("You have ", + turns, 'more guesse')

        if turns ==0:
            print("You lose!")