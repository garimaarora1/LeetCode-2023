# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
"""      
Explanation from discuss section:
If the track is 100m long, your speed is 10m/s, your friend's speed is 5m/s. Then after 20s, you've run 200m, your friend has run 100m. But because the track is circular, so you will be at the same place with your friend since the difference between your distances is exactly 100m.

How about we change another track, change the speed of you and your friend? As long as your speeds are not the same, the faster person will always catch up with the slower person again.

https://leetcode.com/problems/linked-list-cycle/discuss/1829768/JavaScript-Easy-to-understand-slow-and-fast-pointers-detailed-explanation
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        

        
        
"""      
Explanation from discuss section:
If the track is 100m long, your speed is 10m/s, your friend's speed is 5m/s. Then after 20s, you've run 200m, your friend has run 100m. But because the track is circular, so you will be at the same place with your friend since the difference between your distances is exactly 100m.

How about we change another track, change the speed of you and your friend? As long as your speeds are not the same, the faster person will always catch up with the slower person again.
"""