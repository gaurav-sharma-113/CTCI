# Given two strings, write a method to decide if one is a permutation of the other.
import sys

def isPermute(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    letters = {}
    
    for letter in str1:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 0
    
    for letter in str2:
        if not letter in letters:
            return False
            
        letters[letter] -= 1
        if letters[letter] == -1:
            del letters[letter]

    return (len(letters) == 0)

if __name__ == "__main__":
    str1 = "Hie"
    str2 = "ieh"
    print(isPermute(sys.argv[-2], sys.argv[-1]))
