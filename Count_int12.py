class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    # iteratively time complexity O(n)

    def count_key(self, key):
        current_node = self.head
        if current_node is None:
            return 0
        count = 0
        while current_node:
            if current_node.data == key:
                count += 1
            current_node = current_node.next
        return count

    def count_key_recursive(self, node, key):

        if node is None:
            return self.counter
        if node.data == key:
            self.counter += 1

        return self.count_key_recursive(node.next, key)


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(1)
    llist.append(1)
    llist.append('E')
    llist.append(1)
    llist.print_list()

    print(llist.count_key_recursive(llist.head, 1))
