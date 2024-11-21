# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1_head:ListNode, list2_head: ListNode) -> ListNode:
        # List to temporarily store the values
        vec=[]
        # Pushing the values of a linked list
        while list1_head:
            vec.append(list1_head.val)
            list1_head = list1_head.next

        # Pushing the values of b linked list
        while list2_head:
            vec.append(list2_head.val)
            list2_head = list2_head.next

        # Sorting the list
        vec.sort()

        # Creating a new list with sorted values
        temp = ListNode(-1)
        head = temp
        for value in vec:
            temp.next = ListNode(value)
            temp = temp.next
        head = head.next

        # Returning the resultant linked list
        return head