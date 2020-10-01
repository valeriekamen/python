class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node_to_end(self, val):
        new_node = Node(val=val)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node


ll = LinkedList()
ll.add_node_to_end(3)
ll.add_node_to_end(4)
