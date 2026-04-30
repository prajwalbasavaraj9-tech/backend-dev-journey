class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# --- Execution ---
# 1. Build the list
my_list = SinglyLinkedList()
for val in [10, 20, 30, 40, 50]:
    my_list.append(val)

# 2. Run the algorithm
test = Solution()
middle = test.middleNode(my_list.head)

print(f"The middle node value is: {middle.val}")

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)