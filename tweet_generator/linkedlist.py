#!python

from __future__ import print_function
import sys


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)

            # result.append(current)
            current = current.getNext()
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""

        # # TODO: count number of items
        # pass
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        current = self.head
        new = Node(item)
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new)
        else:
            self.head = new

        if new.getNext() == None:
            self.tail = new


    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # # TODO: prepend given item
        # pass
        new = Node(item)
        new.setNext(self.head)
        self.head = new
        if new.getNext() == None:
            self.tail = new


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # # TODO: find given item and delete if found
        # pass
        current = self.head
        previous = None
        goal = False
        if current:
            while not goal:
                if current.getData() == item:
                    goal = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.head = current.getNext()
                if current.getNext() == None:
                    self.tail = current.getNext()
            else:
                previous.setNext(current.getNext())
                if previous.getNext() == None:
                    self.tail = previous
        else:
            raise ValueError("Could not find value to delete.")

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # # TODO: find item where quality(item) is True
        # pass
        current = self.head
        goal = False
        while current != None and not goal:
            if quality(current.getData()):
                goal = True
            else:
                current = current.getNext()
        if goal:
            return current.getData()
        else:
            return None
        # return quality(self.head.getData())


def test_linked_list():
    ll = LinkedList()
    print(ll)

    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))

    print(ll.length())
    print(ll.find(lambda item: item == 'B'))

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())



if __name__ == '__main__':
    test_linked_list()
