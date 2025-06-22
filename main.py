import DataStucture
import random as rdm

class Run:
    def DLL():
        List = DataStucture.Double_LIngked_List()
        print("This program is a simple implementation of Double Linkked-list, including insertion and deletion!")
        print()

        length = int(input("Input the length of the list: "))

        for i in range(length):
            value = rdm.randint(1, 100)
            List.pushh(value)
        
        List.display()
        remove = int(input("Delete One!: "))
        x = List.pop(remove)
        if x:
            print(f"You have successfully delete {x}!")
            List.display()

    def Binary_Tree():
        root = DataStucture.BinaryTree()
        print("This program is a simple implementation of Binary Tree(Unbalanced Tree), including insertion, deletion, and search!")
        print()
        length = int(input("Input the number of the tree: "))

        for i in range(length):
            value = rdm.randint(1, 100)
            root.insert(value)
        
        root.display()

        remove_value = int(input("Delete One!: "))
        deleted_value = root.search(remove_value)
        root.delete(remove_value)
        if deleted_value:
            print(f"You have successfully delete {deleted_value}!")
            root.display()

def main():
    while(True):
        print("What data structure do you want to run?")
        print("1. Double Linked-list")
        print("2. Binary tree (Unbalanced)")
        print("0. Nothing!")

        choice = int(input("Input your choice!: "))

        if choice == 1:
            Run.DLL()
            break
        elif choice == 2:
            Run.Binary_Tree()
            break
        elif choice == 0:
            print("Thank You!")
            break
        else:
            print("Enter the corret number! (0/1/2)")
            print()

try:
    main()
except ValueError:
    print("Value Eror")
