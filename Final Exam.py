def dict_invert(dict):
    new_dict = {}
    list_keys = []
    for key in dict.keys():
        if dict[key] in list_keys:
            new_dict[dict[key]] += [key]
        else:
            new_dict[dict[key]] = [key]
        list_keys += [dict[key]]
    for key in new_dict.keys():
        new_dict[key].sort()
    return new_dict


def getSublists(L, n):
    output = []
    L_copy = L[:]
    while len(L_copy[:n]) == n:
        output += [L_copy[:n]]
        L_copy.remove(L_copy[0])
    return output


def longestRun(L):
    output = []
    dict = {}
    sequence = 1
    list_keys = []
    for n in range(2, len(L)):
        output += getSublists(L, n)
    output += [L]
    for item in output:
        for n in range(1, len(item)):
            if item[n] >= item[n-1]:
                sequence += 1
            else:
                break
        if sequence in list_keys:
            dict[sequence] += [item]
        else:
            dict[sequence] = [item]
        list_keys += [sequence]
        sequence = 1
    try:
        return max(dict.keys())
    except ValueError:
        print '1'


class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        self.status = status
        if self.status is 'citizen' or self.status is 'legal_resident' or self.status is 'illegal_resident':
            return
        else:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status


class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        Person.__init__(self, 'Prof. ' + self.name)
        #self.name = 'Prof. ' + Person.__str__(self)
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
            return self.name + ' says: It is obvious that ' + Professor.lecture(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Professor.lecture(self, stuff)
