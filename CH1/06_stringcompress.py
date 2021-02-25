# String compression
import sys 

def stringCompress(string):
    compressedString = []
    currentLetter = string[0]
    count = 1
    for letter in string[1:]:
        if letter == currentLetter:
            count += 1
        else:
            compressedString.append(currentLetter+str(count))
            currentLetter = letter
            count = 1
    compressedString.append(currentLetter+str(count))
    return string if len(string) < len(compressedString)*2 else (''.join(compressedString))

if __name__ == "__main__":
    
    print(stringCompress(sys.argv[-1]))