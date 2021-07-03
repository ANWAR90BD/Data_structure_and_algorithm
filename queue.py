class queue:
    def __init__(self) -> None:
        self.item = []
        pass

    def enqueue(self, add_item):
        self.item.append(add_item)

    def dequeue(self):
        if len(self.item) < 1:
            return None
        return self.item.pop(0)


    def output(self):
        print(self.item)

x = queue()
x.enqueue(10)
x.enqueue(20)
x.enqueue(30)
x.enqueue(40)
x.enqueue(50)

x.output()

x.dequeue()
x.dequeue()

x.output()