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

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_at_beginning(head, data):
#     new_node = Node(data)
#     new_node.next = head   # new node points to old head
#     return new_node        # new node becomes the new head

# def display(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# head = None  # start with empty list

# # Insert elements
# head = insert_at_beginning(head, 10)
# print(head)
# head = insert_at_beginning(head, 20)
# display(head)


#-----------------------------------------------------------------------------------------------------------------
#singly linked list
#practice-1 
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3

# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")

# #practice-1 
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3

# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")
        
#doubley linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# node2.prev=node1
# node3.prev=node2
# node4.prev=node3

# current=node1
# while current is not None:
#     print(current.data,end="<-")
#     current=current.next
# print("None")
        
#circular linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None

# node1=Node(100)
# node2=Node(200)
# node3=Node(300)
# node4=Node(400)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node1

# node1.prev=node4
# node2.prev=node1
# node3.prev=node2
# node4.prev=node3

# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
#     if current==node1:
#         break


#insertion at beginning

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def Insert_at_beginning(head,data):
#     new_data=Node(data)
#     new_data.next=head
#     return new_data

# def display(head):
#     current=head
#     while current:
#         print(current.data,end="->")
#         current=current.next
#     print("None")

# head = None
# head = Insert_at_beginning(head,8)
# head = Insert_at_beginning(head,18)
# head = Insert_at_beginning(head,80)
# display(head)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def Add_beginning(head,data):
#     new_data=Node(data)
#     new_data.next=head
#     return new_data

# def display(head):
#     current=head
#     while current:
#         print(current.data,end="->")
#         current=current.next
#     print("None")
# head = None
# head = Add_beginning(head,5)
# head = Add_beginning(head,50)
# head = Add_beginning(head,500)
# display(head)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None

# node1=Node(1)
# node2=Node(2)
# node3=Node(3)

# node1.next=node2
# node2.next=node3
# node3.next=node1

# node1.prev=node3
# node2.prev=node1
# node3.prev=node2


# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
#     if current==node1:
#         break
# print("None")


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None

# node1=Node(1)
# node2=Node(2)
# node3=Node(3)

# node1.next=node2
# node2.next=node3
# node3.next=node1

# node1.prev=node3
# node2.prev=node1
# node3.prev=node2


# def add_beginning(head,data):
#     new_node=Node(data)
#     new_node.next=head
#     return new_node

# def display(head):
#     current=node1
#     while current is not None:
#         print(current.data,end="->")
#     print("None")

# head=None
# head = add_beginning(20)
# head = add_beginning(30)
# head = add_beginning(40)
# display(head)

#aad atvthe specific
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def insert_at_position(head, data, position):
#     new_node = Node(data)

#     # Case 1: Insert at beginning
#     if position == 1:
#         new_node.next = head
#         return new_node

#     # Case 2: Insert at any other position
#     current = head
#     count = 1
#     while current and count < position - 1:
#         print("count",count,"position",position)
#         current = current.next
#         count += 1

#     if not current:
#         print("Position out of range")
#         return head

#     new_node.next = current.next
#     current.next = new_node
#     return head

# def display(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# head = None

# # Creating initial list: 10 -> 20 -> 30
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# print("Original List:")
# display(head)

# # Insert 25 at position 3
# head = insert_at_position(head, 25, 3)

# print("After inserting 25 at position 3:")
# display(head)

# #insert at end
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_at_end(head, data):
#     new_node = Node(data)

#     # Case 1: If list is empty
#     if head is None:
#         return new_node

#     # Case 2: Traverse to the last node
#     current = head
#     while current.next:   # move until last bogie
#         current = current.next

#     # Link last node to new node
#     current.next = new_node
#     return head


# def display(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# head = None

# # First node
# head = insert_at_end(head, 10)

# # Add more nodes
# head = insert_at_end(head, 20)
# head = insert_at_end(head, 30)
# head = insert_at_end(head, 40)

# display(head)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def insert_at_specific_node(head,data,position):
#     new_node = Node(data)

#     if position == 1:
#         new_node.next = head
#         new_node.next=head
#         return new_node
#     currnet = head
#     count = 1
#     while currnet and count< position -1:
#         currnet = currnet.next
#         count += 1

#     if not currnet:
#         print("Position out of range")
#         return head
    
#     new_node.next = currnet.next
#     currnet.next = new_node
#     return head


    
# def display(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# head = None

# # # Creating initial list: 10 -> 20 -> 30
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# print("Original List:")
# display(head)

# # Insert 25 at position 3
# head = insert_at_specific_node(head, 200, 1)
# display(head)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def add_specific_position(head,data,position):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        new_node.next = head
        return new_node
    
    Current = head
    count = 1
    while Current and count < position - 1:
        Current = Current.next
        count += 1
    
    if not Current:
        print("Position out of range")
        return head
    
    new_node.next = Current.next
    Current.next = new_node
    return head
