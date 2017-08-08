"""
Palindrome Generator
by Aaron Dunigan-AtLee
July 2017
"""
import random

class Palindrome:
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
    random.shuffle(extensions) 
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

def begin_palindrome(seed):
    """
    Set up an initial palindrome from a seed word.
    """
    global out_file
    seed = input("Give a seed word for the palindrome: ")
    # from left: [x for x in range(len(a)) if a[:x]==a[x-1::-1]]
    # from right: [(len(a)-x) for x in range(len(a)) if a[x:]==a[:x-1:-1]]
    """
    seed = "cat"
    stub_length = 3 # Indicates number of letters that will be reflected.
    add_to_right = True # Whether stub is on the right (left if False)
    """
    out_filename = seed + "_dromes.txt"
    out_file = open(out_filename,"w")
    out_file.write("Seed: " + seed + "\n")
    if add_to_right:
        stub = reverse(seed[:stub_length])
        text = seed + ' ' + stub
    else:
        stub = reverse(seed[len(seed)-stub_length:])
        text = stub + ' ' + seed
    return Palindrome(text, stub, add_to_right)


MAX_LENGTH = 4 # Max number of words in a palindrome (to avoid infinite recursion).
WORD_FILE = "shortlist_words.txt" # Filename of dictionary file.
WORD_LIST = load_words(WORD_FILE)
 
dromes =[]
pal = begin_palindrome()
print(pal.text)
pal_list = [pal]
while len(pal_list) > 0:
    pal_list = palindrome_search(pal_list)
out_file.close()
print("Done.")


