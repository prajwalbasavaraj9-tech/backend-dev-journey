# - Linked List Cycle (leet code 141).

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    def Append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def create_cycle(self, pos):
        if pos == -1 or not self.head:
            return
            
        cycle_target = None
        tail = self.head
        index = 0
        
        while tail.next:
            if index == pos:
                cycle_target = tail
            tail = tail.next
            index += 1
            
        tail.next = cycle_target

class Solution:
    def hasCycle(self, head: Node) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False

# --- Testing ---
obj = SLL()

for val in [1, 2, 3, 4, 5, 6, 2, 3, 4, 6, 5]:
    obj.Append(val)

# Force the cycle
obj.create_cycle(6) 

# Run the test
test = Solution()
res = test.hasCycle(obj.head)

print(res)

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)