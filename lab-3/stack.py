"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from singly_linked_list import SinglyLinkedList
from link_node import LinkNode
from currency import Currency
from krone import Krone


# Do not use linked list functions in this class
class Stack(SinglyLinkedList):
    
    def __init__(self) -> None:
        super().__init__()

    def push(self, currency: Currency):
        super().add_currency(currency, index=0)

    def pop(self):
        super().remove_currency(0)

    def peek(self):
        return Krone(self._start.data.get_value())  # copy of a Krone object

    def print_stack(self):
        super().print_list()

    def add_currency(self, currency: Currency, index):
        raise NameError("method is not accessible")

    def remove_currency(self, element):
        raise NameError("method is not accessible")

    def find_node(self, currency: Currency):
        raise NameError("method is not accessible")

    def find_currency(self, currency: Currency):
        raise NameError("method is not accessible")

    def get_node(self, index):
        raise NameError("method is not accessible")

    def get_currency(self, index):
        raise NameError("method is not accessible")

    def print_list(self):
        raise NameError("method is not accessible")

    def count_currency(self):
        raise NameError("method is not accessible")
