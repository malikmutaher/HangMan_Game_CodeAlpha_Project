import random
import time
from colorama import Fore, Style, init

# Initialize colorama for coloring text
init(autoreset=True)


# HANGMAN STAGES (ASCII ART)

stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
    --------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
    --------
    """
]


# WORD CATEGORIES

words = {
    "animals": ["tiger", "elephant", "giraffe", "monkey", "panda", "rabbit"],
    "countries": ["pakistan", "canada", "brazil", "japan", "france", "egypt"],
    "fruits": ["apple", "banana", "mango", "grapes", "orange", "cherry"],
    "programming": ["python", "variable", "loop", "function", "array", "string"]
}


# FUNCTION: Select difficulty

def choose_difficulty():
    print(Fore.CYAN + "\nChoose difficulty level:")
    print("1. Easy (10 lives)")
    print("2. Medium (7 lives)")
    print("3. Hard (5 lives)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 10
    elif choice == "2":
        return 7
    else:
        return 5


# FUNCTION: Select category

def choose_category():
    print(Fore.YELLOW + "\nChoose a category:")
    for i, cat in enumerate(words.keys(), 1):
        print(f"{i}. {cat.capitalize()}")
    choice = int(input("Enter your choice (1-4): "))
    category = list(words.keys())[choice - 1]
    return random.choice(words[category]), category


# MAIN GAME FUNCTION

def play_game():
    print(Fore.GREEN + "\n🎮 Welcome to HANGMAN 🎮")
    time.sleep(1)

    lives = choose_difficulty()
    word, category = choose_category()
    word_letters = set(word)
    guessed_letters = set()
    wrong_guesses = 0
    hint_used = False

    print(Fore.CYAN + f"\nCategory: {category.capitalize()}")
    print("You can use 'hint' one time to get help!")

    while len(word_letters) > 0 and wrong_guesses < len(stages) - 1:
        print(stages[wrong_guesses])
        print(Fore.MAGENTA + f"Lives left: {lives - wrong_guesses}")

        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(display_word))

        guess = input("\nGuess a letter: ").lower()

        if guess == "hint" and not hint_used:
            hint_used = True
            revealed = random.choice(list(word_letters))
            print(Fore.YELLOW + f"Hint: The word contains the letter '{revealed}'!")
            guessed_letters.add(revealed)
            word_letters.remove(revealed)
            continue
        elif guess == "hint" and hint_used:
            print(Fore.RED + "❌ You already used your hint!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(Fore.GREEN + "✅ Nice! Correct guess.")
        else:
            wrong_guesses += 1
            print(Fore.RED + "❌ Wrong guess!")

        print("-" * 30)

 
    # GAME RESULT
 
    if wrong_guesses == len(stages) - 1:
        print(stages[-1])
        print(Fore.RED + f"\n💀 You lost! The word was '{word}'.")
        return 0
    else:
        print(Fore.GREEN + f"\n🎉 You guessed it! The word was '{word}'.")
        return 1

# GAME LOOP (PLAY AGAIN OPTION)

score = 0

while True:
    result = play_game()
    score += result
    print(Fore.BLUE + f"\nYour current score: {score}")
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print(Fore.CYAN + f"\nThanks for playing! Final Score: {score}")
        break
