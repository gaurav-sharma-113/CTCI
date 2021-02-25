# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import sys

def isUnique(string):
    letters = {}
    for character in string:
        if character in letters:
            return False
        else:
            letters[character] = True
    return True

if __name__ == "__main__":
  print(isUnique(sys.argv[-1]))