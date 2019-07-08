def reverseList(head):
    first = head  # The node we will (eventually) move tot he back of the list
    old_target = head  # pointer to the front of the list
    new_target = head.next  # the node we are moving to the front
    while(first.next):
        first.next, new_target.next, old_target, new_target = new_target.next, old_target, new_target, new_target.next

    return old_target


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
myList = ListNode(1, node2)

x = reverseList(myList)

print(x.next.val)
