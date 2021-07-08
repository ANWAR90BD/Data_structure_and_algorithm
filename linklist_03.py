class Node_03:
    def __init__(self, data="Head", next=None):
        self.data = data
        self.next = next
    
class linked_03:
    def __init__(self):
        self.head = Node_03()
    
    def append_at_begining_03(self, data):
        node_03 = Node_03(data, self.head.next)
        self.head.next = node_03
    
    def print_linked_03_list(self):
        if self.head.next is None:
            print("This is empty")
            return
        
        current_node_03 = self.head
        cur_str = ""
        
        while current_node_03 != None:
            cur_str = cur_str + str(current_node_03.data) + " --> "
            current_node_03 = current_node_03.next

        print(cur_str)

    def get_length_03(self):
        cnt = 0
        current_node_03 = self.head

        while current_node_03 != None:
            cnt += 1
            current_node_03 = current_node_03.next

        return cnt
    
    def insert_at_03(self, location, data):
        if location<0 or location> self.get_length_03():
            print("Invalid location")
            return

        if self.head.next == None:
            self.append_at_begining_03()
            return
        
        current_node_03 = self.head
        cnt = 0
        while current_node_03 != None:
            if cnt == location - 1:
                node_03 = Node_03(data, self.head.next)
                self.head.next = node_03
                break
            current_node_03 = current_node_03.next
            cnt +=1

    def append_at_end_03(self, data):
        current_node_03 = self.head
        while current_node_03.next:
            current_node_03 = current_node_03.next
        current_node_03.next = Node_03(data, None)
    
    def search_03(self, search_03_item):
        current_node_03 = self.head
        
        while current_node_03 != None:
            if current_node_03.data == search_03_item:
                print("This is found..")
                return
            current_node_03 = current_node_03.next
        print("OOps data not found")

    
    def delete_03(self):
        if self.head.next is None:
            print("This is empty")
            return
        else:
            current_node_03 = self.head
            while current_node_03.next.next is not None:
                current_node_03 = current_node_03.next
            current_node_03.next = None
        
         

if __name__ == "__main__":
    ll = linked_03()
    ll.append_at_begining_03(1000)
    ll.append_at_begining_03(2000)
    ll.append_at_begining_03(3000)
    ll.print_linked_03_list()
    ll.append_at_end_03(8000)
    ll.print_linked_03_list()
    ll.search_03(8000)
    ll.delete_03()
    ll.print_linked_03_list()
    
    
    ll.get_length_03()
    ll.insert_at_03(1, 500)
    ll.print_linked_03_list()