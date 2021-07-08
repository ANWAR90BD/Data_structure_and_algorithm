class Node_01:
    def __init__(self, data="Head", next=None):
        self.data = data
        self.next = next
    
class linked_01:
    def __init__(self):
        self.head = Node_01()
    
    def append_at_begining_01(self, data):
        node_01 = Node_01(data, self.head.next)
        self.head.next = node_01
    
    def print_linked_01_list_01(self):
        if self.head.next is None:
            print("This is empty")
            return
        
        current_node_01 = self.head
        cur_str = ""
        
        while current_node_01 != None:
            cur_str = cur_str + str(current_node_01.data) + " --> "
            current_node_01 = current_node_01.next

        print(cur_str)

    def get_length_01(self):
        cnt = 0
        current_node_01 = self.head

        while current_node_01 != None:
            cnt += 1
            current_node_01 = current_node_01.next

        return cnt
    
    def insert_at_01(self, location, data):
        if location<0 or location> self.get_length_01():
            print("Invalid location")
            return

        if self.head.next == None:
            self.append_at_begining_01()
            return
        
        current_node_01 = self.head
        cnt = 0
        while current_node_01 != None:
            if cnt == location - 1:
                node_01 = Node_01(data, self.head.next)
                self.head.next = node_01
                break
            current_node_01 = current_node_01.next
            cnt +=1

    def append_at_end_01(self, data):
        current_node_01 = self.head
        while current_node_01.next:
            current_node_01 = current_node_01.next
        current_node_01.next = Node_01(data, None)
    
    def search_01(self, search_01_item):
        current_node_01 = self.head
        
        while current_node_01 != None:
            if current_node_01.data == search_01_item:
                print("This is found..")
                return
            current_node_01 = current_node_01.next
        print("OOps data not found")

    
    def delete_01(self):
        if self.head.next is None:
            print("This is empty")
            return
        else:
            current_node_01 = self.head
            while current_node_01.next.next is not None:
                current_node_01 = current_node_01.next
            current_node_01.next = None
        
         

if __name__ == "__main__":
    ll = linked_01()
    ll.append_at_begining_01(10)
    ll.append_at_begining_01(20)
    ll.append_at_begining_01(30)
    ll.print_linked_01_list_01()
    ll.append_at_end_01(40)
    ll.print_linked_01_list_01()
    ll.search_01(10)
    ll.delete_01()
    ll.print_linked_01_list_01()
    
    
    ll.get_length_01()
    ll.insert_at_01(1, 100)
    ll.print_linked_01_list_01()