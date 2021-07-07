class Node:
    def __init__(self, data= "Head", next = None):
        self.data = data
        self.next = next

class linked:
    def __init__(self):
        self.head = Node()

    def insert(self,data):
        node = Node(data, self.head.next)
        self.head.next = node

    def get_length(self):
        count = 0
        current_node = self.head.next
        while current_node != None:
            count += 1
            current_node = self.head.next
        return count

    def print_insert(self):
        if self.head.next is None:
            print("This is empty")
            return
        current_node = self.head
        cur_str = ""
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next
        print(cur_str)



    def insert_at(self, location, data):
        if location < 0 or location > self.get_length():
            print("Invalid location")
            return
        if location == 0:
            node = Node(data, self.head.next)
            self.head.next = node
            return
        
        count = 0
        current_node = self.head
        while current_node != None:
            if count == location -1:
                node = Node(data, current_node.next)
                current_node = current_node.next
                break
            current_node = current_node.next
            count += 1

if __name__ == '__main__':
    ll = linked()
    ll.insert_at(1, 10)
    ll.insert_at(2, 20)
    ll.insert_at(3, 30)
    ll.print_insert()