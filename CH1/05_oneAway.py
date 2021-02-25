# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

import sys

def isOneAway(str1, str2):
    diffLen = abs(len(str1) - len(str2))
    if diffLen > 1:
        return False
    elif diffLen == 0:
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
                if count > 1:
                    return False
        return True
    else:
        shift = 0
        if len(str1) > len(str2):
            shorter, longer = str2, str1
        else:
            shorter, longer = str1, str2
        print(shorter, longer)
        for i in range(len(shorter)):
            if shorter[i] != longer[i+shift]:
                if shift or (shorter[i] != longer[i + 1]):
                    return False
                shift = 1
        return True

if __name__ == "__main__":
    print(isOneAway(sys.argv[-1], sys.argv[-2]))

