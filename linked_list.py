class Node:
    """Single Node"""

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"<Node: {self.data}>"


class LinkedList:
    """Single Linked List"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns True if the linked list at least has one element"""
        return self.head is None

    def size(self):
        """Returns the number of elements in the linked list
        Takes O(n) time complexity"""
        current = self.head
        counter = 0

        while current:
            current = current.next_node
            counter += 1
        return counter

    def add(self, data):
        """Adds a new node with data, at the head of the linked list
        Takes O(1) time complexity"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):
        """Inserts a new node in the index position
        Takes O(n) to find the index
        Takes O(1) to insert the new node

        The time complexity of this algorithm is O(n)"""
        if index == 0:
            self.add(data)

        new_node = Node(data)

        position = index
        current = self.head

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new_node
        new_node.next_node = next_node

    def remove(self, key):
        """Removes the node with matches with the key
        Takes O(n) time complexity"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        if found:
            return current
        return None

    def search(self, key):
        """Search for the first node with data that matches with the key
        Takes O(n) time"""
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def node_at_index(self, index):
        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            position += 1
            current = current.next_node

        return current
    
    def find_cycle_beggining(self):
        current = self.head
        memory = []
        
        while current:
            if current.data in memory:
                return current
            memory.append(current.data)
        return None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next_node
            curr.next_node = prev  # Reverse the link
            prev = curr  # Move prev one step ahead
            curr = next_node  # Move curr one step ahead
        return prev


    def __repr__(self):
        """Returns a string representation of the list
        Takes O(n) time complexity"""
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head ⁞ {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail ⁞ {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node

        return " → ".join(nodes)

my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

print(my_list)
my_list.reverse()
print(my_list)
