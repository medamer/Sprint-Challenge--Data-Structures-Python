class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.size = len(self.queue)
        self.next = None
        self.head = None
        self.tail = None

    def append(self, item):
        if self.head is None:
            self.queue.append(item)
        elif self.size < self.capacity:
            item
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item

    def get(self):
        if self.head == -1:
            print([])
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i])
            print()
        else:
            for i in range(self.head, self.capacity):
                print(self.queue[i])
            for i in range(0, self.tail + 1):
                print(self.queue[i])
            print()
            