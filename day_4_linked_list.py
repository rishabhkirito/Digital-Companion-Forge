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
        print("->".join(elements)+"None")

my_list = LinkedList()
my_list.connection(10)
my_list.connection(11)
my_list.connection(7)
my_list.display()
