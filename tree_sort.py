class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_item_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def make_into_tree(self, tree):
        current = self.head
        while current:
            print('make tree', current.value)
            tree.add_to_tree(current.value, None)
            current = current.next
        tree.print_tree_in_order()


class Tree:
    def __init__(self):
        self.tree_head = None

    def add_to_tree(self, value, start_node):
        if not self.tree_head:
            print('head is', value)
            self.tree_head = TreeNode(value)
            return

        if not start_node:
            start_node = self.tree_head
        if start_node.value is None or value <= start_node.value:
            if not start_node.left:
                start_node.left = TreeNode(value)
                print('added on left', value)
                return
            else:
                self.add_to_tree(value, start_node.left)
        else:
            if not start_node.right:
                start_node.right = TreeNode(value)
                print('added on right', value)
                return
            else:
                self.add_to_tree(value, start_node.right)

    def print_tree_in_order(self, start_node=None):
        if not start_node:
            start_node = self.tree_head
        if start_node.left:
            self.print_tree_in_order(start_node.left)
        print('its', start_node.value)
        if start_node.right:
            self.print_tree_in_order(start_node.right)

    def print_tree_in_order(self, start_node=None):
        if not start_node:
            start_node = self.tree_head
        if start_node.left:
            self.print_tree_in_order(start_node.left)
        print('its', start_node.value)
        if start_node.right:
            self.print_tree_in_order(start_node.right)


def make_tree_from_ll(linked_list):
    tree = Tree()
    current = linked_list.head
    while current:
        print('make tree', current.value)
        tree.add_to_tree(current.value, None)
        current = current.next
    tree.print_tree_in_order()
    tree.make_tree_into_ll()
    return tree


def make_ll_from_tree(tree, new_ll, start_node=None):
    if not start_node:
        start_node = tree.tree_head
    if start_node.left:
        make_ll_from_tree(tree, new_ll, start_node.left)
    new_ll.add_item_to_end(start_node.value)
    if start_node.right:
        make_ll_from_tree(tree, new_ll, start_node.right)
    new_ll.print_list()


mylist = LinkedList()
mylist.add_item_to_end(5)
mylist.add_item_to_end(15)
mylist.add_item_to_end(7)
mylist.add_item_to_end(6)
mylist.add_item_to_end(9)
mylist.print_list()
mytree = Tree()
mylist.make_into_tree(mytree)
mytree.print_tree_in_order()
new_ll = LinkedList()
make_ll_from_tree(mytree, new_ll)
print('final list in order:')
new_ll.print_list()
