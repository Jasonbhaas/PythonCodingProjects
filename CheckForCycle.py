class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        next_str = "None"
        if self.next:
            next_str = str(self.next.value)
        return str(self.value) + "   Next: " + next_str

def check_for_cycle(N):
    dummy_head = Node(0, N)

    slow = dummy_head.next
    fast = dummy_head.next.next
    counter = 1

    while(slow != fast):
        if counter % 2 == 0:
            slow = slow.next

        fast = fast.next
        if not fast:
            return None
        
        counter += 1
    
    ## fast == slow
    fast = fast.next
    head_start = dummy_head.next

    while (fast != slow):
        fast = fast.next
        head_start = head_start.next
    
    lag_behind = dummy_head
    loop_begin_position = 0
    while (head_start != lag_behind):
        lag_behind = lag_behind.next
        head_start = head_start.next
        loop_begin_position += 1
    
    return lag_behind

node6 = Node(6)
node5 = Node(5, node6)
node4 = Node(4, node5)
node3 = Node(3, node4)
node6.next = node3
node2 = Node(2, node3)
node1 = Node(1, node2)

loop_start = check_for_cycle(node1)

if loop_start:
    print(loop_start)