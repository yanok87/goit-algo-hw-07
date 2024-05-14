"""Module that implements a max-value search function in AVL tree"""


class Node:
    """AVL tree node"""

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Function to add new node to AVL tree"""
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_max_value(root):
    """Function to find the max value in AVL tree"""
    current = root
    # Keep traversing right until we reach the rightmost leaf node, which will be the biggest value
    while current.right:
        current = current.right
    return current.val


def find_min_value(root):
    """Function to find the min value in AVL tree"""
    current = root
    # Keep traversing left until we reach the leftmost leaf node which is the smallest value
    while current.left:
        current = current.left
    return current.val


def sum_of_values(root):
    """Function to find the sum of all values in AVL tree"""

    if root is None:
        return 0
    else:
        # Recursively calculate sum of values in left and right subtrees
        left_sum = sum_of_values(root.left)
        right_sum = sum_of_values(root.right)
        # Add current node's value to the sum of left and right subtrees
        return root.val + left_sum + right_sum


# Example usage:
root = Node(5)
insert(root, 50)
insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 180)
insert(root, 40)
insert(root, 70)
insert(root, 60)

print("The maximum value in the BST is:", find_max_value(root))
print("The minimum value in the BST is:", find_min_value(root))
print("The sum of all values in the BST is:", sum_of_values(root))
