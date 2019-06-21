class Queue():

    # initialize queue
    def __init__(self):
        self.list = []

    # function to add values to the queue
    def enqueue(self, item):
        self.list.append(item)

    # function to remove values from the queue
    def dequeue(self):
        # if queue is empty
        if self.is_empty():

            # throw error 
            raise ValueError('Queue empty')

        # pop from the front of the list
        return self.list.pop(0)

    # function to check if queue is empty
    def is_empty(self):
        return self.size() == 0

    # function to return length of queue
    def size(self):
        return len(self.list)


# TEST CASES
if __name__ == '__main__':
    queue = Queue()
    print("Pushing values 5, 99, -2, 8 onto the queue...")
    queue.enqueue(5)
    queue.enqueue(99)
    queue.enqueue(-2)
    queue.enqueue(8)

    print("\nPopping two values from the queue...")
    print(queue.dequeue())
    print(queue.dequeue())
    

    print("\nPrinting the size of the queue...")
    print(queue.size())
   
