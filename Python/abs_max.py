# from .abs import abs_val


def absMin(x):
    """
    >>> absMin([0,5,1,11])
    0
    >>> absMin([3,-10,-2])
    -2
    """
    min_abs_value = x[0]

    for i in x:
        if abs(i) < abs(min_abs_value):
            min_abs_value = i
    return min_abs_value


def main():
    a = [-3, -1, 2, -11]
    print(absMin(a))  # = -1


if __name__ == "__main__":
    main()
