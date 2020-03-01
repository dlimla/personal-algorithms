# the fibonacci sequence


def fibonacci(n):
    fibSeq=[0,1,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        i = 2
        temp = 0
        while i < n:
            temp = n[-1] + n[-2]
            temp.append(fibSeq)
            return fibSeq