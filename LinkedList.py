class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        if current == None:
            print "No link list present."
        while(current):
            print(current.data)
            current = current.next
    def add(self, data):
        current = self.head
        if current == None:
            print "No head present adding a fresh start"
            self.head = Node(data)
        else:
            #make sure there is a next or else bug NoneType
            while(current.next):
                current = current.next
            current.next = Node(data)
    
    def add_position(self, position, data):
        current = self.head
        counter_index = 1
        if current == None:
            print "No head present adding a fresh start"
            self.head = Node(data)
        else:
            if position > self.size_link():
                print "Sorry but can't insert in the current location"
                return
            elif position == 1:
                new_insert = Node(data)
                new_insert.next = current
                current = new_insert
            #make sure there is a next or else bug NoneType
            while(current.next and position <= self.size_link()):
                counter_index = counter_index + 1
                if(counter_index == position):
                    new_insert = Node(data)
                    new_insert.next = current.next
                    current.next = new_insert
                current = current.next
    
    # def delete_node_nth(self, position):
    #     current = self.head
    #     previous = None

    #     if current == None or position < 0:
    #         print "No link list present cant delete"
    #         return
    #     if position == 1:
    #         if position == 1 and self.size_link() == 1 :
    #             current = None
    #             return
    #     else:
    #         pos = 0
    #         while(current != None):
    #             pos = pos + 1
                
    #             if position == pos:
    #                 print "ok", pos, self.size_link()
    #                 if previous:
    #                     previous = current
    #                     print "previous ", previous.data
    #                 else:
    #                     current = current.next
    #                     print "current ", current.data
    #             previous = current
    #             current = current.next 
                    
                
    def size_link(self):
        size = 0
        current = self.head
        
        if current == None:
            return size
        
        while (current):
            size = size + 1
            current = current.next
        
        return size
        
class LinkedListPractice:
    ls = LinkedList()
    ls2 = LinkedList()
    first_node = Node(30)
    second_node = Node(20)
    
    ls.head = first_node
    
    ls.head.next = second_node
    ls.add(40)
    ls.add_position(8, 39)
    ls.add_position(2, 99)
    
    print("Size for first: ", ls.size_link(), "\n")
    
    ls.print_list()
    
    # ls.delete_node_nth(3)
    print " "
    ls.print_list()
    print("Size for first second try: ", ls.size_link(), "\n")

    ls2.print_list()
    ls2.add_position(1, 100)
    print("Size for first: ", ls2.size_link(), "\n")
    ls2.print_list()
    