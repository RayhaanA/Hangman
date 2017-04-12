import random
import time

def main():
    words = ['Apple', 'Ball', 'Cathode', 'Deceive', 'Emulate', 'Frigate',
             'Guardian', 'Hair', 'Indigo', 'Jelly', 'Kathmandu', 'Location',
             'Meningitis', 'Jam', 'Yarn', 'Truck', 'Staking', 'Steel', 'Scared',
             'Ship', 'Support', 'Bubble', 'Grieving', 'Quickest', 'Interest',
             'Resolute', 'Man', 'Silk', 'Macho', 'Disarm', 'Kitty', 'Absorbed',
             'Screw', 'Chase', 'Mourn' 'Repeat', 'Waste', 'Juggle', 'Snow',
             'Decorous', 'Tooth', 'Meat' 'Carry', 'Super', 'Wave', 'Thick',
             'Attack', 'Excuse', 'Tangible' 'Obtain', 'Unwritten', 'Yak', 'Decay',
             'Flowers', 'Judicious', 'Crook', 'Shade', 'Found', 'Giddy', 'Roof',
             'Aback', 'Island']

    word = random.choice(words)

    num_letters = len(word)

    answer = '-' * len(word)

    guessed_letters = []

    lives = 10

    hint_used = False

    while answer.lower() != word.lower() and lives > 0:
        correct_guess = False
        print("Lives left: {}".format(lives))
        print("Number of letters: {}".format(num_letters))

        if not hint_used:
            print("Type 'hint' for a hint!\n")

        guess = str(input("Guess a letter or the word! {}\n".format(answer)))

        if guess.lower() == "hint":
            if hint_used:
                print("Already used your hint!\n")

            else:
                print("Used your only hint!\n")
                unguessed_letters = []
                for letter_pos in range(len(word)):
                    if answer[letter_pos] == '_':
                        unguessed_letters.append(letter_pos)

                hint_letter = word[random.choice(unguessed_letters)]

                for letter_pos in range(len(word)):
                    if word[letter_pos].lower() == hint_letter.lower():
                        hint_letter = hint_letter.upper() if letter_pos == 0 else hint_letter.lower()
                        answer = answer[0:letter_pos] + hint_letter + \
                            answer[letter_pos + 1:len(answer)]
                hint_used = True

        elif not guess.isalpha():
            print("Please enter letter/word guesses only!\n")

        elif guess.lower() in guessed_letters:
            print("You've already guessed that letter!\n")

        else:
            if len(guess) > 1:
                if guess.lower() == word.lower():
                    answer = word
                    correct_guess = True
            else:
                for letter_pos in range(len(word)):
                    if word[letter_pos].lower() == guess.lower():
                        guess = guess.upper() if letter_pos == 0 else guess.lower()
                        answer = answer[0:letter_pos] + guess + \
                            answer[letter_pos + 1:len(answer)]
                        correct_guess = True

            if not correct_guess:
                lives -= 1
                print("You guessed wrong!\n")
            else:
                print("Good guess!\n")

            if len(guess) == 1:
                guessed_letters.append(guess.lower())

        print("****************************\n")
        time.sleep(1.0)

    if lives == 0:
        print("Game over, you ran out lives!\n")

    else:
        print("You won!\n")

    print("The word was {}".format(word))

if __name__ == "__main__":
    main()
