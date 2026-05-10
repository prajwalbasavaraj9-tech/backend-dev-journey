# - Segrregate odd & even nodes in LL (leet code 328) (Brute force)

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
    def oddEvenBrute(self, head: Node) -> Node:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        values = []
        
        # Pass 1: Get ODD positions (1st, 3rd, 5th...)
        temp = head
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        # Pass 2: Get EVEN positions (2nd, 4th, 6th...)
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        # Pass 3: Reassign values to the original nodes
        temp = head
        index = 0
        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next
            
        return head
 
# --- Execution ---
obj = SLL()
for i in [8, 7, 1, 5, 6, 4, 9]:
    obj.append(i)

sol = Solution()
sol.oddEvenBrute(obj.head)

# Display Output
curr = obj.head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
    
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)