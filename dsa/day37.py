# - Lenght of Loop in LL (Optimized Sol^)

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
            
    def length_loop_optimized(self):
        slow = self.head
        fast = self.head
        
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If pointers meet, there is a loop
            if slow == fast:
                # Step 2: Count nodes in the loop
                count = 1
                slow = slow.next # Move slow forward once to start counting
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        
        return 0 # No loop found

# --- Testing the Logic ---
obj = SLL()
for i in [1, 2, 3, 4, 5, 6]:
    obj.append(i)

# Manually creating a loop for testing:
# Link node '6' back to node '3'
# List: 1 -> 2 -> (3) -> 4 -> 5 -> 6 -> (back to 3)
last_node = obj.head
while last_node.next:
    last_node = last_node.next

loop_entry = obj.head.next.next # This is node 3
last_node.next = loop_entry

# Calculate length
print(f"Loop length is: {obj.length_loop_optimized()}")

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)