#Testing whether an integer is a multiple of 2
x = int(raw_input("Enter an integer: "))
if x % 2 == 0:
    print ("")
    print ("Even")
else:
    print("")
    print ("Odd")
print ("Done with conditional")

#Squaring an integer
x = int(raw_input("Enter an integer: "))
ans = 0
itersLeft = x
while itersLeft != 0:
    ans = ans + x
    itersLeft = itersLeft - 1
print (str(x) + "*" + str(x) + "=" + str(ans))

#Sum from 1 to end
end = int(raw_input("Enter an integer: "))
x = 1
y = 0
while x <= end:
    y += x
    x += 1
print(y)

#Test for cube roots
x = int(raw_input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans += 1
#    print (abs(x) - ans**3) #Decrementing function
if ans**3 != abs(x):
    print (str(x) + " is not a perfect cube.")
else:
    if x < 0:
        ans = -ans
    print ("Cube root of " + str(x) + " is " + str(ans))


#Sum from 1 to end
end = int(raw_input("Enter an integer: "))
x = 1
y = 0
for x in range(1,end+1):
    y += x
    x += 1
print(y)

#Binary form
num = int(raw_input("Enter an integer: "))
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result
print result

#Square root of x
x = int(raw_input("Enter an integer: "))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses +=1
print ('numGuesses = ' + str(numGuesses))
if abs(ans**2 - x) >= epsilon:
    print ('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))

#Square root of x bisection
x = int(raw_input("Enter an integer: "))
epsilon = 0.001
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))

#Secret code
print("Please think of a number between 0 and 100!")
low = 0.0
high = 99
ans = round((high + low)/2.0)
print ('Is your secret number ' + str(ans) + ' ?')
print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
           " Enter 'c' to indicate I guessed correctly.")
y = str(raw_input(""))
while y != 'c':
    if y == 'h':
        high = ans
    elif y == 'l':
        low = ans
    else:
        print ('Sorry, I did not understand your input.')
    ans = round((high + low) / 2.0)
    print ('Is your secret number ' + str(ans) + ' ?')
    print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
           " Enter 'c' to indicate I guessed correctly.")
    y = str(raw_input(""))
print ('Game over. Your secret number was: ' + str(ans))

#Newton-Raphson algo
x = int(raw_input("Enter an integer: "))
epsilon = 0.01
guess = x/2.0
while abs(guess**2 - x) >= epsilon:
    guess -= ((guess**2 - x)/(2*guess))
print('Square root of ' + str(x) + ' is about ' + str(guess))

#Procedure for iterative power
def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

#Procedure for squaring
def square(x):
    result = x**2
    return result

#Problem
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns: (lo < hi)
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    result = min(max(max(x,lo),min(x,hi)),hi)
    return result

#Fourth power
def fourthPower(x):
    result = square(x)*square(x)
    return result

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    for char in ['a', 'e', 'i', 'o', 'u']:
        if str(char) == str(a) or str(e) or str(i) or str(o) or str(u):
            result = "True"
        else:
            result = "False"
    return result

#Polysum exercise
import math     #Importing the package for the tangent function and pi
def area(n,s):
    '''
    :param n: number of sides
    :param s: length of each side
    :return: area of the regular polygon
    '''
    x = (.25 * n * s**2) / math.tan(math.pi / n)
    return x
def perimeter(n,s):
    '''
     :param n: number of sides
     :param s: length of each side
     :return: perimeter of the regular polygon
    '''
    y = n * s
    return y
def polysum(n,s):
    '''
     :param n: number of sides
     :param s: length of each side
     :return: sum the area and square of the perimeter of the regular polygon
    '''
    z = area(n,s) + perimeter(n,s)**2
    return round(z,4)

#Counting Vowels
s = 'word'
x = 0
for char in s:
    if char in 'aeiouAEIOU':
        x += 1
    else:
        x += 0
print('Number of vowels: ' + str(x))

#Counting Bobs
s = 'azcbobobegghakl'
y = len(s)
x = 0
num_bob = 0
b = 'bob'
set1 = set(b.split(' '))
for num in range(x,y+1):
    z = s[x-1:num+2]
    set2 = set(z.split(' '))
    if z == b:
        num_bob += 1
    else:
        num_bob += 0
    x += 1
print('Number of times bob occurs is: ' + str(num_bob))

#Counting and Grouping
order = "salad water hamburger salad hamburger"
def item_order(order):
    x = order.count('salad')
    y = order.count('water')
    z = order.count('hamburger')
    return('salad:' + str(x) + ' hamburger:' + str(z) + ' water:' + str(y))

#Paying the Minimum
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
remainingBalance = balance
x = 0
y = 0
for num in range(x,12):
    print('Month: ' + str(x+1))
    minimumMonthlyPayment = monthlyPaymentRate * remainingBalance
    print ('Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2)))
    newbalance = remainingBalance - minimumMonthlyPayment
    remainingBalance = newbalance + (annualInterestRate / 12.0) * newbalance
    print ('Remaining balance: ' + str(round(remainingBalance, 2)))
    x += 1
    y += minimumMonthlyPayment
print ('Total paid: ' + str(round(y, 2)))
print ('Remaining balance: ' + str(round(remainingBalance, 2)))

#Paying Debt Off in a Year
balance = 3926
annualInterestRate = 0.2
import math
remainingBalance = balance
x = 0
y = 0
z = 0
test = 0
while test < balance and remainingBalance > 0:
    if x < 12:
        for num in range(x,12):
            minimumMonthlyPayment = test
            newbalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = newbalance + (annualInterestRate / 12.0) * newbalance
            x += 1
            y += minimumMonthlyPayment
            z += remainingBalance
        test += 0.01
    else:
        remainingBalance = balance
        x = 0
        y = 0
        z = 0
        for num in range(x, 12):
            minimumMonthlyPayment = test
            newbalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = newbalance + (annualInterestRate / 12.0) * newbalance
            x += 1
            y += minimumMonthlyPayment
            z += remainingBalance
        test += 0.01
lowestPayment = math.ceil(minimumMonthlyPayment/10.0)*10.0
print ('Lowest Payment: ' + str(int(lowestPayment)))

#Paying Debt Off in a Year with Bisection
balance = 320000
annualInterestRate = 0.2
remainingBalance = balance
epsilon = 0.01
x = 0
low = balance / 12.0
high = (balance * (1 + (annualInterestRate/12.0))**12)/12.0
test = (low + high)/2.0
while abs(remainingBalance) >= epsilon:
    if x < 12:
        for num in range(x, 12):
            minimumMonthlyPayment = test
            newbalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = newbalance + (annualInterestRate / 12.0) * newbalance
            x += 1
    else:
        test = (low + high) / 2.0
        remainingBalance = balance
        x = 0
        for num in range(x, 12):
            minimumMonthlyPayment = test
            newbalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = newbalance + (annualInterestRate / 12.0) * newbalance
            x += 1
    if remainingBalance > 0:
        low = test
    else:
        high = test
    test = (low + high) / 2.0
print ('Lowest Payment: ' + str(round(minimumMonthlyPayment, 2)))