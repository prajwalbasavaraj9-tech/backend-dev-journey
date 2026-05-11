# Insert in btw（⊙ｏ⊙）

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        """O(1) Insertion at the end using Tail"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at(self, val, position):
        """O(n) Insertion in between"""
        if position == 0:
            self.insert_at_head(val)
            return

        new_node = Node(val)
        current = self.head
        count = 0

        # Traverse to the node just BEFORE the target position
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next: # If we are not inserting at the very end
            current.next.prev = new_node
        else: # If we are inserting at the end, update the tail
            self.tail = new_node
            
        current.next = new_node

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" <-> ".join(elements) if elements else "Empty List")

dll = DoublyLinkedList()
dll.append(5)   # Index 0
dll.append(10)  # Index 1
dll.append(9)   # Index 2
dll.append(4)   # Index 4 (shifted later)
dll.append(1)   # Index 5

print("Before insertion:")
dll.display() # 5 <-> 10 <-> 9 <-> 4 <-> 1

# Inserting 100 at position 3 
dll.insert_at(100, 3)

print("After inserting 100 at index 3:")
dll.display() # 5 <-> 10 <-> 9 <-> 100 <-> 4 <-> 1

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)