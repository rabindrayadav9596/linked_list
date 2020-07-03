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

    def count_length(self):
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def print_middle(self):
        # calculate the middle index
        length = self.count_length()
        if(length % 2 == 0):
            middle = int(length/2)+1
        middle = int(length/2)
        position = 0
        current_node = self.head
        # checking if the linked list is empty
        if current_node is None:
            return
        # traverse until you reach middle
        while position != middle:
            current_node = current_node.next
            position += 1

        print("middle value is: ")
        print(current_node.data)

    def print_middle_two_ptr(self):
        # pointing both slow and fast to head of the linked list
        slow_ptr = self.head
        fast_ptr = self.head
        # if linked list is empty just return politely
        if self.head is None:
            return
        # move fast pointer skipping one node but slow pointer to just next node
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print("middle value is: ")
        print(slow_ptr.data)


if __name__ == "__main__":
    llist = LinkedList()
    # llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append('D')
    llist.append('E')
    llist.append('F')
    llist.append('G')
    llist.print_list()

    llist.print_middle_two_ptr()
