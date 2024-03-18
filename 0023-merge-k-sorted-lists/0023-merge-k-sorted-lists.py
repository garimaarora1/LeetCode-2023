# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge_two_lists(list1, list2))
            lists = merged_lists
        return lists[0]

    def merge_two_lists(self, list1, list2):
        dummy_node = ListNode()
        merged_list = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                dummy_node.next = list1
                list1 = list1.next
            else:
                dummy_node.next = list2
                list2 = list2.next
            dummy_node = dummy_node.next
        if list1:
            dummy_node.next = list1
        if list2:
            dummy_node.next = list2
        return merged_list.next
        