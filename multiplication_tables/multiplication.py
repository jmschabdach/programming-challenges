import numpy as np

def printMultiplicationTable():
    table = np.zeros((12,12))

    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = (i+1)*(j+1)

    print(table)

def printMultiplicationTableNoLib(n):
    for i in range(1, n+1):
        row = ""
        for j in range(1, n+1):
           row += str(i*j)+"\t"
        print(row)

if __name__ == "__main__":
#    printMultiplicationTable()
    printMultiplicationTableNoLib(12)
