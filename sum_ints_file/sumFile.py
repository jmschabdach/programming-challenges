import numpy as np

def sumFile(fn):
    sum = 0
   
    # Read all lines from file into a list of strings
    with open(fn, "r") as f:
        lines = f.readlines()

    # Remove all newline characters from the strings
    ints = [line.split("\n")[0] for line in lines]

    # Sum all ints in the list of ints
    for i in ints:
        sum += int(i)
            
    # Print the sum of the ints in the file
    print(sum)

if __name__ == "__main__":
    n = 20 # number of integers to add to a file
    # Generate text file full of ints
    with open("ints.txt", "w") as f:
        for i in range(n):
            f.write(str(np.random.randint(100))+"\n")

    sumFile("ints.txt")
