class Node:
    __data = 0
    __next_node = None
    def __init__(self, data, next_node=None):
        if not isinstance(data, int) and data is not None:
            raise TypeError("data must be an integer")
        elif not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.data = data
            self.next_node = next_node

    def data(self):
        return self.data

    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.data = value

    def next_node(self):
        return self.next_node

    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.next_node = value


class SinglyLinkedList:
    __head = None

    def __init__(self):
        self.head = None
    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            if self.head is not None:
                current = self.head
            else:
                current = Node()
            while current:
                if current.data <= value:
                    if current.next_node != None:
                        new.next_node(current.next_node)
                    current.next_node(new)
