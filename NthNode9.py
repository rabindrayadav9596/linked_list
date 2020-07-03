class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        current_node = self.head
        if current_node is None:
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def getNth(self, position):
        count = 0
        current_node = self.head
        if position == 0:
            return current_node.data
        while current_node and count != position:
            current_node = current_node.next
            count += 1

        if current_node is None:

            return

        return current_node.data


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append('D')
    llist.append('E')
    llist.append('F')
    llist.print_list()
    print("nth value is: ")
    print(llist.getNth(0))
