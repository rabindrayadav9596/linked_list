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
            count += 1
            current_node = current_node.next
        return count

    def nth_node_from_end(self, num):
        # calculate the position from start with the help of length
        length = self.count_length()
        position = length-num

        count_from_start = 0
        current_node = self.head

        # testing edge cases
        if current_node is None or num > length:
            return
        while current_node and count_from_start != position:
            current_node = current_node.next
            count_from_start += 1
        print(current_node.data)


# time complexity O(n)

    def nth_node_from_end_two_ptr(self, n):
        # creating two pointer main and reference
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        # move reference pointer to n position
        while count != n:
            ref_ptr = ref_ptr.next
            count += 1
        # move both pointer until reference pointer points to NULL
        while ref_ptr:
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next
        print("answer is: ")
        print(main_ptr.data)


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append('C')
    llist.append('D')
    llist.print_list()
    # print(llist.count_length())
    llist.nth_node_from_end_two_ptr(2)
