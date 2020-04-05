
def number_of_divisors(n: int) -> int:
    """Calculate Number of Divisors of an Integer.
    >>> number_of_divisors(100)
    9
    """
    div = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div *= temp
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div *= temp
    return div

if __name__ == "__main__":
    print(number_of_divisors(100))
