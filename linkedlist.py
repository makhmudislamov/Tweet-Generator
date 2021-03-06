#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.ll_length = 0

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """
        Return a boolean indicating whether this linked list is empty.
        Running Time: O(1) >>> checking .head and .tail
        """
        return self.head is None and self.tail is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) >>> since using .ll_length """
        return self.ll_length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) only change the node (tail)"""
        # New node
        new_node = Node(item)
        # check if LL is empty and append at the beginning of the list
        if(self.head == None):
            self.head = new_node
            self.tail = self.head
        # else append at the end with tail 
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.ll_length += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we only change the first node and never loop through all nodes. """
        # New node
        new_node = Node(item)
        # check if head is pointing to none
        if(self.head == None):
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.ll_length += 1


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) >>> looking for an item at or near head 
        Worst case running time: O(n) looking for an item in the middle, near tail or item DNE"""

        node = self.head
        while (node != None):
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) >>> looking for an item at or near head
        Worst case running time: O(n) looking for an item in the middle, near tail or item DNE"""
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == item:
                self.ll_length -= 1
                if current_node.next is None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = current_node.next
                    return self.head
                else:
                    self.head = current_node.next
                    return self.head
            previous_node = current_node
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
