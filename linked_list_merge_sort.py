from linked_list import LinkedList


def split(linked_list):
    """Divide a linked_list
    Takes O(k log n)"""
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        middle = size // 2

        middle_node = linked_list.node_at_index(middle - 1)

        left_half = linked_list
        right_half = LinkedList()

        right_half.head = middle_node.next_node
        middle_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """Merges two linked list sorting by data in its nodes
    Takes O(n) time"""
    # Create a new linked list
    merged = LinkedList()

    # Add a fake head that will be discarted later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right
    left_head = left.head
    right_head = right.head

    # Iterate over the left and right list
    while left_head or right_head:
        # If one left or right were None
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # Compare the data values
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    # Discart the fake head
    merged.head = merged.head.next_node
    return merged


def merge_sort(linked_list):
    """Orders a single linked list
    Runs O(kn log n)"""
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


l = LinkedList()
l.add(4)
l.add(1)
l.add(5)
l.add(0)
l.add(2)
l.add(3)

print("Unsorted linked list:")
print(l)

sorted_linked_list = merge_sort(l)
print("Sorted linked list:")
print(sorted_linked_list)
