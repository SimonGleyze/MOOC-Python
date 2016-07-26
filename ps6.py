import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') returns
    True
    #>>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict_lowercase = {}
        dict_uppercase = {}
        for letter in string.ascii_lowercase:
            dict_lowercase[str(letter)] = str(letter)
        for letter in string.ascii_uppercase:
            dict_uppercase[str(letter)] = str(letter)
        copy_keys_lowercase = dict_lowercase.keys()[:]
        copy_keys_uppercase = dict_uppercase.keys()[:]
        copy_shift = shift
        for keys_lowercase in sorted(copy_keys_lowercase):
            dict_lowercase[str(keys_lowercase)] = str(sorted(copy_keys_lowercase)[shift])
            shift += 1
            if shift > 25:
                shift = 0
        for keys_uppercase in sorted(copy_keys_uppercase):
            dict_uppercase[str(keys_uppercase)] = str(sorted(copy_keys_uppercase)[copy_shift])
            copy_shift += 1
            if copy_shift > 25:
                copy_shift = 0
        dict = {}
        for elem_lowercase in dict_lowercase:
            dict[str(elem_lowercase)] = dict_lowercase[str(elem_lowercase)]
        for elem_uppercase in dict_uppercase:
            dict[str(elem_uppercase)] = dict_uppercase[str(elem_uppercase)]
        return dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        original = self.get_message_text()[:]
        cipher = ''
        for letter in original:
            if letter in alphabet:
                cipher += self.build_shift_dict(shift)[str(letter)]
            else:
                cipher += str(letter)
        return cipher

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.text = str(text)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.build_shift_dict(self.shift)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.shift)[:]

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        combinations = {}
        eval = {}
        counting_words = 0
        for i in range(26):
            temp = PlaintextMessage(self.get_message_text(), i)
            combinations["try{0}".format(i)] = temp.get_message_text_encrypted().split()
        for key in combinations.keys():
            for word in combinations[str(key)]:
                if is_word(self.get_valid_words(), str(word)):
                    counting_words += 1
            eval[format(key)] = counting_words
            counting_words = 0
        if len(eval.keys()[eval.values().index(max(eval.values()))]) == 4:
            decrypted_message = PlaintextMessage(self.get_message_text(),
                                                 int(eval.keys()[eval.values().index(max(eval.values()))][-1]))
            result = (int(eval.keys()[eval.values().index(max(eval.values()))][-1]),
                      str(decrypted_message.get_message_text_encrypted()))
            return result
        else:
            decrypted_message = PlaintextMessage(self.get_message_text(),
                                                 int(eval.keys()[eval.values().index(max(eval.values()))][-2:]))
            result = (int(eval.keys()[eval.values().index(max(eval.values()))][-2:]),
                      str(decrypted_message.get_message_text_encrypted()))
            return result

# Decrypt a Story
def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()
