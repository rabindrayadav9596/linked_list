class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self, current_node):

        if current_node is None:
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_list_iteratively(self):
        current_node = self.head
        prev_node = None
        next_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.print_list(prev_node)

    def reverse_list_recursively(self, head):
        if head is None or head.next is None:
            return head
        ptr = self.reverse_list_recursively(head.next)
        head.next.next = head
        head.next = None
        return ptr


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.print_list(llist.reverse_list_recursively(llist.head))
