class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        
        newHead= head
        if head.next:
            newHead=self.reverseList(head.next)
            #head.next.next which is now the tail of the reversed call has to be pointed to the head,first node
            head.next.next = head
        head.next = None
        return newHead
        
                
        
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
head = create_linked_list([3,1, 2, 3, 4, 5])
reversed_head = sol.reverseList(head)
print_linked_list(reversed_head)

