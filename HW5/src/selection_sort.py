def find_min_index(allData, data, mark):
    """
    This function compares with the first value of the dictionary that stores
    the max value of each coordinates and then it finds the minimum index and returns it
    :param allData: dictionary which contains max value as its value
    :param data:  the list of keys of dictionary
    :param mark: the index at the current iteration
    :return: minimum index
    """
    min_index = mark
    for element in range(mark+1, len(data)):
        if allData[data[element]][0] > allData[data[min_index]][0]:
            min_index = element
    return min_index


def selection_sort(allData, data):
    """
    This function calls the find_min_index function to find the minimum index and
    then swap the value of that index with the current index value. This will
    sort the list with all the keys so that we can read the data in that order
    :param allData: a dictionary with coordinates as keys
    :param data: list of all keys
    :return: the sorted list of keys
    """
    for mark in range(len(data)):
        min_index = find_min_index(allData, data, mark)
        data[mark], data[min_index] = data[min_index], data[mark]
    return data

def main():
    pass


if __name__ == "__main__":
    main()