#!python
# This link helped me a lot to understand stacks: https://www.codesdope.com/course/data-structures-stacks/

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        # if the head of the stack is none, then the stack is gonna be empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.size
    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        # if the list is empty we need to prepend
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Empty Stack")
        else:
            item = self.list.head.data
            self.list.head = self.list.head.next
            # the size is going to decrease by 1
            self.list.size -= 1
            return item
# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.is_empty():
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[len(self.list) - 1]
    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Empty Stack")
        else:
            item = self.peek()
            self.list.pop(len(self.list) - 1)
            return item

Stack = LinkedStack
# Stack = ArrayStack
