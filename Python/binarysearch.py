# A binary search implementation to test if a number is in a list of elements


def binary_search(a_list, item):

    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1 :], item)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
