import sys

def fib(n):
    if n >= 0 and n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = sys.argv[1]
    print("The",n,"th Fibonacci number is:", fib(int(n)))
