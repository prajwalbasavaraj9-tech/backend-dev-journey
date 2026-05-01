# - Linked List Cycle 2 (leet code 142).

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
class Solution:
    def linked_list_optimized(self, head: Node) -> Node:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
# Create a list: 1 -> 2 -> 3 -> 4 -> 5
obj = SLL()
for i in [1, 2, 3, 4, 5]:
    obj.append(i)

# Manually create a cycle: 5 points back to 3
# 1 -> 2 -> (3) -> 4 -> 5
#            ^---------|
last_node = obj.head.next.next.next.next # Node 5
cycle_start = obj.head.next.next        # Node 3
last_node.next = cycle_start

# Run your logic
sol = Solution()
entry_node = sol.linked_list_optimized(obj.head)
print(f"Cycle starts at node with value: {entry_node.val}")

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)