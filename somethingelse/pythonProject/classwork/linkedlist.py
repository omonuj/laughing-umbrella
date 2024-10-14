class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def pop(self):
        if self.head is None:
            print("List is empty.")
            return None
        if self.head.next is None:
            popped_data = self.head.data
            self.head = None
            return popped_data
        current = self.head
        while current.next.next:
            current = current.next
        popped_data = current.next.data
        current.next = None
        return popped_data

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if count == next:
                return current.data
            count += 1
            current = current.next

        return "Index out of range"

    def reverse_recursive(self):
        self.head = self.reverse_recursive(self.head)

        def reverse_recursive(self, node):
            if not node or not node.next:
                return node
            new_head = self._reverse_recursive(node.next)
            node.next.next = node
            node.next = None
            return new_head
        ...




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None