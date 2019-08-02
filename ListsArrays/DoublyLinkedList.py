import threading


class DoubleLinkedListNode(object):
    def __init__(self, next, previous, key):
        self.next = next
        self.previous = previous
        self.key = key


class DoubleLinkedList(object):
    def __init__(self, max_size, key):
        # root of the circular doubly linked list
        self.head = DoubleLinkedListNode(None, None, key)
        # each linked list entry wil go [previous, next, key]
        # LRU Protocol, the head is the most recently used, head.previous is the least recently used
        self.node_lookup = {}  # to allow for quick lookup
        self.node_lookup[key] = self.head
        self.max_size = max_size
        self.size = 0

    def Move_To_Front(self, key):
        # Link should already exists, so we will move it to the front of the list
        node = self.node_lookup[key]
        if node is not None:
            if node != self.head:  # if node is already at the front, no need to change
                previous_node, next_node = node.previous, node.next
                previous_node.next = next_node
                next_node.previous = previous_node
                last_node = self.head.previous
                last_node.next = self.head.previous = node
                node.previous = last_node
                node.next = self.head
                self.head = node
        else:
            raise KeyError

    def Add_To_List(self, key):
        node = self.node_lookup.get(key)
        if node is not None:  # no eviction required, just call Track
            self.Track(key)
            return None
        elif self.size < self.max_size:  # List is not at capacity, eviction not required
            with threading.RLock():
                node = DoubleLinkedListNode(None, None, key)
                last_node = self.head.previous
                last_node.next = self.head.previous = node
                node.previous = last_node
                node.next = self.head
                self.node_lookup[key] = self.head = node
                self.size += 1
                return None
        else:
            # Remove the last element of the list with our new element,
            # and make this new node the head
            with threading.RLock():
                last_node = self.head.previous
                key_to_evict = last_node.key
                last_node.key = key
                self.head = node_lookup[key] = last_node
                del(node_lookup[key_to_evict])
                return key_to_evict

    def Print_List(self):
        PREV, NEXT, KEY = 0, 1, 2  # give names to the indexes
        node = self.head
        # print(node[KEY] + " --> ")
        while node.next != self.head:
            print(node[KEY] + " --> ")
            node = node.next


testList = DoubleLinkedList(10, "First Key")
testList.Add_To_List("Second Key")
testList.Add_To_List("Third Key")
testList.Add_To_List("Fourth Key")
testList.Add_To_List("Fith Key")
testList.Add_To_List("Sixth Key")

testList.Print_List()
