# find the minimum of the array
import math
def avg(arr):
    
    # print('hello')
    if len(arr) == 0:
        return arr
    if len(arr) > 0:
        average = 0
        for i in arr:
            average += i
    return math.floor(average/len(arr))


def main():
    a = [4, 1,2, 11, 3]
    print(avg(a))

if __name__ == "__main__":
    main()