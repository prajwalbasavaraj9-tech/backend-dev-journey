# - Lenght of Loop in LL.

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
            
    def lenght_loop(self):
        temp = self.head
        total = 0
        freq = dict()
        
        while temp:
            # We check if the Node object (memory address) exists in freq
            if temp in freq:
                return total - freq[temp]
            freq[temp] = total
            total += 1
            temp = temp.next
        return 0

# --- Execution and Testing ---
obj = SLL()
# Adding unique nodes
vals = [5, 9, 1, 7, 6]
for v in vals:
    obj.append(v)

# To make the code return something other than 0, we MUST create a cycle manually:
# Let's link the last node (6) back to the node with value (9)
last_node = obj.head
while last_node.next:
    last_node = last_node.next

cycle_entry = obj.head.next # This is the node with value 9
last_node.next = cycle_entry # The loop is now: 5 -> 9 -> 1 -> 7 -> 6 -> (back to 9)

print(f"Loop length: {obj.lenght_loop()}")

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)