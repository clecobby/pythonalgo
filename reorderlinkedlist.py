import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: 'ListNode'=None):
        self.val = val
        self.next = next

    # utility for easier debugging/printing
    def __repr__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"


class Solution:
    def reorderList(self, head: ListNode) -> None:
       





def list_to_linkedlist(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---- Quick test ----
if __name__ == "__main__":
    sol = Solution()

    head = list_to_linkedlist([1, 2, 3, 4])
    sol.reorderList(head)
    print(linkedlist_to_list(head))  # Expected: [1, 4, 2, 3]

    head = list_to_linkedlist([1, 2, 3, 4, 5])
    sol.reorderList(head)
    print(linkedlist_to_list(head))  # Expected: [1, 5, 2, 4, 3]
