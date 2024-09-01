import random
import sys

"""
CSCI-603 Lab 4: Wordle

A program that implements the game of Wordle 
The program will read in from the standard input and print the results in the standard output.

The secret word can be given from the command line and also from the text file

author: Kapil Sharma ks4643
"""


def isAlreadyVisited(visited_array, guess_index):
    """
    This function keeps track of everything that has already visited inside the answer string
    and stores it inside an array
    :param visited_array: this is an array to store if the letters are already visited
    :param guess_index: index that we need to compare and store
    :return: boolean returns true if the index already exists inside the array else false
    """
    for i in range(len(visited_array)):
        if visited_array[i] == guess_index:
            return True
    return False


def display_patterns(guess_word: str, answer_word: str, visited_array):
    """
    This function executes the comparison code and returns two things one is the
    list of visited array and pattern string that we need to display

    :param guess_word: word defined by user
    :param answer_word: the secret word
    :param visited_array: list of indexes already visited
    :return: visited array and pattern string
    """
    pattern_string = ""
    for i in range(5):
        if guess_word[i] == answer_word[i] and (not isAlreadyVisited(visited_array, i)):
            pattern_string = pattern_string + "^"
            visited_array.append(i)
        elif answer_word.find(guess_word[i]) != -1 and (
        not isAlreadyVisited(visited_array, answer_word.find(guess_word[i]))):
            pattern_string = pattern_string + "*"
            visited_array.append(answer_word.find(guess_word[i]))
        else:
            pattern_string = pattern_string + " "

    return visited_array, pattern_string


def guess_game_function(guess_word: str, answer_word: str, number_of_guesses: int, set_of_used_letters):
    """
    This function runs for 6 number of tries and prints the guessed word with its pattern
    After 6 tries the code will terminate with displaying the word itself
    :return: None
    """
    if len(guess_word) == 5:
        if number_of_guesses < 6:
            visited_array = []
            print("Number of guesses: ", number_of_guesses, " of 6")
            print(guess_word)
            for letters in guess_word:
                set_of_used_letters.add(letters)
            visited_array, pattern_string = display_patterns(guess_word, answer_word, visited_array)
            print(pattern_string)
            print("Letters used: ", set_of_used_letters)
            if pattern_string == "^^^^^":
                print("You won!!")
                return None
        else:
            print("You lost!!")
            print("The secret word was ", answer_word)
    else:
        print("Illegal Word.")


def cheat_game_function(answer_word):
    """
    Prints the secret word
    :param answer_word:
    :return: None
    """
    print("Secret Word: ", answer_word)


def help_game_function():

    print("Commands:")
    print("new: Start a new game")
    print("guess <word>: Make a guess")
    print("cheat: Show the secret word")
    print("help: This is help message")
    print("quit: End the program")


def action_selectors(user_input: str, answer_word: str, number_of_guesses: str, set_of_used_letters):
    """
    This function performs actions and call different functions based on the given command
    in the command line

    :param user_input: it will have the commands given by user
    :param answer_word: secret word
    :param number_of_guesses: that would be updated value of guesses
    :param set_of_used_letters: letters that are being used
    :return: number of guesses
    """
    if user_input == "new":
        main()
    if "guess" in user_input:
        number_of_guesses = number_of_guesses + 1
        guess_game_function(user_input.split(" ")[1], answer_word, number_of_guesses, set_of_used_letters)
    if user_input == "cheat":
        cheat_game_function(answer_word)
    if user_input == "help":
        help_game_function()
    return number_of_guesses


def read_files_from_file(file_name: str):
    """
    This function reads file from the text file passed from the arguments
    :param file_name: name of the text file from where the file will be read
    :return: secret keyword
    """
    open_file = open(file_name)
    file_content = open_file.readlines()
    random_number = random.randint(1, 10)
    return file_content[random_number]


def main():
    print("Welcome to Wordle App!")
    print("Commands:")
    print("new: Start a new game")
    print("guess <word>: Make a guess")
    print("cheat: Show the secret word")
    print("help: This is help message")
    print("quit: End the program")
    number_of_guesses = 0
    set_of_used_letters = set()
    answer_word = read_files_from_file("/HW4/data/wordle.txt")
    if len(sys.argv) == 3:
        answer_word = sys.argv[1]
    else:
        print("Usage Wordle: [1st-secret-word]")
    while True:
        prompt = input()
        print(prompt)
        if prompt != "quit":
            number_of_guesses = action_selectors(prompt, answer_word, number_of_guesses, set_of_used_letters)
        else:
            print("Bye!")
            break


if __name__ == '__main__':
    main()
