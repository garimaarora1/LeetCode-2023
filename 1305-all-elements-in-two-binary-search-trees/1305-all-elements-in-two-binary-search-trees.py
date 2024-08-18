# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order_traversal(self, root):
        if not root:
            return []
        return self.in_order_traversal(root.left) + [root.val] + self.in_order_traversal(root.right)

    def merge_sorted_lists(self, list1, list2):
        merged = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Append remaining elements
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        return merged

    def getAllElements(self, root1, root2):
        list1 = self.in_order_traversal(root1)
        list2 = self.in_order_traversal(root2)
        
        return self.merge_sorted_lists(list1, list2)