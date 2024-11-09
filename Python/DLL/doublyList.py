class DNode: 
    def __init__(self, val):
        self.value = val 
        self.next = None
        self.prev = None


class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, val):
        new_node = DNode(val)
        if self.tail is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node

    def delete(self, val):
        runner = self.head
        while runner:
            if runner.value == val:
                if runner.prev:
                    runner.prev.next = runner.next
                if runner.next:
                    runner.next.prev = runner.prev
                if runner == self.head:
                    self.head = runner.next
                if runner == self.tail:
                    self.tail = runner.prev
                return
            runner = runner.next

    def insert_between(self, prev_val, new_val):
        runner = self.head
        while runner: 
            if runner.value == prev_val: 
                new_node = DNode(new_val)
                new_node.next = runner.next
                new_node.prev = runner
                if runner.next:
                    runner.next.prev = new_node 
                runner.next = new_node
                if runner == self.tail:
                    self.tail = new_node
                return
            runner = runner.next

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value, end=" <-> " if runner.next else "\n")
            runner = runner.next