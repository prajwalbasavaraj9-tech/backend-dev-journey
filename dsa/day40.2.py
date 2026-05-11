# DLL (insert_at_end) -> append (head only)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = ListNode(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            
    def display(self):
        if not self.head:
            print("DLL is empty")
        else:
            current = self.head
            while current:
                print(current.val, end = " <-> " if current.next else "")
                current = current.next
            print()
       
# Example Usage            
my_list = DLL()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.display()

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)