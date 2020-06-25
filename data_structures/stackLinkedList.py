class ListElement():
    def __init__(self, data, nextEl=None):
        self.data = data
        self.nextEl = nextEl

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextEl

    def setNext(self, el):
        self.nextEl = el

class Stack():
    def __init__(self, el=None):
        self.head = el
        if el is None:
            self.size = 0
        else:
            self.size = 1

    def push(self, el):
        # Add an element to the beginning of the list
        # Get the head of the list
        listEl = self.head
        # Make the new element the head of the list
        el.setNext(listEl)
        self.head = el
        self.size += 1

    def pop(self):
        # Get the head of the list
        listEl = self.head
        # Edge case: the list is empty
        if listEl is None:
            # Throw an error
            raise ValueError("The stack is empty.")

        # Reset the head of the list
        self.head = listEl.getNext()
        # Decrement the list size
        self.size -= 1
        # Return the data from the popped element
        return listEl.getData()

    def printHead(self):
        print("The stack contains",self.size,"elements.")
        if self.head is None:
            print("The stack is empty.")
        else:
            print("The last element added to the stack has a value of",self.head.getData())

if __name__ == "__main__":
    # Make a new stack
    stack = Stack()
    stack.printHead()

    # Add an element to the stack
    stack.push(ListElement("First element added"))
    stack.printHead()

    # Add two more elements to the stack
    stack.push(ListElement("Second element added"))
    stack.push(ListElement("Third element added"))
    stack.printHead()

    # Pop the last element from the stack
    val = stack.pop()
    print("Popped:", val)
    stack.printHead()

    # Try to pop three elements from the stack (there are only two in the stack)
    val = stack.pop()
    print("Popped:", val)
    stack.printHead()

    val = stack.pop()
    print("Popped:", val)
    stack.printHead()

    val = stack.pop()
    print("Popped:", val)
    stack.printHead()



