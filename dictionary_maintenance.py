"""
Dictionary maintenance for palindromes.py
Aaron D.A., July 2017
Run this program to remove multiple words from the dictionary file
being used with Palindromes.
"""

WORD_FILE = "shortlist_words.txt" # Filename of dictionary file.
REMOVAL_FILE = "to_remove.txt" # Filename with words to be removed from dictionary.

def load_words(file_name):
    """Load the dictionary file and store it in a list"""
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

WORD_LIST = load_words(WORD_FILE)
with open(REMOVAL_FILE,'r') as removal_file:
    for line in removal_file:
        remove_from_dict(line.strip())
    removal_file.close()
