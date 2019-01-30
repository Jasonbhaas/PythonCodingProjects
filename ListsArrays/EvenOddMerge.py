class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        next_str = "None"
        if self.next:
            next_str = str(self.next.value)
        return str(self.value) + "   Next: " + next_str

def Even_Odd_Merge(L):
    first_node = L
    last_even = L
    odd_sublist_tail = L.next
    if L.next is None or L.next.next is None:
        return L
    
    while(odd_sublist_tail and odd_sublist_tail.next):
        last_even.next, odd_sublist_tail.next.next, odd_sublist_tail.next = odd_sublist_tail.next, last_even.next, odd_sublist_tail.next.next

        last_even, odd_sublist_tail = last_even.next, odd_sublist_tail.next

    return first_node


node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)

#merged = Even_Odd_Merge(node0)

merge_len_one = Even_Odd_Merge(node5)
merge_len_two = Even_Odd_Merge(node4)

print("hello")
#print(merged)

