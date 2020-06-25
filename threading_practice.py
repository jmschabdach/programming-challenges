"""
Jenna Schabdach 2019

Description

Useage:

"""

import threading
import time

class MyThreading(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(self.name, "started")
        time.sleep(1)
        print(self.name, "finished")

def main():
    maxThreads = 10
    count = 0
    repCount = 0
    length = 27
    threads = []

    for i in range(length):
        t = MyThreading("thread-"+str(i).zfill(2))
        threads.append(t)
        t.start()
        count += 1

        if count >= maxThreads:
            print("Max number of threads reached:", len(threads))
            for t in threads:
                t.join()
            threads = []
            print("Reset the list of threads:", len(threads))
            count = 0
        elif i == (length - 1):
            print("Reached last item in for loop")
            print("Threads should be joined here.")
            for t in threads:
                t.join()
            print("Threads were joined")

    print("end of program woo")

if __name__ == "__main__":
    main()