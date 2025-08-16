
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newhead= head
        prev = None
        while(newhead):
            headtemp = newhead.next
            newhead.next= prev
            prev = newhead        
            newhead = headtemp

        return prev
            
            # Helper function to create a linked list from a Python list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Test the code
sol = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = sol.reverseList(head)
print_linked_list(reversed_head)


