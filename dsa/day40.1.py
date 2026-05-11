# DLL (insert_at_head)

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            # Connect the new node to the current head
            new_node.next = self.head
            # Point current head's back-pointer to the new node
            self.head.prev = new_node
            # Move the head pointer to the new node
            self.head = new_node

    def display(self):
        if not self.head:
            print("DLL is empty!!")
        else:
            current = self.head
            while current:
                print(current.val, end = "<->" if current.next else "")
                current = current.next
            print()
        
# 1. Initialize the list
dll = DoublyLinkedList()

# 2. Insert elements
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)

# 3. Print the results
# The list should look like: 30 <-> 20 <-> 10
dll.display()

# 4. Verify bidirectional link
print(f"Head value: {dll.head.val}")           
print(f"Next after head: {dll.head.next.val}")    
print(f"Back to head: {dll.head.next.prev.val}")

# Time Complexity (TC): O(1)
# Space Complexity (SC): O(1)