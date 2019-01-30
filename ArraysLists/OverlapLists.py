class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        next_str = "None"
        if self.next:
            next_str = str(self.next.value)
        return str(self.value) + "   Next: " + next_str


def Check_For_Overlap(l1, l2):
    head1 = l1
    head2 = l2

    length1 = 1
    length2 = 1

    while l1.next is not None:
        l1 = l1.next
        length1 += 1
    
    while l2.next is not None:
        l2 = l2.next
        length2 += 1

    if l1 is not l2:
        return None
    else:
        if length1 > length2:
            l1 = head1
            l2 = head2
        else:
            l1 = head2
            l2 = head1      #l1 will be the longer of the two
    
    for _ in range(abs(length1 - length2)):
        l1 = l1.next

    while(l1 is not l2):
        l1 = l1.next
        l2 = l2.next
    
    return l1


Node5 = Node(5)
Node4 = Node(4, Node5)
Node3 = Node(3, Node4)
Node2 = Node(2, Node3)
Node1 = Node(1, Node2)

Node_3 = Node(-3, Node4)
Node_2 = Node(-2, Node_3)

intersect = Check_For_Overlap(Node_2, Node1)

if intersect is Node4:
    print("success")
else:
    print("failure")
