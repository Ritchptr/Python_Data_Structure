class Double_LIngked_List:
    class node:
        def __init__(self, value = 0, next = None, prev = None):
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None

    def pushh(self, value):
        newnode = Double_LIngked_List.node(value)

        if not self.head or self.head.value >= value:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            newnode.prev = None
            self.head = newnode
            return
        
        current = self.head
        while current.next and current.next.value:
            current = current.next
        
        newnode.next = current.next
        newnode.prev = current
        if current.next:
            current.next.prev = newnode
        current.next = newnode
        

    def pop(self, value):
        if not self.head:
            print("List is empty!!")
            return None
        
        current = self.head

        while current and current.value != value:
            current = current.next

        if not current:
            print("Value is not found!!")
            return None
        
        if current == self.head:
            self.head = current.next
            if self.head:    
                self.head.prev = None
            return value

        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next
        return value
    
    def display(self):
        if not self.head:
            print("List is Empty!!")
            return None
        current = self.head

        while current:
            print(current.value, end='-')
            if not current.next:
                print(current.value)
            current = current.next


            