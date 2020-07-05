class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            return

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        if self.head is None:
            return
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def create_loop(self, n):
        # loopnode is the connecting node to the last node of linked LinkedList
        loop_node = self.head
        for i in range(1, n):
            loop_node = loop_node.next
        # end is the last node of the linked list
        end = self.head
        while end.next:
            end = end.next
        # creating the loop
        end.next = loop_node

    def detect_loop(self):
        if self.head is None:
            return 0
        slow = self.head
        fast = self.head
        flag = 0
        while slow and slow.next and fast and fast.next and fast.next.next:
            if slow == fast and flag != 0:

                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.create_loop(2)
loop_length = llist.detect_loop()
if llist.head is None:
    print("linked list is empty")
else:
    print(str(loop_length))
