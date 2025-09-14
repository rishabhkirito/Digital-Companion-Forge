class Node:
    def __init__(self,Data):
        self.data = Data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def connection(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("->".join(elements)+"-> None")

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node   
        


my_list = LinkedList()
my_list.connection(10)
my_list.connection(11)
my_list.connection(7)
my_list.display()
my_list.reverse()
print("reversed List")
my_list.display()
