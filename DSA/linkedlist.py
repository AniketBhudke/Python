# from platform import node


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.name=None
        
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node2.name="aniket"
# print(node2.name)

# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")
    
#insertion and deletion in linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     # Insert at end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:   # move till last node
#             current = current.next
#         current.next = new_node

#     # Insert after a specific node value
#     def insert_after(self, prev_data, data):
#         current = self.head
#         while current and current.data != prev_data:
#             current = current.next
#         if not current:
#             print("Node not found")
#             return
#         new_node = Node(data)
#         new_node.next = current.next
#         current.next = new_node

#     # Print list
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
# # Create LinkedList object
# ll = LinkedList()

# # Insert elements
# ll.insert_at_end(10)
# ll.insert_at_end(20)
# ll.insert_at_end(30)

# # Print list
# ll.display()   # Output: 10 -> 20 -> 30 -> None

# ll.insert_at_end(45)
# ll.display()
# # Insert at beginning
# ll.insert_at_beginning(5)
# ll.display()   # Output: 5 -> 10 -> 20 -> 30 -> None

# # Insert after a specific node (after 20)
# ll.insert_after(20, 25)
# ll.display()   # Output: 5 -> 10 -> 20 -> 25 -> 30 -> None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head   # new node points to old head
    return new_node        # new node becomes the new head

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = None  # start with empty list

# Insert elements
head = insert_at_beginning(head, 10)
print(head)
head = insert_at_beginning(head, 20)
display(head)
