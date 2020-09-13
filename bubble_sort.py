class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def add_node_to_end(self, value):
        new_node = Node(value)
        current = self.head
        if not current.next:
            current.next = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def bubble_sort(self):
        list_changed = True
        while list_changed:
            list_changed = False
            previous = self.head
            while previous.next.next:
                current = previous.next
                if current.value > current.next.value:
                    temp = current
                    previous.next = current.next
                    if current.next.next:
                        temp.next = current.next.next
                    else:
                        temp.next = None
                    previous.next.next = temp
                    list_changed = True
                previous = previous.next


mylist = LinkedList()
mylist.add_node_to_end(5)
mylist.add_node_to_end(3)
mylist.add_node_to_end(7)
mylist.add_node_to_end(2)
mylist.print_list()
mylist.bubble_sort()
mylist.print_list()
