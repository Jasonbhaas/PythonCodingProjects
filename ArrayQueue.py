class AQueue:
    def __init__(self, _size):
        self.data = [None] * _size
        self.head = 0
        self.tail = 0
        self.queue_size = _size ### len(self.data)
        self.element_count = 0  ### tail - head
    
    def enqueue(self, value):
        if self.tail + 1 == self.queue_size:
            self.IncreateSize()
        
        self.data[self.tail] = value
        self.element_count += 1
        self.tail += 1

    def dequeue(self):
        value = self.data[self.head]
        self.head += 1
        self.element_count -= 1

        if self.element_count < self.queue_size / 4 and self.element_count != 0:
            self.DecreaseSize()
        
        return value

    def IncreateSize(self):
        new_queue = [None] * (self.queue_size * 2)
        j = 0
        for i in range(self.head, self.tail):
            new_queue[j] = self.data[i]
            j += 1
        
        self.data = new_queue
        self.head = 0
        self.tail = j
        self.queue_size = self.queue_size * 2    

    def DecreaseSize(self):
        new_queue = [None] * int(self.queue_size / 2)
        j = 0

        for i in range(self.head, self.tail):
            new_queue[j] = self.data[i]
            j += 1
        
        self.data = new_queue
        self.head = 0
        self.tail = j
        self.queue_size = int(self.queue_size / 2)

    def HowMany(self):
        return self.element_count

