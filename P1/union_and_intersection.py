class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_set = set()
    union_ll = LinkedList()

    llist_1 = llist_1.head
    llist_2 = llist_2.head
    
    while llist_1:
        union_set.add(llist_1.value)
        llist_1 = llist_1.next

    while llist_2:
        union_set.add(llist_2.value)
        llist_2 = llist_2.next

    for e in union_set:
        union_ll.append(e)

    return union_ll


def intersection(llist_1, llist_2):
    # Your Solution Here
    llist_1_set = set()
    llist_2_set = set()
    intersection_ll = LinkedList()

    llist_1 = llist_1.head
    llist_2 = llist_2.head

    while llist_1:
        llist_1_set.add(llist_1.value)
        llist_1 = llist_1.next

    while llist_2:
        llist_2_set.add(llist_2.value)
        llist_2 = llist_2.next

    intersection_set = set.intersection(llist_1_set, llist_2_set)

    for e in intersection_set:
        intersection_ll.append(e)

    return intersection_ll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
# One empty list
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
# no output because there are no elements
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))