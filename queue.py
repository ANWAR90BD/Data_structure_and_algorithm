class queue:
    def __init__(self) -> None:
        self.item = []
        
    def is_empty(self):
        if self.item == []:
            return "This is empty"
        return "This is not empty"

    def enqueue(self, add_item):
        self.item.append(add_item)

    def dequeue(self):
        if len(self.item) < 1:
            return None
        return self.item.pop(0)
    
    def size(self):
        return len(self.item)


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

print(x.size())

print(x.is_empty())





def create_queue():
    item = []
    return item

def is_empty(item):
    if len(item) == []:
        return "This is empty"
    return "This is not empty"

def enqueue(item, value):
    return item.append(value)

def dequeue(item):
    return item.pop(0)

def size(item):
    return len(item)


x = create_queue()
enqueue(x, 10)
enqueue(x, 20)
enqueue(x, 30)
enqueue(x, 40)
enqueue(x, 50)
print(x)

dequeue(x)
dequeue(x)
dequeue(x)
print(x)

print("size is: ",size(x))
print(is_empty(x))
