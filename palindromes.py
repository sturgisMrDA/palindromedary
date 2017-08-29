"""
Palindromedary: Palindrome Generator
Copyright (C) 2017  Aaron Dunigan-AtLee

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
WORD_FILE = "shortlist_words.txt" # Filename of dictionary file to be used.

class Palindrome:
    """
    The Palindrome class; includes a text string,
    a stub (the part of the text that is an incomplete
    word), and whether the stub is on the right or the left.
    """
    def __init__(self, text, stub, add_to_right):
        self.text = text
        self.stub = stub
        self.add_to_right = add_to_right
    def list_words(self):
        """ List words including stub. """
        return self.text.split()
    def is_complete(self):
        """ True if stub is a word. """
        return (self.stub in WORD_LIST)
    def length(self):
        """ Number of words including stub. """
        return len(self.list_words())
    
def reverse(word):
    """ Return a string with its characters reversed. """
    return word[::-1]

def load_words(file_name):
    """ Load the dictionary file and store it in a list """
    words =[]
    with open(file_name,"r") as word_file:
        for line in word_file:
            words.append(line.strip())
        word_file.close()
    return words

def remove_from_dict(word):
    """ Remove word from the dictionary file. """
    global WORD_LIST
    if word in WORD_LIST:
        WORD_LIST.remove(word)
        with open(WORD_FILE,"w") as word_file:
            word_file.write('\n'.join(WORD_LIST))
            word_file.close()
    else:
        print('"' + word +'"' + ' is not in the dictionary.')

def partitions(palindrome):
    """
    Generates a list of palindromes, containing all partitions of
    the stub of palindrome
    """
    parts = [palindrome]
    word = palindrome.stub
    if palindrome.add_to_right:
        for i in range(1,len(word)):
            if word[:i] in WORD_LIST:
                # Create a new palindrome by removing the stub and replacing it
                # with its partition.
                new_stub = word[i:]
                new_text = ' '.join(palindrome.list_words()[:-1]) \
                           + ' ' + word[:i] + ' ' + new_stub
                new_pal = Palindrome(new_text, new_stub, True)
                if new_pal.is_complete():
                    print(new_pal.text)
                    out_file.write(new_pal.text + '\n')
                    dromes.append(new_pal)
                elif new_pal.length() < MAX_LENGTH:
                    parts += partitions(new_pal)
    else: # i.e. palindrome adds to left
        for i in range(len(word)-1,0,-1):
            if word[i:] in WORD_LIST:
                # Create a new palindrome by removing the stub and replacing it
                # with its partition.
                new_stub = word[:i]
                new_text = new_stub + ' ' + word[i:] + ' ' \
                           + ' '.join(palindrome.list_words()[1:])
                new_pal = Palindrome(new_text, new_stub, False)
                if new_pal.is_complete():
                    print(new_pal.text)
                    out_file.write(new_pal.text + '\n')
                    dromes.append(new_pal)
                elif new_pal.length() < MAX_LENGTH:
                    parts += partitions(new_pal)
    # Shuffle to avoid really repetitive output.
    random.shuffle(parts)
    return parts

def extend(palindrome):
    """
    Extend a palindrome by finding words in
    the dictionary that complete its stub.
    Return a list of all palindromes that extend it.
    """
    global dromes
    old_stub = palindrome.stub
    extensions = []
    if palindrome.add_to_right:
        # Generate 'extenders' that complete the stub:
        extenders = [word for word in WORD_LIST if word.startswith(old_stub)]
        # For each one, reflect it and create a new palindrome
        for extender in extenders:
            new_stub = reverse(extender[len(old_stub):])
            new_text = new_stub + ' ' \
                       + ' '.join(palindrome.list_words()[:-1]) \
                       + ' ' + extender
            new_pal = Palindrome(new_text, new_stub, False)
            if new_pal.is_complete():
                print(new_pal.text)
                out_file.write(new_pal.text + '\n')
                dromes.append(new_pal)
            elif new_pal.length() < MAX_LENGTH:
                extensions.append(new_pal)
                
    else: # i.e. add to left
        # Generate 'extenders' that complete the stub:
        extenders = [word for word in WORD_LIST if word.endswith(old_stub)]
        random.shuffle(extenders)
        # For each one, reflect it and create a new palindrome
        for extender in extenders:
            new_stub = reverse(extender[:len(extender)-len(old_stub)])
            new_text = extender + ' ' \
                       + ' '.join(palindrome.list_words()[1:]) \
                       + ' ' + new_stub
            new_pal = Palindrome(new_text, new_stub, True)
            if new_pal.is_complete():
                print(new_pal.text)
                out_file.write(new_pal.text + '\n')
                dromes.append(new_pal)
            elif new_pal.length() < MAX_LENGTH:
                extensions.append(new_pal)
     
    return extensions

def palindrome_search(pal_list):
    """
    Return all extensions of all partitions
    of each palindrome in a list
    """
    new_list = []
    for pal in pal_list:
        for drome in partitions(pal):
            new_list += extend(drome)
    random.shuffle(new_list)
    return new_list

def choose_from_seed(seed):
    """
    Allow user to choose an initial palindrome based on their given seed.
    """
    seed_length = len(seed)
    # Find the positions (pivots) at which the seed could be reflected.
    # e.g., 'omelette' could be reflected as 'omelette lemo...' (pivot at 4)
    # or 'omelette ttelemo...' (pivot at 7)
    left_pivots = [0] + [x for x in range(seed_length) \
                   if seed[:x] == seed[x-1::-1]]
    right_pivots = [(seed_length-x) for x in range(seed_length) \
                  if seed[x:] == seed[:x-1:-1]] + [0]
    # Create list of palindrome starters using the pivots.
    pals = []
    for x in right_pivots:
        stub_length = seed_length - x
        stub = reverse(seed[:stub_length])
        text = seed + ' ' + stub 
        pals.append(Palindrome(text, stub, True))
    for x in left_pivots:
        stub_length = seed_length - x
        stub = reverse(seed[len(seed)-stub_length:])
        text = stub + ' ' + seed
        pals.append(Palindrome(text, stub, False))
    message = 'Using that seed, the palindrome could center around any of these:'
    print(message)
    for i, pal in enumerate(pals):
        print(str(i+1) + '.  ...' + pal.text + '...')
    choice = 0
    while True:
        try:
            message = 'Choose a number from 1 to ' + str(len(pals)) + ': '
            choice = int(input(message))
            if choice <= 0:
                raise ValueError
            pal = pals[int(choice-1)]
            break
        except (ValueError, IndexError):
            print('Not a valid selection. Please try again.')
    return pal
    
    
def begin_palindrome():
    """
    Set up an initial palindrome from a seed word.
    """
    global out_file
    seed = input("Give a seed word for the palindrome: ")
    initial_pal = choose_from_seed(seed)
    out_filename = seed + "_dromes.txt"
    out_file = open(out_filename,"w")
    out_file.write("Seed: " + seed + "\n")
    return initial_pal

def set_max_length():
    """
    Set max number of words in a palindrome (to avoid infinite recursion).
    """
    print('What is the maximum number of words you want in a palindrome?')
    print('(Careful!  Things can get out of hand quickly...)')
    while True:
        try:
            max_words = int(input('Max words: '))
            break
        except ValueError:
            print('Try again...')
    return max_words
 
# Main code.
WORD_LIST = load_words(WORD_FILE) 
dromes =[]
pal = begin_palindrome()
MAX_LENGTH = set_max_length()
print('Generating palindromes from "...' + pal.text + '...":')
pal_list = [pal]
while len(pal_list) > 0:
    pal_list = palindrome_search(pal_list)
out_file.close()
print("Done.")


