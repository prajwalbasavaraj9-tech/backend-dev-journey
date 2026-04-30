# - Reverse A Linked List  (Brute Force Sol^)

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
            
class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

class Solution:
    def reverse_list_brute(self, head: Node) -> Node:
        if not head:
            return None
        
        stack = []
        temp = head
        
        # Pass 1: Push all values onto the stack
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        # Pass 2: Pop values back into the nodes
        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
            
        return head
    
obj = SLL()
for i in [10, 20, 30, 40, 50, 60]:
    obj.Append(i)

sol = Solution()

# FIX: Pass the head node and store the new head returned by the function
new_head = sol.reverse_list_brute(obj.head)

# To see the output, we traverse starting from the new_head
print("Reversed List Output:")
temp = new_head
while temp:
    print(temp.val, end=" -> " if temp.next else "")
    temp = temp.next