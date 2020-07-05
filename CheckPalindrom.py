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

    def get_nth_value(self, n):
        current_node = self.head
        count = 1
        if count == n:
            return current_node.data
        while current_node and count != n:
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        return current_node.data

    def check_palindrome(self):
        left = 0
        right = self.count_length()
        current_node = self.head
        if current_node is None or self.count_length() == 1:
            return True
        while left < right:
            left_value = current_node.data
            right_value = self.get_nth_value(right)
            current_node = current_node.next
            right -= 1
            left += 1
            if left_value != right_value:
                return False
        return True


llist = LinkedList()
llist.append('m')
llist.append('a')
llist.append('m')
# llist.append('a')
# llist.append('p')
llist.print_list()
print(llist.count_length())
print(llist.check_palindrome())
