class Solution:
    def find_val(self, root):
        return root.val if root else 0

    def sumEvenGrandparent(self, root):
        if not root:
            return 0
        
        q = deque([root])
        total_sum = 0
        
        while q:
            curr = q.popleft()
            
            if curr.val % 2 == 0:
                if curr.left:
                    total_sum += self.find_val(curr.left.left) + self.find_val(curr.left.right)
                if curr.right:
                    total_sum += self.find_val(curr.right.left) + self.find_val(curr.right.right)
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        return total_sum
