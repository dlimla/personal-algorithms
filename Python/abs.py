"""Absolute Value."""


def abs_val(num):

    # print('hello')
    if num == 0:
        return num

    elif num < 0:
        return num * -1
        
if __name__ == "__main__":
    print(abs_val(-34))  # --> 34
    print(abs_val(0))