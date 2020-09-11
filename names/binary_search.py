class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if new_node.value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                return self.right.insert(value)
        elif new_node.value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                return self.left.insert(value)


    def contains(self, target):
        # Check if the LL us empty:
        if not self.value:
            return None
        # Check if the target == the root:
        elif self.value == target:
            return True
        # check if the target smaller than root:
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # check if the target is greater than root:
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        

    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()


    def bft_print(self):
        queue = Queue()
        node = self
        while node:
            if node is None:
                return
            if node is not None:
                print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            node = queue.dequeue()


    def dft_print(self):
        stack = Stack()
        node = self
        while node:
            if node is None:
                return
            if node is not None:
                print(node.value)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)
            node = stack.pop()