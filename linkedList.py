

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinnkedList:

    def __init__(self, head, tail):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.tail is None:
            print("List is empty")
            return
        if self.tail is not None:
            print("List has nodes")
            return

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node
        
        self.head = new_node
        return new_node

    def push_back(self, data):
        new_node = Node(data)
        new_node.prev = self.tail

        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node 

        self.tail = new_node
        return new_node     
    
    def pop_front(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def pop_back(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.tail.prev.next = None

    def get_at(self, index):
        new_node = Node(None)
        new_node = self.head
        n = 0
        while (n != index):
            if new_node is None:
                return new_node
            new_node = new_node.next
            n += 1
        return new_node
    
    def travel(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, ' ')
                n = n.next

    def insert(self, index, data):
        right = self.get_at(index)
        if right is None:
            return self.push_back(data)
        
        left = right.prev
        if left is None:
            return self.push_front(data)
        
        new_node = Node(data)
        new_node.prev = left
        new_node.next = right
        left.next = new_node
        right.prev = new_node

        return new_node

    def earase(self, index):
        new_node = self.get_at(index)
        if new_node is None:
            return
        if new_node.prev is None:
            self.pop_front()
            return
        if new_node.next is None:
            self.pop_back()
            return
        
        left = new_node.prev
        right = new_node.next
        left.next = right
        right.prev = left

def main():
    my_list = LinnkedList(None, None)
    my_list.push_front(10)
    my_list.push_back(20)
    my_list.push_back(30)
    my_list.push_back(40)
    my_list.push_back(50)
    my_list.push_back(60)
    my_list.push_back(70)
    my_list.pop_front()
    my_list.insert(4, 1337)
    my_list.travel()

if __name__ == '__main__':
    main()