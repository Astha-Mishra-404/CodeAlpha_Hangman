import random

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                   "   ",
                   "   "),
                2: (" o ",
                   " | ",
                   "   "),
                3: (" o ",
                   "/| ",
                   "   "),
                4: (" o ",
                   "/|\\",
                   "   "),
                5: (" o ",
                   "/|\\",
                   "/  "),
                6: (" o ",
                   "/|\\",
                   "/ \\")}

categories = {
    "Animals": {
        "aardvark": "A burrowing animal with a long snout.",
        "alligator": "A large reptile found in the Americas.",
        "alpaca": "A domesticated species of South American camelid.",
        "ant": "A small insect that lives in colonies.",
        "anteater": "An animal that feeds on ants and termites.",
        "antelope": "A swift-running herbivorous animal.",
        "ape": "A large primate without a tail.",
        "armadillo": "A small mammal with a shell."
    },
    "Fruits": {
        "apple": "A common fruit that is red, green, or yellow.",
        "banana": "A long yellow fruit that is sweet.",
        "cherry": "A small, round fruit that is often red or black.",
        "date": "A sweet fruit from the date palm tree.",
        "elderberry": "A small dark berry used in syrups.",
        "fig": "A soft fruit with many seeds inside.",
        "grape": "A small round fruit that grows in bunches.",
        "kiwi": "A small brown fruit with green flesh."
    },
    "Colors": {
        "red": "The color of blood or ripe strawberries.",
        "blue": "The color of the sky on a clear day.",
        "green": "The color of grass and leaves.",
        "yellow": "The color of ripe bananas.",
        "purple": "A color often associated with royalty.",
        "orange": "A color that is also a fruit.",
        "pink": "A light shade of red.",
        "brown": "The color of chocolate and coffee."
    }
}

def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def choose_category():
    print("Choose a category:")
    for idx, category in enumerate(categories.keys(), start=1):
        print(f"{idx}. {category}")
    choice = int(input("Enter the number of the category: ")) - 1
    return list(categories.values())[choice], list(categories.keys())[choice]

def main():
    selected_words, category_name = choose_category()
    answer = random.choice(list(selected_words.keys()))
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print(f"Hint: {selected_words[answer]}")  # Display the hint for the chosen word

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
