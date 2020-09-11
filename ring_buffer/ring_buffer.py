class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.pointer = 0
        
    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer +=1
        if self.pointer == self.capacity:
            self.pointer = 0
        

    def get(self):
        return [i for i in self.storage if i != None]

