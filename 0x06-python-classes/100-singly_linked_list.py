#!/usr/bin/python3


class Node:
    """Definng a node"""

    def __init__(self, data, next_node=None):
        """intializes a node
        Args:
            data(int): type int
            next_node(node): type node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of an object"""
        return self.__data

    @property
    def next_node(self):
        """Returns the next node of the nodes"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node obect")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a linked list"""

    def __init__(self):
        """Intialzes the linke dlist"""
        self.head = None

    def sorted_insert(self, value):
        """Sorts out the linkd list in ascending order"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next_node = None
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            temp = self.head
            while(temp.next_node and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Defines the strng attrbutes in the class"""
        val = []
        temp = self.head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(val)
