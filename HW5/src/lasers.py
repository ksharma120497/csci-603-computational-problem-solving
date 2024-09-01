import sys
from selection_sort import *

"""
CSCI-603 Lab 5: Lasers

A program that gives a grid of number where a laser can be placed 
the laser will be scattered into nearby three element and in 4 directions

We are finding the maximum values with that one direction in it and displaying it

We are also displaying the total sum of all the maximum values

author: Kapil Sharma ks4643
"""


def convert_content_to_int(word):
    """
    While reading the word from file it is getting in the string
    we want to store in integer, so this function is doing that
    :param word: numbers in strings
    :return: list filled with integer values
    """
    words_in_numbers = []
    for element in word:
        words_in_numbers.append(int(element))
    return words_in_numbers


def read_files_from_file(file_name: str):
    """
    This function reads file from the text file passed from the arguments
    :param file_name: name of the text file from where the file will be read
    :return: secret keyword
    """
    open_file = open(file_name)
    file_content = open_file.readlines()
    puzzle_in_array = []
    for line in file_content:
        word = line.split()
        words_in_numbers = convert_content_to_int(word)
        puzzle_in_array.append(words_in_numbers)
    return puzzle_in_array


def ignore_condition(row_length, column_length, i, j):
    """
    This function is used to ignore the corner edges of the puzzle
    so that the laser cant be placed there
    :param row_length: length of the row
    :param column_length: length of the column
    :param i: laser placed at row i
    :param j: laser placed at row j
    :return: a boolean value it returns True if we want to ignore the laser else False
    """
    if i == j == 0 or (i == 0 and j == column_length) or (i == row_length and j == 0) or (
            i == row_length and j == column_length):
        return True
    return False


def number_to_direction(direction_coordinate):
    """
    This code stores the direction in integers so this function gives the
    equivalent values of those integers that translates to a direction
    :param direction_coordinate: integer value
    :return: a character of the direction
    """
    if direction_coordinate == 0:
        return 'N'
    elif direction_coordinate == 1:
        return 'E'
    elif direction_coordinate == 2:
        return 'S'
    elif direction_coordinate == 3:
        return 'W'
    else:
        pass


def sort_with_max_values(laser_max_value, number_of_lasers):
    """
    This function takes the dictionary with keys as coordinates and
    values will be a list with the max value for that coordinate and the direction
    Then we will sort the dictionary based on the max value and then will be store the
    keys into a separate array. This function then display in the order of the keys stored
    in that new list
    :param laser_max_value: dictionary with max value and direction
    :param number_of_lasers: number of lasers given by user
    :return: None
    """
    keys_from_dict = []
    total_sum = 0
    for element in laser_max_value:
        keys_from_dict.append(element)
    sorted_keys = selection_sort(laser_max_value, keys_from_dict)
    print(sorted_keys)
    for element in range(int(number_of_lasers)):
        if element < len(laser_max_value):
            total_sum += laser_max_value[sorted_keys[element]][0]
            print("loc: ( " + sorted_keys[element], "), facing: ",
                  number_to_direction(laser_max_value[sorted_keys[element]][1]), ", sum: ",
                  laser_max_value[sorted_keys[element]][0])
    print("Total Sum: ", total_sum)


def dict_with_max_value(laser_sum_value, number_of_lasers):
    """
    This function takes all the values from the dictionary and creates a new one which
    contains a key as coordinates and values as list with max value and direction
    :param laser_sum_value: dictionary with key as coordinates and value as list of all direction
    :param number_of_lasers: number of laser given by user
    :return: None
    """
    laser_max_value = dict()
    for elements in laser_sum_value:
        max_value = 0
        max_index = 0
        for index in range(len(laser_sum_value[elements])):
            if laser_sum_value[elements][index] > max_value:
                max_value = laser_sum_value[elements][index]
                max_index = index
        laser_max_value[elements] = [max_value, max_index]
    sort_with_max_values(laser_max_value, number_of_lasers)


def laser_game_logic(puzzle, number_of_lasers):
    """
    This function is the one that places laser on all the coordinates and fills the
    dictionary with coordinates as keys and the sum in all the direction as
    values
    :param puzzle: 2D array with the puzzle grid
    :param number_of_lasers: number of lasers entered by user
    :return: None
    """
    laser_sum_value = dict()
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            coordinates = str(i) + "," + str(j)
            if ignore_condition(len(puzzle) - 1, len(puzzle[i]) - 1, i, j):
                laser_sum_value[coordinates] = [0, 0, 0, 0]
            else:
                if i == 0:
                    south = puzzle[i][j - 1] + puzzle[i + 1][j] + puzzle[i][j + 1]
                    laser_sum_value[coordinates] = [0, 0, south, 0]
                elif i == len(puzzle) - 1:
                    north = puzzle[i][j - 1] + puzzle[i - 1][j] + puzzle[i][j + 1]
                    laser_sum_value[coordinates] = [north, 0, 0, 0]
                elif j == 0:
                    east = puzzle[i - 1][j] + puzzle[i][j + 1] + puzzle[i + 1][j]
                    laser_sum_value[coordinates] = [0, east, 0, 0]
                elif j == len(puzzle[i]) - 1:
                    west = puzzle[i - 1][j] + puzzle[i][j - 1] + puzzle[i + 1][j]
                    laser_sum_value[coordinates] = [0, 0, 0, west]
                else:
                    south = puzzle[i][j - 1] + puzzle[i + 1][j] + puzzle[i][j + 1]
                    north = puzzle[i][j - 1] + puzzle[i - 1][j] + puzzle[i][j + 1]
                    east = puzzle[i - 1][j] + puzzle[i][j + 1] + puzzle[i + 1][j]
                    west = puzzle[i - 1][j] + puzzle[i][j - 1] + puzzle[i + 1][j]
                    laser_sum_value[coordinates] = [north, south, east, west]
    print(laser_sum_value)
    dict_with_max_value(laser_sum_value, number_of_lasers)


def print_puzzle_grid(puzzle):
    """
    This function prints the grid of the puzzle that is read
    from the file
    :param puzzle: the grid taken out of the file
    :return: None
    """
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            print(puzzle[i][j], end=" ")
        print(" ")


def main():
    if len(sys.argv) != 2:
        print("Usage: python lasers filename")
        return None
    puzzle = read_files_from_file(sys.argv[1])
    print("Loaded: lazer_puzzle")
    print_puzzle_grid(puzzle)
    number_of_lasers = input("Enter number of lasers: ")
    if int(number_of_lasers) > (len(puzzle) * len(puzzle[0]) - 4):
        print("Too many lasers to place!")
        return None
    print("Optimal placement: ")
    laser_game_logic(puzzle, number_of_lasers)


if __name__ == "__main__":
    main()
