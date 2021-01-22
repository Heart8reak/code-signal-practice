class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        '''
        Takes an item as a parameter and inserts it into the 0th index of the list that is representing the Deque

        The runtime is linear, or 0(n), because every time you insert into the front of a list, all the other items in the list need to shift one position to the right.

        '''
        self.items.insert(0, item)
        

    def add_rear(self, item):
        '''
        Takse in an item as a parameter and appends that item to the end of the list that is representing the Deque.

        The runtime is constant 0(1) because appending to the end of a list happens in constant time.

        '''
        self.items.append(item)

    def remove_front(self):
        '''
        Removes and returns the item in the 0th index of the list, which represents the front of the Deque.

        The runtime is linear, or 0(n), becuase when we remove an item from the 0th index, all the other items have to shift one index to the left.

        '''
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        '''
        Removes and returns the last item of the list, which represents the rear of the Deque.

        The runtime is constant because all we're doing is indexing to the end of a list.
        '''
        if self.items:
            return self.items.pop()
        return None
    
    def peek_front(self):
        '''
        Returns the value found at the oth index of the list, which represents the front of the Deque

        The runtime is constant becuase all we're doing is inndexing into a list.
        '''
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        '''
        Returns the value found at the -1st , or last , index.

        the runtime is constant because all we're doing is indexing into a list.
        '''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        '''
        Returns the length of the list, which is representing the Deque.

        The runtime will be constant because all we're doing is finding the length of a list and returning that value
        '''
        return len(self.items)

    def is_empty(self):
        '''
        Checks to see if the list representing our Deque is empty. Returns True if it is, or False if it isn't.

        The runtime is constant because all we're doing is comparing two values.
        '''
        return self.items == []


def check_palindrome(input_str):

    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2:
        front_item = my_d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False

    return True


print(check_palindrome('racecar'))
print(check_palindrome('oranges'))
print(check_palindrome('illuminati'))