from __future__ import print_function
import argparse

def encrypt(phrase, offset):
    encrypted = ""
    phrase = phrase.lower()

    for char in phrase:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            newChar = chr((ord(char)-ord('a') + offset)%26 + ord('a'))
            encrypted += newChar
        else:
            encrypted += char
    
    return encrypted

def decrypt(phrase, offset):
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', help='Enter the phrase to be encrypted.')
    parser.add_argument('-d', '--decrypt', help='Enter the phrase to be decrypted.')
    parser.add_argument('-o', '--offset', help='Enter the number of characters to use for the offset of the encryption/decryption.')
    parser.add_argument('-t', '--test', help='Run unit tests')

    args = parser.parse_args()
    print(args)
    if args.encrypt is not None:
        if args.offset is not None:
            print(encrypt(args.encrypt, args.offset))
        else:
            print("Error: no offset specified.")
            print("Please use the -o argument to specify the offset for encryption.")

    elif args.decrypt is not None:
        if args.offset is not None:
            print(decrypt(args.decrypt, args.offset))
        else:
            print("Error: no offset specified.")
            print("Please use the -o argument to specify the offset for encryption.")


    # testing
    print(encrypt('Hello, world!', 2))

if __name__ == '__main__':
    main()