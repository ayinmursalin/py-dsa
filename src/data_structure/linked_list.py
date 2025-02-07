class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def __str__(self):
        return "Node(data: {}, prev: {}, next: {})".format(self.data, self.prev.data if self.prev else None, self.next.data if self.next else None)


class LinkedList:
    head: Node | None = None

    def __init__(self):
        self.head = None

    # Insert at head
    def head_insert(self, node: Node):
        if self.head:
            self.head.prev = node
            node.next = self.head

            self.head = node
        else:
            self.head = node

    # Insert at tail
    def tail_insert(self, node: Node):
        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = node
            node.prev = current
        else:
            self.head = node

    # Delete a data
    def delete_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                prev = current.prev
                next = current.next

                if prev:
                    prev.next = next
                if next:
                    next.prev = prev

                current = None

                return True

            current = current.next

        return False
    
    # Get node from a data
    def get_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            
            current = current.next
        
        return None

    def print(self):
        current = self.head
        data_arrays = []
        while current:
            data_arrays.append(current.data)
            current = current.next

        print("Data as Array:", data_arrays)


def run():
    linked_list = LinkedList()

    for item in [1, 5, 3, 2, 4]:
        node = Node(item)
        linked_list.tail_insert(node)

    print("------------------------------------------------------------")
    linked_list.print()

    linked_list.head_insert(Node(10))
    print("Head Insert: 10")
    linked_list.print()

    linked_list.tail_insert(Node(7))
    print("Tail Insert: 7")
    linked_list.print()

    linked_list.head_insert(Node(6))
    print("Head Insert: 6")
    linked_list.print()

    linked_list.delete_data(5)
    print("Delete Data: 5")
    linked_list.print()
    
    node = linked_list.get_node(4)
    print("Get node of a data: 4")
    print("Node:", node)
    
    node = linked_list.get_node(6)
    print("Get node of a data: 6")
    print("Node:", node)
    print("------------------------------------------------------------")
