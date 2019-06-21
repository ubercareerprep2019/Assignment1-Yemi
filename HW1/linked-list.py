class ListNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)
    
class LinkedList:
    head = None
    size = 0
    
    # Initialize new linked list which defaults to empty
    def __init__(self, data=None):
      if data is not None:
        self.head = ListNode(data)
        self.size = 1
        
    def __len__(self):
      return self.size
        
    def __str__(self):
      if self.is_empty():
        return "[]"
    
      current = self.head
      result = str(current)
      while current.next is not None:
        result += f' -> {str(current.next)}'
        current = current.next
      return f'[{result}]'
      
    def __iter__(self):
      current = self.head
      while current is not None:
        yield current
        current = current.next
      return
      
    def is_empty(self):
      if self.head is None:
        return True
      return False
      
    # Insert data to the front of the list O(1)
    def pushFront(self, data):  
      # create a new node to hold the data.
      node = ListNode(data)
      
      # if list is empty then make data the head
      if self.head is None:
        self.size += 1
        self.head = node
        return node
        
      # point new node to current head and make head the new node
      node.next = self.head
      self.head = node

      # increment list size
      self.size += 1
      
    # Delete data from the front of the list and return removed value
    def popFront(self):
      if self.is_empty():
        return False
        
      # store pointer to the front node
      node = self.head

      # point head to former heads next
      self.head = self.head.next

      # decrement list size
      self.size -= 1

      # return node
      return node
      
    # Push data to the end of the list O(N)
    def pushBack(self, data):
      # create a new node to hold the data.
      node = ListNode(data)
      
      # if ;ist is empty make data head
      if self.head is None:
        self.size += 1
        self.head = node
        return self.head
        
      # create pointer to iterate through list
      current = self.head
      
      # iterate through list till last node is reached
      while current.next is not None:
        current = current.next
        
      # make last node point to new data
      self.size += 1
      current.next = node
      return node
      
    def popBack(self):
      # if list is empty there's nothing to pop 
      if self.head is None:
        return False
        
      # If there's one value in the list
      if self.head.next is None:
        node = self.head.next
        self.head = None
        self.size -= 1
        return node
        
      # create pointer to iterate through list
      current = self.head

      # iterate through list till node before last node is reached
      while current.next.next is not None:
        current = current.next
    
      # make node before last node point to nothing
      node = current.next
      current.next = None
      
      # make last node point to nothing
      node.next = None
      self.size -= 1
      return node
      
    # insert a new node at index 
    def insert(self, data, index=0):

      # Push to front if index is 0 or unspecified
      if index == 0:
        return self.pushFront(data)

      # create node to contain data
      node = ListNode(data)

      # create pointer to iterate through list
      current = self.head
      count = 0
      
      # iterate through list until index is reached 
      while (count < index and current is not None):
        if (count + 1 == index):
          node.next = current.next
          current.next = node
          self.size += 1
          return True

        current = current.next

        # increment count as index
        count += 1
        
      # if indexis out of bounds return False
      return False
      
    # Delete node at specified index and return it 
    def erase(self, index=0):

    
      if self.is_empty():
        return False
        
      if (index == 0):
        return self.popFront()
        
      count = 0
      current = self.head
      while count < index and current.next is not None:
        if count + 1 == index:
          node = current.next
          current.next = current.next.next
          self.size -= 1
          return node
            
        current = current.next
        count += 1
      return False
      
    # funciton to return element at specific index
    def elementAt(self, index):
        if self.is_empty():
            return False
    
        if (index == 0):
            return self.popFront()
        
        count = 0
        current = self.head
        while count < index and current.next is not None:
            if count + 1 == index:
                node = current.next
                return node
            
            current = current.next
            count += 1
        return False
    
    # function to return size of list
    def list_size(self):
        return self.size

    # function to check if list loops back upon itself
    def hasCycle(self): 
        x  = set() 
        temp = self.head
        while (temp): 
            if (temp in x): 
                return True
            x.add(temp) 
     
            temp = temp.next
        return False

# TEST CASES 
def printLength(link):
    print("Current list length: {}\n".format(str(link.list_size())))

if __name__ == '__main__':

    link = LinkedList()
    # testPushBackAddsOneNode
    print("\nPushing 2 into list...")
    print(link.pushBack(2))
    printLength(link)

    # testPopBackRemovesCorrectNode
    print("\nPopping from the end of the list...")
    print(link.popBack())
    printLength(link)

    # testEraseRemovesCorrectNode
    print("\nAdding 2000 to the list and erasing it...")
    print(link.pushBack(2000))
    printLength(link)

    print(link.erase())
    printLength(link)


    # testElementAtReturnNode
    print("\nAdding 42, 56, 73, and 19 to the list")
    print(link.pushBack(42))
    print(link.pushBack(56))
    print(link.pushBack(73))
    print(link.pushBack(19))
    printLength(link)

    print("\nPrinting value at index 2...")
    print(link.elementAt(2))


    print("\nNow emptying list...")
    print(link.erase(3))
    print(link.erase())
    print(link.erase())
    print(link.erase())
    printLength(link)

    # testEraseDoesNothingIfNoNode
    print("\nAttempting to erase from empty list...")
    print(link.erase())

    # testElementAtReturnsNoNodeIfIndexDoesNotExist
    print("\nAttempting to print node at index 2 which does not exist...")
    print(link.elementAt(2))
