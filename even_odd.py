"""
Input:  5 -> 1 -> 3 -> 7 -> 3 -> X  
Output: 5 -> 3 -> 3 -> 1 -> 7 -> X 
Explanation: All the even index nodes go first, followed by the odd. The relative ordering of the nodes is maintained.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> X
Output: 1 -> 3 -> 5 -> 2 -> 4 -> X

"""
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def add_new_node_to_end(self, value):
        new_node = Node(value)
        this_node = self.head
        if not this_node.next:
            this_node.next = new_node
        else:
            while this_node.next:
                this_node = this_node.next

            this_node.next = new_node

    def print_list_and_len(self):
        this_node = self.head
        len_list = 0

        while this_node:
            print("Pos", len_list, ":", this_node.value)
            if not this_node.next:
                return len_list
            this_node = this_node.next
            len_list += 1

    def make_list_even_then_odd(self, total_rounds, start_node=0):
        rounds = total_rounds
        start = start_node
        node = self.head

        if rounds == 0:
            self.print_list_and_len()
            return

        # go out to one before start node
        for i in range(0, start_node):
            node = node.next

        # move that node to end of list
        while node.next.next:
            move_node = Node(node.next.value)
            node.next = node.next.next

            if node.next.next:
                move_node.next = node.next.next
            else:
                move_node.next = None

            node.next.next = move_node
            node = node.next

        self.make_list_even_then_odd(rounds - 1, start + 1)

    def call_even_then_odd(self):
        len_list = self.print_list_and_len()
        self.make_list_even_then_odd(math.floor(len_list / 2))

    def recur(self, node=None):
        this_node = node
        if not node:
            this_node = self.head

        print(this_node.value)
        if this_node.next:
            self.recur(this_node.next)


ll = LinkedList(0)
ll.add_new_node_to_end(1)
ll.add_new_node_to_end(2)
ll.add_new_node_to_end(3)
ll.add_new_node_to_end(4)
ll.add_new_node_to_end(5)
ll.add_new_node_to_end(6)
ll.add_new_node_to_end(7)
ll.add_new_node_to_end(8)
ll.call_even_then_odd()
