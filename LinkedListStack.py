## Linked list ##
# linked list composite each data and next data.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.last is None:
            return None
        else:
            got = self.head.data
            self.head = self.head.next
            return got

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

def main_stack():
    a_stack = Stack()
    while True:
        do = input('what would you like to do? (pop, push, quit): ')
        if do == 'push':
            do_push = input('what would you like to push value? ')
            a_stack.push(int(do_push))
            a_stack.print_list()
        elif do == 'pop':
            popped = a_stack.pop()
            if popped is None:
                print('Stack is empty.')
            else:
                print('popped value: ', popped)
            a_stack.print_list()
        elif do == 'quit':
            break

def main_queue():
    a_queue = Queue()
    while True:
        do = input('what would you like to do? (get, put, quit): ')
        if do == 'put':
            do_put = input('what would you like to put value? ')
            a_queue.enqueue(int(do_put))
            a_queue.print_list()
        elif do == 'get':
            got = a_queue.dequeue()
            if got is None:
                print('Queue is empty.')
            else:
                print('got value: ', got)
            a_queue.print_list()
        elif do == 'quit':
            break


if __name__=='__main__':
    op = input('What do u want datastruture (stack, queue): ')
    if op == 'stack':
        main_stack()
    elif op == 'queue':
        main_queue()
