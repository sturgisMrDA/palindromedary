"""
Dictionary maintenance for palindromes.py
Aaron D.A., July 2017
specify dictionary file and file of words to be removed.
"""
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

WORD_FILE = "shortlist_words.txt" # Filename of dictionary file.
WORD_LIST = load_words(WORD_FILE)
with open("to_remove.txt",'r') as removal_file:
    for line in removal_file:
        remove_from_dict(line.strip())
    removal_file.close()
"""
open the file of words to remove and give it a variable name
for each word in the file,
delete it from the word list variable
then copy the new list back into the file
"""
