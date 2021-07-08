class Node_02:
    def __init__(self, data="Head", next=None):
        self.data = data
        self.next = next
    
class linked_02:
    def __init__(self):
        self.head = Node_02()
    
    def append_at_begining_02(self, data):
        node_02 = Node_02(data, self.head.next)
        self.head.next = node_02
    
    def print_linked_02_list(self):
        if self.head.next is None:
            print("This is empty")
            return
        
        current_node_02 = self.head
        cur_str = ""
        
        while current_node_02 != None:
            cur_str = cur_str + str(current_node_02.data) + " --> "
            current_node_02 = current_node_02.next

        print(cur_str)

    def get_length_02(self):
        cnt = 0
        current_node_02 = self.head

        while current_node_02 != None:
            cnt += 1
            current_node_02 = current_node_02.next

        return cnt
    
    def insert_at_02(self, location, data):
        if location<0 or location> self.get_length_02():
            print("Invalid location")
            return

        if self.head.next == None:
            self.append_at_begining_02()
            return
        
        current_node_02 = self.head
        cnt = 0
        while current_node_02 != None:
            if cnt == location - 1:
                node_02 = Node_02(data, self.head.next)
                self.head.next = node_02
                break
            current_node_02 = current_node_02.next
            cnt +=1

    def append_at_end_02(self, data):
        current_node_02 = self.head
        while current_node_02.next:
            current_node_02 = current_node_02.next
        current_node_02.next = Node_02(data, None)
    
    def search_02(self, search_02_item):
        current_node_02 = self.head
        
        while current_node_02 != None:
            if current_node_02.data == search_02_item:
                print("This is found..")
                return
            current_node_02 = current_node_02.next
        print("OOps data not found")

    
    def delete_02(self):
        if self.head.next is None:
            print("This is empty")
            return
        else:
            current_node_02 = self.head
            while current_node_02.next.next is not None:
                current_node_02 = current_node_02.next
            current_node_02.next = None
        
         

if __name__ == "__main__":
    ll = linked_02()
    ll.append_at_begining_02(100)
    ll.append_at_begining_02(200)
    ll.append_at_begining_02(300)
    ll.print_linked_02_list()
    ll.append_at_end_02(400)
    ll.append_at_end_02(50)
    ll.print_linked_02_list()
    ll.search_02(10)
    ll.delete_02()
    ll.print_linked_02_list()
    
    
    ll.get_length_02()
    ll.insert_at_02(1, 500)
    ll.print_linked_02_list()