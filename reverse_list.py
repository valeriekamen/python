class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_item(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert_item_at_start(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        current = self.head
        print('head', self.head.value)
        while(current):
            print(current.value)
            current = current.next


def reverse_list(input_list):
    reversed_list = LinkedList()
    current = input_list.head
    while current:
        reversed_list.insert_item_at_start(current.value)
        if not current.next:
            break
        current = current.next

    return reversed_list


my_list = LinkedList()
my_list.insert_item(3)
my_list.insert_item(4)
my_list.insert_item(5)
print('original list')
my_list.printLL()
print('reversing')
reversed_list = reverse_list(my_list)
reversed_list.printLL()