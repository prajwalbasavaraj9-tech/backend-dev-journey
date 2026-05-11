# DLL (insert_at_end) -> append (head & Tail)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None # Shortcut to the end
        
    def append(self, data):
        new_node = ListNode(data)
        
        # Case 1: List is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # Case 2: List has elements (O(1) operation)
        else:
            new_node.prev = self.tail # Link new node back to current tail
            self.tail.next = new_node # Link current tail forward to new node
            self.tail = new_node      # Move tail label to the new end node
            
    def display(self):
        if not self.head:
            print("DLL is empty")
        else:
            current = self.head
            while current:
                print(current.val, end = " <-> " if current.next else "")
                current = current.next
            print()

# Usage remains the same
my_list = DLL()
my_list.append(13)
my_list.append(25)
my_list.append(37)
my_list.display()

# New Complexity Analysis:
# Time Complexity (TC): O(1) - No loop required!
# Space Complexity (SC): O(1)