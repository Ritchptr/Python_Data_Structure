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
        while current.next and current.next.value < value:
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

class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BinaryTree.Node(value)
            return 
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = BinaryTree.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = BinaryTree.Node(value)
            else:
                self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        if not self.root:
            return None
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node :
            return None
        elif node.value == value:
            return node.value
        elif value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):

        if not node:
            print("Value Not Found!")
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.right and not node.left:
                return None
            elif node.left and node.right:
                temp = self._max_(node.left)
                node.value = temp.value
                node.left = self._delete_recursive(node.left, temp.value)
            elif node.right:
                return node.right
            elif node.left:
                return node.left
        return node

    def _max_(self, node):
        current = node
        while current.right:
            current = current.right
        return current
                 

    def display(self):
        if not self.root:
            print("Tree is Empty!")
            return None
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value, end= " ")
            self._inorder_traversal(node.right)
 