class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


root = Node()


def add_node_recursive(node, new_node):
    if not node.next:
        node.next = new_node
        return

    if node.next.value > new_node.value:
        new_node.next = node.next
        node.next = new_node
        return

    add_node_recursive(node.next, new_node)


def add_node(node, new_node):

    while node.next:
        if new_node.value < node.next.value:
            new_node.next = node.next
            node.next = new_node
            return
        
        node = node.next
        
    node.next = new_node

def print_the_things(node):
    print(node.value)
    
    if node.next:
        print_the_things(node.next)


add_node_recursive(root, Node(25))
add_node_recursive(root, Node(17))
add_node_recursive(root, Node(100))

print_the_things(root)

    # while True:
    #     if not node.next:
    #         node.next = new_node
    #         break
    #     node = node.next


    # for n in node:
    #     if not n.next:
    #         n.next = new_node
    #         return
    #     n = n.next
    