#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
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
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
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
        val = []
        temp = self.head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(val)
