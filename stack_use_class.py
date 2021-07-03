class stack:
    def __init__(self) -> None:
        self.item = []
        pass

    def insert(self, value):
        self.item.append(value)
    
    def delet(self):
        if len(self.item) < 1:
            return None
        return self.item.pop()
    
    def output(self):
        print(self.item)
    

x = stack()
x.insert(10)
x.insert(20)
x.insert(30)
x.insert(40)
x.insert(50)

x.output()


x.delet()
x.delet()
x.delet()

x.output()