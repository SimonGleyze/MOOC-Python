# An iterative "Pythonic" search procedure
def search(list, element):
    for e in list:
        if e == element:
            return True
    return False

# A recursive search procedure
def rSearch(list,element):
    if element == list[0]:
        return True
    if len(list) == 1:
        return False
    return rSearch(list[1:],element)

#A recursive "Pythonic" binary search procedure
def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list)/2
    if list[mid] > element:
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        return rBinarySearch( list[mid : ] , element)
    return True

# Class of cartesian coordinate
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'

# Class of integers
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        temp_inter = []
        inter = intSet()
        for i in self.vals:
            for j in other.vals:
                if i == j:
                    temp_inter.append(i)
        for k in temp_inter:
            inter.insert(k)
        return inter

    def __len__(self):
        count = 0
        for i in self.vals:
            count += 1
        return count

# Class of elements in a queue
class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        if len(self.vals) == 0:
            raise ValueError()
        else:
            result = self.vals[0]
            del self.vals[0]
            return result

# Generator of prime numbers
def genPrimes():
    prime2 = 2
    former_num = [1, 2]
    count = 0
    prime = 3
    yield prime2
    while True:
        former_num += [prime]
        for num in former_num:
            if (former_num[-1] % num) != 0:
                count += 1
        if count == (len(former_num)-2):
            yield former_num[-1]
            prime += 1
            count = 0
        else:
            prime += 1
            count = 0