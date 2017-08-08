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
    print('Generating palindromes from "...' + pal.text + '...":')
    return pal

pal = choose_from_seed("omelette")
