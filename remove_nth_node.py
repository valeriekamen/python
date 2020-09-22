"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def add_to_end_of_list(l: ListNode, val: int):
    last_node = go_to_end_of_list(l)
    new_node = ListNode(value=val)
    last_node.next = new_node


def remove_node(prev_node: ListNode, node_to_remove: ListNode):
    new_next = node_to_remove.next
    prev_node.next = new_next


def go_to_end_of_list(l: ListNode) -> ListNode:
    node = l
    if not node:
        return node
    while node.next:
        node = node.next
    return node


def print_list_and_give_length(l: ListNode) -> int:
    node = l
    length_list = 1
    if not l.next:
        print(l.value)
        return length_list

    while node.next:
        print(node.next.value)
        node = node.next
        length_list += 1

    return length_list


def make_range_list(start, end) -> ListNode:
    root = ListNode()
    for i in range(start, end):
        add_to_end_of_list(root, i)

    print("ORIGINAL LEN", print_list_and_give_length(root))
    return root


def go_to_position_from_end_and_remove(l: ListNode, pos: int) -> ListNode:
    # determine length of list
    # then go out to that point (pos is from end)
    # remove that node
    length_list = print_list_and_give_length(l)
    pos_from_start = length_list - pos
    prev_node = None
    node = l
    for i in range(pos_from_start):
        prev_node = node
        node = node.next
    remove_node(prev_node, node)
    print("FINAL LEN", print_list_and_give_length(l))


root = make_range_list(1, 6)
go_to_position_from_end_and_remove(root, 2)
