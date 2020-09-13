class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_new_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            if node.next:
                node = node.next
            node.next = new_node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        int1 = Solution.make_list_into_int(l1)
        int2 = Solution.make_list_into_int(l2)
        print(int1, int2)
        total = int1 + int2
        print('total is', total)
        return Solution.make_int_into_ll(total)

    def make_list_into_int(l):
        str_int = ''
        node = l.head
        while node:
            str_int += str(node.value)
            node = node.next
        return int(str_int)

    def make_int_into_ll(num):
        result = LinkedList()
        for n in str(num)[::-1]:
            result.add_new_node(n)
        teststr = Solution.make_list_into_int(result)
        print(teststr)
        return result

# 253 + 564 = 807 result 7 > 0 > 8


l1 = LinkedList()
l1.add_new_node(2)
l1.add_new_node(4)
l1.add_new_node(3)
l2 = LinkedList()
l2.add_new_node(5)
l2.add_new_node(6)
l2.add_new_node(4)
s = Solution()
s.addTwoNumbers(l1, l2)

