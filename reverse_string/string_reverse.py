import sys

def reverse(string):
    reversedStr = ""
    for i in range(len(string)-1, -1, -1):
        reversedStr += string[i]
    return reversedStr

if __name__ == "__main__":
    inputStr = sys.argv[1]
    outputStr = reverse(inputStr)
    print("Original string:", inputStr)
    print("Reversed string:", outputStr)
