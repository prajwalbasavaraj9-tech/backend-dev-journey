# - Remove N^th node from end of list (Brute Force).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # 1. Calculate the total length of the list
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next
    
    # 2. Handle the edge case: Removing the head node
    # If length == n, the node to remove is the head itself
    if length == n:
        return head.next
    
    # 3. Find the position to stop (the node BEFORE the one to be deleted)
    position_to_stop = length - n
    temp = head
    count = 1
    
    while count < position_to_stop:
        temp = temp.next
        count += 1
    
    # 4. Delete the node by skipping it
    # temp.next is the node to be deleted
    temp.next = temp.next.next
    
    return head

# Create the nodes
node7 = ListNode(6)
node6 = ListNode(8, node7)
node5 = ListNode(1, node6)
node4 = ListNode(7, node5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
head = ListNode(1, node2)

# List looks like: 1 -> 3 -> 4 -> 7 -> 1 -> 8 -> 6 -> None

n = 2
new_head = removeNthFromEnd(head, n)

def print_list(node):
    elements = []
    while node:
        elements.append(str(node.val))
        node = node.next
    print(" -> ".join(elements) + " -> None")

print_list(new_head)
# Output: 1 -> 3 -> 4 -> 7 -> 1 -> 6 -> None

# Time Complexity (TC): O(L) 2 Passes
# Space Complexity (SC): O(1)