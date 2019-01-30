class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, first_node, last_node=None):
        self.start = Node("Dummy First Node", first_node)
        self.end = last_node

def reverse_sub_list(L, s, f):
    node_before = L
    current_node = L.next
    next_node = current_node.next
    counter = 1

    while(counter < f):
        if counter == s:
            one_before_s = node_before
            s_node = current_node

        if counter > s:
            current_node.next = node_before

        node_before = current_node
        current_node = next_node
        next_node = current_node.next
        counter += 1

    current_node.next = node_before
    one_before_s.next = current_node
    s_node.next = next_node

    return L

Node5 = Node(5)
Node4 = Node(4, Node5)
Node3 = Node(3, Node4)
Node2 = Node(2, Node3)
Node1 = Node(1, Node2)


#reversed_list = reverse_sub_list(Node0, 2, 4)
#print(reversed_list.next.value)



def reverse_linked_list(N):
    dummy_head_node = Node(0, N)

    iter_node = N
    while (iter_node.next):
        temp = iter_node.next
        temp.next, iter_node.next, dummy_head_node.next = dummy_head_node.next, temp.next, temp
    
    return dummy_head_node.next

totally_reversed_list = reverse_linked_list(Node1)

print(totally_reversed_list.value)
print(totally_reversed_list.next.value)
print(totally_reversed_list.next.next.value)
print(totally_reversed_list.next.next.next.value)
print(totally_reversed_list.next.next.next.next.value)





    