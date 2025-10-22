class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, target, data):
        cur = self.head
        while cur is not None:
            if cur is target:
                new_node = Node(data, cur.next)
                cur.next = new_node
                return True
            cur = cur.next
        return False 

    def delete(self, target):
        if self.head is None:
            return False
        if self.head is target:
            self.head = self.head.next
            return True
        prev = None
        cur = self.head
        while cur is not None:
            if cur is target:
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False 

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def size(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def to_list(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out

    def print(self):
        cur = self.head
        first = True
        while cur is not None:
            if not first:
                print(" -> ", end="")
            print(cur.data, end="")
            first = False
            cur = cur.next
        print() 



#PART B - Big O Analysis

def __init__(self):
    self.head = None   # 1
T(n) = 1
T(n) is O(1)


def is_empty(self):
    return self.head is None   # 1
T(n) = 1
T(n) is O(1)


def prepend(self, data):
    new_node = Node(data, self.head)  # 1
    self.head = new_node              # 1
T(n) = 2
T(n) is O(1)


def append(self, data):
    new_node = Node(data)       # 1
    if self.head is None:       # 1
        self.head = new_node    # 1
        return                  # 1
    cur = self.head             # 1
    while cur.next is not None: #(n-1)
        cur = cur.next          # (n-1)
    cur.next = new_node         # 1
T(n) = 1 + 1 + 1 + 1 + 1 + (n-1) + (n-1) + 1 = 2n + 4
T(n) is O(n)


def insert_after(self, target, data):
    cur = self.head                 # 1
    while cur is not None:          #n
        if cur is target:           #n 
            new_node = Node(data, cur.next)  # 1
            cur.next = new_node     # 1
            return True             # 1
        cur = cur.next              #(n-1) 
    return False                    # 1
T(n) = 1 + n + n + 1 + 1 + 1 + (n-1) + 1 = 3n + 4
T(n) is O(n)


def delete(self, target):
    if self.head is None:       # 1
        return False            # 1
    if self.head is target:     # 1
        self.head = self.head.next  # 1
        return True             # 1
    prev = None                 # 1
    cur = self.head             # 1
    while cur is not None:      #n
        if cur is target:       #n
            prev.next = cur.next    # 1
            return True             # 1
        prev = cur              #(n-1)
        cur = cur.next          #(n-1)
    return False                # 1
T(n) = 1+1+1+1+1+1 + n + n + 1 + 1 + (n-1) + (n-1) + 1 = 4n + 7
T(n) is O(n)


def search(self, data):
    cur = self.head             # 1
    while cur is not None:      #n
        if cur.data == data:    #n
            return cur          #1
        cur = cur.next          #(n-1)
    return None                 # 1
T(n) = 1 + n + n + (n-1) + 1 = 3n + 1
T(n) is O(n)


def size(self):
    count = 0                   # 1
    cur = self.head             # 1
    while cur is not None:      # n 
        count += 1              # n
        cur = cur.next          # n
    return count                # 1
T(n) = 1 + 1 + n + n + n + 1 = 3n + 3
T(n) is O(n)


def to_list(self):
    out = []                    # 1
    cur = self.head             # 1
    while cur is not None:      # n
        out.append(cur.data)    # n
        cur = cur.next          # n
    return out                  # 1
T(n) = 1 + 1 + n + n + n + 1 = 3n + 3
T(n) is O(n)


def print(self):
    cur = self.head             # 1
    first = True                # 1
    while cur is not None:      # n
        cur = cur.next          # n
T(n) = 1 + 1 + n + n = 2n + 2
T(n) is O(n)





