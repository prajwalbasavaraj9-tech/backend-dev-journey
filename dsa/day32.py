# Linked list (SLL) [Append + Traverse + Insert + Delete]

class Node:
    def __init__(self, val):
        self.val = val  # data val
        self.next = None  # pointer 
        
class SLL:
    def __init__(self) -> None:
        self.head = None  # declaration (self.head)

    def Append(self, data):
        new_node = Node(data)
        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def Traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end = " ")
                current = current.next
            print()
            
    def Insert(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            previous_node = None
            count = 0
            while current_node is not None and count < position:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            previous_node.next = new_node
            new_node.next = current_node

    def Delete(self, val):
        current = self.head
        if current.next is not None:
            if current.val == val:
                self.head = current.next
                return
            else:
                found = False
                previous = None
                while current is not None:
                    if current.val == val:
                        found = True
                        break
                    previous = current
                    current = current.next
                
                if found:
                    previous.next = current.next
                    return
                else:
                    print("val Not Found!!!")


Nums_Dict = SLL()
# Append
Nums_Dict.Append(10)
Nums_Dict.Append(20)
Nums_Dict.Append(30)
Nums_Dict.Append(55)
# Traverse
Nums_Dict.Traverse()
# Insert 
Nums_Dict.Insert(40, 3)
Nums_Dict.Insert(60, 5)
# Traverse
Nums_Dict.Traverse()
# Delete
Nums_Dict.Delete(55)
# Traverse
Nums_Dict.Traverse()

# Time Complexity (TC): O(n) # specified w.r.t each func
# Space Complexity (SC): O(1)