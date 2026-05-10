# - Segrregate odd & even nodes in LL (leet code 328) (Optimal Sol^)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def oddEvenOptimal(self, head: Node) -> Node:
        # Base case: if list has 0, 1, or 2 nodes, no reordering needed
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        even_head = even # Save this to link back at the end
        
        # Traverse and unweave
        while even and even.next:
            odd.next = odd.next.next    # Point current odd to next odd
            odd = odd.next              # Move odd marker forward
            
            even.next = even.next.next  # Point current even to next even
            even = even.next            # Move even marker forward
            
        # Stitch the two lists together
        odd.next = even_head
        
        return head

# --- Execution ---
# Build list: 8 -> 7 -> 1 -> 5 -> 6 -> 4 -> 9
vals = [8, 7, 1, 5, 6, 4, 9]
head = Node(vals[0])
curr = head
for v in vals[1:]:
    curr.next = Node(v)
    curr = curr.next

sol = Solution()
new_head = sol.oddEvenOptimal(head)

# Display result
curr = new_head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
    
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)