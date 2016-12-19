"""This is the module for doubly-linked lists methods."""
# encoding: utf-8


class DLLNODE(object):
    """Define the doubly-linked list node class.

    __init__(): instantiates an instance of a node with val, next, and prev.
    """

    def __init__(self, val, next=None, prev=None):
        """Initiate the instance of a node."""
        self.val = val
        self.next = next
        self.prev = prev


class DLL(object):
    """Define the doubly-linked list class.

    __init__(): initializes the DLL class and adds a tail, head, and size_of_list attribute. It also checks that the values passed in are iterable.
    push(): Inserts a value to head of the list
    pop(): Remove node from head of list and return it to user.
    append(): Add a tail to the end of the list.
    shift(): Remove node from end of list and return to user.
    def search(self, val): Return the val of the node when searched.
    remove(): Remove the node passed into the parameter.

    """

    def __init__(self, iterable=None):
        """Instantiate LinkedList class."""
        self.tail = None
        self.head = None
        self.size_of_list = 0
        if iterable and hasattr(iterable, "__iter__") or isinstance(iterable, str):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError("Please submit an iterable when instantiating the list. You can use the push method to add one value at a time.")

    def push(self, val):
        """Insert value to head of the list."""
        new_node = DLLNODE(val, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self.size_of_list += 1

    def pop(self):
        """Remove node from head of list and return it to user."""
        if self.head is None:
            raise IndexError("Impossible to pop an empty list")
        value_popped = self.head.val
        self.head = self.head.next
        if self.size_of_list > 1:
            self.head.prev = None
        if self.head is None:
            self.tail = None
        self.size_of_list -= 1
        return value_popped

    def append(self, val):
        """Add a tail to the end of the list."""
        if self.tail is None:
            self.push(val)
        else:
            new_node = DLLNODE(val)
            self.tail.next = new_node
            self.tail = new_node
            self.size_of_list += 1

    def shift(self):
        """Remove node from end of list and return to user."""
        if self.tail is None:
            raise IndexError("Impossible to shift from an empty list.")
        value_shifted = self.tail.val
        self.tail = self.tail.prev
        if hasattr(self.tail, "next"):
            self.tail.next = None
        self.size_of_list -= 1
        return value_shifted

    def search(self, val):
        """Return the val of the node when searched."""
        current = self.head
        if current is None:
            raise NameError("Parameter given, {}, is not in list".format(str(val)))
        while current:
            if current.val == val:
                return current
            current = current.next
        return current

    def remove(self, node_to_delete):
        """Remove the node passed into the parameter."""
        current_node = self.search(node_to_delete)
        if current_node is self.head:
            self.pop()
        elif current_node is self.tail:
            self.shift()
        elif current_node and current_node.val == node_to_delete:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size_of_list -= 1
        else:
            raise NameError("Parameter given, {}, is not in list".format(node_to_delete))


class Queue(object):
    """Define the Queue class.

    It is important to note that the "tail" of our queue is actually the front of the Queue.

    __init__(): initializes the Queue class as a composite of the DLL class.
    enqueue(): uses the push method from DLL to add nodes to the end of the Queue.
    dequeue(): removes a node from the front of the dequeue
    peek(): Looks at the front value of the Queue without removing it or advancing the view beyond it.
    size(): returns the size of the Queue.
    """

    def __init__(self, iterable=None):
        """Initiate the Queue as an instance of DLL."""
        self._container = DLL(iterable)

    def enqueue(self, val):
        """Add value to the Queue at the end."""
        self._container.push(val)

    def dequeue(self):
        """Remove the first value of the queue."""
        return self._container.shift()

    def peek(self):
        """Look at next value in the Queue without removing."""
        return self._container.tail.val

    def size(self):
        """How big the Queue is."""
        return self._container.size_of_list


def proper_parenthetics(paren_string):
    """The module adds a string, and evals whether the parens line up."""
    new_q = Queue(paren_string)
    if paren_string == "":
        return 0
    if new_q._container.tail.val == ")":
        return -1
    curr = new_q._container.tail
    openit = closeit = 0
    for i in range(new_q._container.size_of_list):
        if curr.val == "(":
            openit += 1
        if curr.val == ")":
            closeit += 1
        if closeit > openit:
            return -1
        curr = curr.prev
    if openit > closeit:
        return 1
    if closeit > openit:
        return -1
    if closeit == openit:
        return 0
