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
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_node(self, position):

        temp = self.head
        # if the position is 0
        if position == 0:
            self.head = temp.next
            temp = None
            return

        position_count = 0
        prev = temp
        while(temp and position_count != position):
            prev = temp
            temp = temp.next
            position_count += 1
        if temp is None:
            print("No item to delete")
            return
        prev.next = temp.next
        temp = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.delete_node(2)
    llist.print_list()
