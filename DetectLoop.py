class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

# Method 1 : Hare and Tortoise method
    def detect_loop(self):
        tortoise_ptr = self.head
        hare_ptr = self.head
        # if linked list is empty just return politely
        if self.head is None:
            return False
        # move the hare_ptr by 2 node and tortoise_ptr by 1
        # if hare_ptr is None break out of loop
        while hare_ptr and hare_ptr.next:
            tortoise_ptr = tortoise_ptr.next
            hare_ptr = hare_ptr.next.next
            if hare_ptr == tortoise_ptr:
                return True
        return False

# Method2: Hashing *** Traverse the linked list and put the node address in hashtable
# if you reach NULL, return false but if you find the node address again return True
#Time complexity: O(n) as only one traversal of the loop is needed
#Auxiliary space: O(n) n is the space required to store the value in hashmap
    def detect_loop_hashing(self):
        node_address_table = set()
        current_node = self.head
        if current_node is None:
            return False
        while current_node:
            if current_node in node_address_table:
                return True
            node_address_table.add(current_node)
            current_node = current_node.next
        return False


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = second

print(llist.detect_loop())
