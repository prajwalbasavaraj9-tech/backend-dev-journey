# Traversal Operations

def traverse_forward(self):
    current = self.head
    while current:
        print(current.val, end=" ")
        current = current.next    # Move forward
    print()

def traverse_backward(self):
    current = self.head
    while current.next:        # Go to the last node
        current = current.next
    while current:
        print(current.val, end=" ")
        current = current.prev  # Move backward
    print()
    
def traverse_backward_optimized(self):
    # Start directly at the tail instead of walking from the head
    current = self.tail 
    while current:
        print(current.val, end=" ")
        current = current.prev  # Move backward using the prev pointer
    print()
    
# Time Complexity (TC): O(n)
"""  2 Passes (Head to Tail to Head)  """
""" 1 Pass (Tail to Head)  """
# Space Complexity (SC): O(1)