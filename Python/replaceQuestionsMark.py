import random

A = 'ac?df?e'

def splitStringIntoNumbers(x):
  arr = []
  for letter in x:
    arr.append(ord(letter) - 96)
  return arr

def randomNum():
  listofNumbers = []
  for x in range(1,27):
    listofNumbers.append(x)

  randomNum = random.choice(listofNumbers)
  return randomNum


def replaceQuestions(A):

  numberArr = splitStringIntoNumbers(A)
  randomNumber = randomNum()

  while randomNumber in numberArr:
    randomNumber = randomNum()


  for i, item in enumerate(numberArr):
    # item = chr(item)
    # print(chr(item + 96))
    if item == -33:
      numberArr[i] = chr(randomNumber + 96)
    else:
      numberArr[i] = chr(item + 96)

  combinedArr = "".join(numberArr)
  
  print(combinedArr)
  # print(newString)



replaceQuestions(A)
