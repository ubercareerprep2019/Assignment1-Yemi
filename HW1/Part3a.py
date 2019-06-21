class Stack():

    # initialize stack
    def __init__(self):
        self.list = []
        self.mins = []

    # function to add data to the stack
    def push(self, item):

        # if stack is empty
        if self.size() == 0:

            # add value to list of minuimum values
            self.mins.append(item)
        else:
            
            # add the smaller of the values item or the latest item in the list to the min list
            self.mins.append(min(self.mins[self.size() - 1], item))

        # add the value to the list
        self.list.append(item)

    # function to pop values from the list
    def pop(self):

        # if the list is empty throw an error
        if self.is_empty():
            raise ValueError('Stack empty')

        # pop from the list
        self.mins.pop()
        return self.list.pop()

    # function to peek from the top of the stack
    def top(self):

        # if stack is empty
         if self.is_empty():

             # throw error
             raise Exception("Stack empty")
         return self.list[-1] 

    # function to return minimum value in stack with O(1)
    def min(self):
        if self.is_empty():
            raise ValueError('Stack Empty')
        return self.mins[self.size() - 1]

    # function to check if stack is empty
    def is_empty(self):
        return self.size() == 0

    # fucntion to return stack size
    def size(self):
        return len(self.list)


# TEST CASES
if __name__ == '__main__':
    stack = Stack()
    print("Pushing values 5, 99, -2, 8 onto the stack...")
    stack.push(5)
    stack.push(99)
    stack.push(-2)
    stack.push(8)

    print("\nPrinting the minimum value in the stack...")
    print(stack.min())

    print("\nPopping two values from the stack...")
    stack.pop()
    stack.pop()

    print("\nPrinting the minimum value in the stack...")
    print(stack.min())
   
    print("\nPeeking the top value from stack")
    print(stack.top())

    print("\nPrinting the size of the stack...")
    print(stack.size())

