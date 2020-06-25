import numpy as np

def findLargestInt(arr):
    # Computational Complexity: O(N)
    largest = 0
    for i in range(len(arr)):
        if arr[i] >= largest:
            largest = arr[i]

    return largest

if __name__ == "__main__":
   size = 20
   arr = np.random.randint(100, size=20)
   print(arr)
   print(findLargestInt(arr))

