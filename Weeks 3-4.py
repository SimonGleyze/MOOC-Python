#Iterative Power : base^exp
def iterPower(base, exp):
    x = 1
    while exp > 0:
        x *= base
        exp -= 1
    return x

#Recursive multiplication
def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

#Factorial
def factR(n):
    if n == 1:
        return n
    return n * factR(n-1)

#Recursive Iterative Power, V1
def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * recurPower(base, exp-1)

#Recursive Iterative Power, V2
def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    return base * recurPowerNew(base, exp - 1)

#GCD using Iteration
def gcdIter(a ,b):
    x = min(a, b)
    while x > 0:
        if (a%x == 0 and b%x == 0):
            return x
        else:
            x -= 1

#GCD using Recursion
def gcdRecur(a, b):
    if min(a, b) == 0:
        return max(a, b)
    elif max(a, b)%min(a, b) == 0:
        return min(a, b)
    return gcdRecur(max(a, b), max(a, b)%min(a, b))

#Towers of Hanoi
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def towers(n, fr, to, spare):
    '''
    :param n: number of discs
    :param fr: from
    :param to: to
    :param spare: spare
    '''
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

#Fibonacci
def fib(x):
    assert type(x)==int and x >= 0
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)

#Palindrome
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'azertyuiopqsdfghjklmwxcvbn':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#Length
def lenIter(aStr):
    x = 0
    for c in aStr:
        if c in 'azertyuiopqsdfghjklmwxcvbn':
            x += 1
    return x

def lenRecur(aStr):
    if aStr == '':
        return 0
    else:
        return lenRecur(aStr[0:-1]) + 1

#Is char in a string?
import math
def isIn(char, aStr):
    if aStr == '':
        return False
    elif aStr == char:
        return True
    else:
        if char < aStr[len(aStr)/2]:
            return isIn(char, aStr[:int(math.floor(len(aStr)/2.0))])
        else:
            return isIn(char, aStr[int(math.ceil(len(aStr)/2.0)):])

#Semordnilap
def semordnilap(str1, str2):
    if str1[::-1] == str2:
        return True
    return False

def semordnilap(str1, str2):
    if str1 == '' and str2 == '':
        return True
    elif len(str1) != len(str2):
        return False
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])

#Fibonacci with Global Variable
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    for i in range(n+1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

#Gather Divisors in a Tuple
def findDivisors(n1, n2):
    divisors = ()   #empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors += (i,)
    return divisors

#PGCD
max(findDivisors(n1, n2))

#Function that only keeps odd elements in a tuple
def oddTuples(aTup):
    result = ()
    for j in range(0, len(aTup)):
        if j%2 == 0:
            result += (aTup[j],)
        else:
            result += ()
    return result

#Function that removes duplicates in a list
def removeDups(L1, L2):
    L1Start = L1[:]
    for i in L1Start:
        if i in L2:
            L1.remove(i)

#Mapping
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

#How many elements in a Dictionary
def howMany(aDict):
    elem = 0
    for i in aDict:
        elem += len(aDict[i])
    return elem

#The key of the biggest element in a dictionary
def biggest(aDict):
    result = []
    if aDict == {}:
        return None
    else:
        for i in aDict:
            result += [len(aDict[i])]
    return aDict.keys()[result.index(max(result))]

#Counting digits
def ndigits(x):
    y = str(x)
    return len(y)

import math
count = 0
def ndigits(x):
    global count
    if math.floor(x) == 0:
        result = count
        count = 0
        return result
    else:
        count += 1
        return ndigits(abs(x)/10)

#Radiation Exposure
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    def frange(start, stop, step):
        while start < stop:
            yield start
            start += step
    x = 0
    for num in frange(start, stop, step):
        x += step * f(num)
    return x

#Python Loves Fruits
def nfruits(dict, meal):
    for i in meal[0:-1]:
        for j in dict:
            if i == j:
                dict[j] -= 1
            else:
                dict[j] += 1
    for i in meal[-1]:
        for j in dict:
            if i == j:
                dict[j] -= 1
    result = max(dict, key=dict.get)
    return dict[str(result)]
