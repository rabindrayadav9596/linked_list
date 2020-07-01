class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# function should insert new node at the
# beigning of the list


def insertAtBegining(a, value):
    # code here
    temp = Node(value)
    if a.head == None:
        a.head = temp
        a.Tail = temp
    else:
        temp.next = a.head
        a.head = temp
    return a.head

# function should insert new node at the
# end of the list


def insertAtEnd(a, value):
    # code here too :)
    temp = Node(value)
    if a.Tail is None:
        a.head = temp
        a.Tail = temp
    else:
        a.Tail.next = temp
        a.Tail = temp
    return a.head
