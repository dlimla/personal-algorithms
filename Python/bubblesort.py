# bubble sort the array

def avg(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # print('hello')
    return arr

def main():
    a = [4, 1,2, 11, 3]
    print(avg(a))

if __name__ == "__main__":
    main()