import math
from math import modf
arr1 = [7, 10, 12, 40, -100, -5, 2]
arr2 = [17, 100, 212, -1140, -600, 5, -12]
arr3 = [-70, -80, 0, -40, 250, 15, 2]

# Return the given array, after setting any negative values to zero.
def zeroOut(arr):
    for x in range(len(arr)):
        # print(x)
        if arr[x] < 0:
            arr[x] = 0
    return arr
        
        

# print(zeroOut(arr3))


# def zeroOut(list):
#     temp = 0
#     for x in list:
#         # print(x)
#         if x < 0:
#             x = temp
#             x = 0
#             temp = 0
            
#     return list
        
        

# print(zeroOut(arr1))
print("_________________________")

# Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.
def shiftArrayValsLeft(arr):
    for x in range(1, len(arr)):
        # previous index = current index- this is where we are shifting is happening
        arr[x-1] = arr[x]
    # last item in list
    arr[len(arr)-1] = 0
    return arr

# print(shiftArrayValsLeft(arr2))

print("_________________________")

# Implement function sigma(num) that given a number, returns the sum of all positive integers up to
# number (inclusive). Ex.:sigma(3)=6(or1 + 2 + 3);sigma(5)=15(or1 + 2 + 3 + 4 + 5).
x = 5
y = 9
z = 15
def sigma(num):
    sum = 0
    for x in range(1, num+1):
        sum +=x
        print(sum)
    return sum


# print(sigma(x))

print("_________________________")

def factorial(num):
    sum = 1
    for x in range(1, num+1):
        sum *=x
        print(sum)
    return sum
# print(factorial(x))

print("_________________________")

# Write a function drawLeftStars(num) that accepts a number and prints that many asterisks.


def drawLeftStars(num):
    spaceChar = ''
    for x in range(num):
        spaceChar += "*"
    return spaceChar



# print(drawLeftStars(7))
# print(drawLeftStars(33))
# print(drawLeftStars(63))
print("_________________________")


def drawRightStars(num):
    spaceChar = ''
    for x in range(75-num):
        spaceChar += " "
    for x in range(num):
        spaceChar += "*"
    return spaceChar

# print(drawRightStars(7))
# print(drawRightStars(33))
# print(drawRightStars(63))

print("_________________________")


def drawCenteredStars(num):
    spaceChar = ''
    for x in range(int((75-num)/2)):
        spaceChar += " "
    for x in range(num):
        spaceChar += "*"
    # int always runs down 
    print(int(35.8))
    return spaceChar

# print(drawCenteredStars(7))
# print(drawCenteredStars(33))
# print(drawCenteredStars(63))

print("_________________________")
'''Create threesFives() that adds values from 100 and 4000000 (inclusive) if that value is evenly
divisible by 3 or 5 but not both. Display the final sum in the console. '''

def threeFives():
    sum = 0
    for x in range(100, 4000001):
        if (x % 3 == 0 or x % 5 ==0) and not (x % 3 == 0 and x % 5 ==0):
            sum += x
    return f"Sum is {sum}"

# print(threeFives())
print("_________________________")

'''
Make generateCoinChange(cents). Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).
''' 

def generateCoinChange(num):
    quarter, dime, nickel, penny, remainder = 0, 0, 0, 0, 0
    for x in range(num):
        quarter = num // 25
        remainder = num % 25
        dime = remainder // 10
        remainder = remainder % 10
        nickel = remainder // 5
        remainder = remainder % 5
        penny = remainder // 1
        remainder = remainder % 1
    return quarter, dime, nickel, penny
        

# print(generateCoinChange(94))
# print(generateCoinChange(500))
# print(generateCoinChange(27))
print("_________________________")

def change(amount, units={100: 'dollars' , 50: 'half-dollar', 25: 'quarter', 10: 'dime', 5: 'nickel', 1: 'penny'}):
    quantities = dict()
    # value is they key
    # name is the value
    for value, name in units.items():
        # print("this the value for key:\n",value, "\nthis is the name for value:\n", name)
        quantities[name], amount = divmod(amount, value)
        if not amount:
            break

    return quantities

# print(change(45461))
print("_________________________")

'''
Write a function that console.logs the number 1, then "chick", then "boom", then "chick", then 2,
then "chick", "boom", "chick" – continuing the same cycle for each number up to (including) 12.
'''

def chickBoom(num): 
    while num < 12:
        print()


# print(chickBoom(12))



print("_________________________")

# how many times queries match to he string
# def matchingStrings(strings, queries):
#     matches = dict()
#     results = []
    
#     # looping through strings
#     for string in strings:
#         # looping through queries
#         for query in queries:
#             # if string matches the query
#             if string == query:
#                 # print("---->",string, query)
#                 # if key exists
#                 if string in matches.keys():
#                     # add to value
#                     matches[query] += 1
#                     # else if it doesn't match add key
#                 else: #don't need this line because we made keys before this for loop
#                     # make value equal to 1
#                     matches[query]= 1     
#         matches[query] = 0
        
        
#         # didn't need an else -> WHY!!!
#             # else if no match equal to 0
#             # else:
#             #     matches[]
#                 # matches[string] =0 #makes everything 0

#     print("Matches List---->", matches)



# matchingStrings(['yah', 'aba', 'aba', 'shm', 'shm','yah' ], ['kng', 'aba', 'yah', 'shm'])


def matchingStrings(strings, queries):
    matches = dict()
    results = []
    
    # looping through strings
    for query in queries:
        matches[query] = 0
        # looping through queries
        for string in strings:
            # if string matches the query
            if string == query:
                # print("---->",string, query)
                # if key exists
                if string in matches.keys():
                    # add to value
                    matches[query] += 1
    for match in matches.values():
        results.append(match)

    print("Matches List---->", matches)
    print(results)


matchingStrings(['yah', 'aba', 'aba', 'shm', 'shm','yah' ], ['kng', 'aba', 'yah', 'shm', 'lte', 'hsd'])