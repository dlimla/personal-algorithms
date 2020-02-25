# needs to return the collatz Sequence
    # if positive then returns the number + the next term halved
    # if term is odd then multiped by 3 then adds 1 so the final result will always lead to 1
    # then returns the whole list + how long it is

def n31(a):
    if not isinstance(a, int):
        print('has to be a number')
    if a < 1:
        print("has to be a positive number")
    else:
        total=[a]
        while a != 1:
            if a % 2 == 0:
                a = a //2
            else:
                a = 3 * a + 1
            total += [a]
        return total, len(total)


def test_n31():
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15)


if __name__ == "__main__":
    num = 11
    path, length = n31(num)
    print(f"The Collatz sequence of {num} took {length} steps. \nPath: {path}")
