# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

import sys 

def isPalindromePermute(string):
    letters = {}
    for letter in string.replace(" ",""):
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    oddSum = 0
    for count in letters.values():
        oddSum += count % 2
    
    return oddSum <= 1

if __name__ == "__main__":
    str = "Tact Coa"
    print(isPalindromePermute(sys.argv[-1].lower()))