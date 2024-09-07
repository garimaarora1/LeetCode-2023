# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
                
        def dfs(root, head):
            if head == None:
                return True
            if not root:
                return False
            
            if root.val != head.val:
                return False
            
            return dfs(root.left, head.next) or dfs(root.right, head.next)
        
        def check_path(root, head):
            if not root:
                return False
            if dfs(root, head):
                return True
            return check_path(root.left, head) or check_path(root.right, head)
        

        
        return check_path(root, head)
        

         