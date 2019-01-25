class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        next_str = "None"
        if self.next:
            next_str = self.next.value
        return self.value + "Next: " + next_str

def reverse_sublist (L, start , finish): 
    dummy_head = sublist_head = Node(0, L)
    for i in range(1, start):
        sublist_head = sublist_head.next

    # Reverses sublist

    sublist_iter = sublist_head.next 
    for i in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next , temp.next , sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next

Node5 = Node(2)
Node4 = Node(7, Node5)
Node3 = Node(5, Node4)
Node2 = Node(3, Node3)
Node1 = Node(11, Node2)

reversed_list = reverse_sublist(Node1, 2, 4)
print(reversed_list.next.value)
