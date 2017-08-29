Palindromedary: a palindrome generator
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

Form palindromic phrases by the following procedure:
1. Choose a seed word.  For example, 'omelette.'
2. This seed word will form the center of the palindrome, but there are multiple ways to do this.  For example, the center could be:
	... omelette lemo... 
	... omelette ttelemo... (except no word starts that way)
	... omelette ettelemo... (ditto)
Each of these phrases 'pivots' at a different letter.
3. Once you have chosen a pivot, note that one end of the would-be palindrome is an incomplete word (such as 'lemo...' above).   We will call this a 'stub.'  List all the words that can complete this stub (e.g. lemon, lemons, lemonade).
4. For each word that completes the stub, reflect the word around to the other end of the phrase.  For example, if we complete 'omelette lemo...' with 'lemonade,' we now have the text '...edan omelette lemonade,' and '...edan' is the stub.
5. Note that some stubs can be split into complete words and a shorter stub.  '...edan' could also be '...ed an,' so our work-in-progress is:
	'...ed an omelette lemonade ...'
6. Continue this process recursively until the stub is a complete word, in which case the palindrome is a complete phrase (though not necessarily one that makes grammatical sense).

Run the program palindromes.py.  You give the program a seed word and then choose a pivot point.  Then it generates as many palindromes as it can up to the maximum word count.  

You may find the output gets excessive.  Use Ctrl+C to cancel the program.

Enjoy!
  