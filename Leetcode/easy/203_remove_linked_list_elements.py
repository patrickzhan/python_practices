# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Create a dummy node to handle edge cases like deleting the head node.
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the list.
        while current.next:
            if current.next.val == val:
                # Skip the node with the target value.
                current.next = current.next.next
            else:
                # Move to the next node if the value does not match.
                current = current.next

        # Return the new head (skipping the dummy node).
        return dummy.next
