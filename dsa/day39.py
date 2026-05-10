# - Remove N^th node from end of list (Optimal Sol^).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Initialize both pointers at the head
    slow = fast = head
    
    # 1. Move fast pointer 'n' steps ahead
    for _ in range(n):
        fast = fast.next
        
    # 2. If fast is None, we need to remove the head node
    if not fast:
        return head.next
        
    # 3. Move both pointers until fast reaches the last node
    # Now they move at the same speed, maintaining the 'n' gap
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    # 4. 'slow' is now at the node BEFORE the one to be deleted
    slow.next = slow.next.next
    
    return head

# Create the nodes: 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)

# n=2 means the second node from the end (which is '2')
new_head = removeNthFromEnd(head, 3)

def print_list(node):
    curr = node
    while curr:
        print(curr.val, end=" -> " if curr.next else " -> None\n")
        curr = curr.next

print_list(new_head)
# Expected Output: 1 -> 3 -> 4 -> 7 -> 1 -> 6 -> None

# Time Complexity (TC): O(L) {single pass + two pointer approach}
# Space Complexity (SC): O(1)