class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_all_nodes(self):
        current_node = self.head
        while current_node:
            next = current_node.next
            del current_node.data
            #del current_node.next
            current_node = next
            self.head = None
        print("Everything is deleted. sorry to say goodbye")


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    llist.delete_all_nodes()
    llist.print_list()
