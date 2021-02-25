# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string

import sys

def URLify_crude(string):
    letters = list(string)
    newLetters = []

    for letter in letters:
        if letter == " ":
            newLetters.append("%")
            newLetters.append("2")
            newLetters.append("0")
        else:
            newLetters.append(letter)

    return(''.join(newLetters))


if __name__ == "__main__":
  print(sys.argv[-1].replace(" ", "%20"))
  print(URLify_crude(sys.argv[-1])) 

