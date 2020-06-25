class ListElement():
    def __init__(data, nextEl=null):
        self.data = data
        self.nextEl = nextEl

    def getData():
        return self.data

    def getNext():
        return self.nextEl

    def setNext(el):
        self.nextEl = el

class SinglyLinkedList():
    def __init__():
        self.head = null
        self.tail = null
        self.size = 0

    def addElement(el, pos=-1):
        # Edge case: insert an element at the beginning of the list (pos=0)
        #    get list head
        #    el.setNext(list head)
        #    self.setHead(el)

        # Edge case: insert an element at the end of the list (pos=-1)
        #    get list head
        #    while listEl.getNext() is not null
        #        get next element
        #    listEl.setNext(el)

        # Main case: insert an element at a given index in the list
        #    listEl = self.head
        #    idx = 0
        #    while listEl.getNext() is not null and idx < pos
        #        get next element
        #        idx += 1
        #    newNextEl = listEl.getNext()
        #    el.setNext(newNextEl)
        #    listEl.setNext(el)

        # self.size += 1

    def removeElement():
        # How do we want to remove an element? By index or by contents?
        # self.size -= 1

    def findElementIdx(value):
        # get list head
        # idx = 0
        # while next element is not null
        #    check the value of the element
        #    if value of the element is desired value
        #        return value, idx
        #    idx += 1
        # return null, -1 # value is not in list

    # need function for setting the head of the list
    def setHead(el):
        # if list head is null
        #    self.head = listEl
        # else
        #    get list head
        #    el.setNext(list head)
        #    self.head = el

    def getSize():
        return self.size
