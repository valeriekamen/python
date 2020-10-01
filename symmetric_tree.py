class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_to_tree(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        node = self.root
        while True:
            if not node.left:
                node.left = new_node
                break
            elif not node.right:
                node.right = new_node
                break

            node = node.left

    def add_list_to_tree(self, list_of_vals):
        for item in list_of_vals:
            self.add_to_tree(item)

    def recur_print(self, node=None):
        if not node:
            return

        if node.left:
            print(node.left.val)
        if node.right:
            print(node.right.val)

        self.recur_print(node.left)
        self.recur_print(node.right)

    def print_tree(self):
        """
        This with recur_print function above prints tree in order of additions
        """
        if not self.root:
            return
        node = self.root
        print(self.root.val)
        self.recur_print(node)

    def check_symmetry_recur(self, list_of_vals, level=1):
        print("in", list_of_vals, level)
        if not list_of_vals:
            return True

        nums_to_check = list_of_vals[:level]

        if not nums_to_check == nums_to_check[::-1]:
            return False

        next_level = level * 2
        return self.check_symmetry_recur(list_of_vals[level:], next_level)

    def check_symmetry_iterate(self, list_of_vals):
        level = 1
        while len(list_of_vals):
            nums_to_check = list_of_vals[:level]

            if not nums_to_check == nums_to_check[::-1]:
                return False

            list_of_vals = list_of_vals[level:]
            level *= 2

        return True


t = Tree()
# t.add_list_to_tree([1, 2, 2, 3, 4, 4, 3])
# t.add_list_to_tree([1, 2, 2, "null", 3, "null", 3])
# t.print_tree()
# print(t.check_symmetry([1, 2, 2, 3, 4, 4, 3]))

assert t.check_symmetry_recur([1, 2, 2, 3, 4, 4, 3])
assert not t.check_symmetry_recur([1, 2, 2, "null", 3, "null", 3])

assert t.check_symmetry_iterate([1, 2, 2, 3, 4, 4, 3])
assert not t.check_symmetry_iterate([1, 2, 2, "null", 3, "null", 3])
