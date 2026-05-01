# - Reverse A Linked List (Optimal Sol^)

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
    def reverse_list_optimal(self, head: Node) -> Node:
        temp = head
        prev = None
        
        while temp:
            front = temp.next    # 1. Save next node
            temp.next = prev     # 2. Reverse current pointer
            prev = temp          # 3. Move prev forward
            temp = front         # 4. Move temp forward
            
        return prev  # prev is the new head of the reversed list

obj = SLL()
for _ in [1,2,3,4,5]:
    obj.Append(_)

test = Solution()
curr = test.reverse_list_optimal(obj.head)
while curr:
    print(curr.val, end = " -> " if curr.next else "\n")
    curr = curr.next

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)