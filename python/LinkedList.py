class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.data) + " "
            temp = temp.next
        return result

    def get(self, position):
        temp = self.head
        for i in range(position):
            temp = temp.next
        return temp.data

    def prepend(self, data):
        n = Node(data)
        n.next = self.head.next
        self.head = n

    def push(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def insert_after(self, data, prev_node):
        n = Node(data)
        next = prev_node.next
        n.next = next
        prev_node.next = n

    def insert_in(self, data, position):
        n = Node(data)
        temp = self.head
        prev = None
        for i in range(position):
            if temp is None:
                break
            prev = temp
            temp = temp.next
        n.next = temp
        prev.next = n

    def remove_node(self, key):
        temp = self.head
        prev = None
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def remove_duplicate(self):
        dupli_dict = {}
        temp = self.head
        prev = None
        if temp.next is not None:
            return
        while temp is not None:
            if temp.data in dupli_dict.keys():
                prev = temp.next
            else:
                dupli_dict[temp.data] = True
                prev = temp
            temp = prev.next

    def pop(self, pos = -1):
        temp = self.head
        prev = None
        if pos == 0 and temp is not None:
            self.head = temp.next
            temp = None
            return
        if pos == -1:
            pos = self.count() - 1
        for i in range(pos):
            if temp is None:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def count(self) -> int:
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

list = LinkedList()
list.push(1)
list.push(1)
list.push(4)
list.remove_duplicate()
print(list)
