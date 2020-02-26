# find the minimum of the array
def abs_val(num):
    
    # print('hello')
    if num == 0:
        return num

    elif num < 0:
        return num * -1

def absMin(x):
    current = x[0]
    for i in x:
        if abs_val(i) < abs_val(current):
            current = i
    return current 

def main():
    a = [-4, -1,-2, 11, 3]
    print(absMin(a))

if __name__ == "__main__":
    main()