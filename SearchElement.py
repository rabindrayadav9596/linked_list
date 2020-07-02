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
        if temp is None:
            return
        while temp:
            print(temp.data)
            temp = temp.next

    # search element iteratively
    def search_element(self, key):
        temp = self.head
        if temp is None:
            return False
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # search element recursively
    def search_element_recursive(self, current_node, key):

        if current_node is None:
            return False
        elif current_node.data == key:
            return True
        else:
            return self.search_element_recursive(current_node.next, key)

    def search(self, key):
        return self.search_element_recursive(self.head, key)


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append('D')
    llist.append('E')
    llist.append('F')
    llist.print_list()
    # print(llist.search_element('F'))
    print(llist.search(1))
