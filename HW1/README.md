# Homework 1

## Part 2 A&B
### Arrays & Strings:

● Implement the function: Boolean isStringPermutation(String s1, String s2)

○ This function takes two strings and returns true if one string is a permutation of
the other, false otherwise.

● Implement the function: Array<Pair<int>> pairsThatEqualSum(Array<int> inputArray, int
targetSum)

○ This function takes an array of integers and a target integer to which the array
elements must sum. It returns an array of all pairs of integers from the input
array whose sum equals the target.

## Part 3 A&B
### Stacks and Queues:

● Implement the Stack class from scratch. You will need the following methods. 

○ push() 

■ Pushes an integer on top of the stack. 


○ pop()

■ Removes what is on the top of the stack, and returns that value to the 
caller.


○ top()

■ Looks at the top value, and returns it. Does not manipulate the stack. 


○ isEmpty() 

■ Returns a True or False if the stack is Empty or not, respectively. 


● Implement a Stack Test that makes you comfortable with your implementation. (Example above) You’re encouraged to write more rigorous test cases. 

● What happens if you pop off more items than you push? Write a test for this. 

● Add a new method to you Stack class called min(), which returns the minimum element of the stack in O(1) time, as opposed to O(n) time. 

● Bonus : Improve your min() function to return the minimum element of the queue in O(1) time, and O(1) space optimized. 

● Implement Queues (Queue.enqueue, Queue.dequeue, and Queue.init) using the stack you made. 


## Part 4
### Linked Lists:

● Implement a Singly Linked List class. You will need to implement the following methods: 

○ void pushBack(<T> data) 
  
■ Adds a single node containing data to the end of the list 


○ <T> popBack() 
  
■ Removes a single node from the end of the list 


○ void insert(uint index,<T> data) 
 
■ Adds a single node containing data to a chosen location in the list. If the index is above the size of the list, do nothing. 


○ void erase(uint index) 

■ Erases a single node at the index location in the list. 


○ <T> elementAt(uint index) 
  
■ Returns a single node at the index location in the list. 


○ uint size()

■ Returns the length of the list. 


● Implement the following tests (should be self explanatory): 

○ testPushBackAddsOneNode 

○ testPopBackRemovesCorrectNode

○ testEraseRemovesCorrectNode 

○ testEraseDoesNothingIfNoNode

○ testElementAtReturnNode 

○ testElementAtReturnsNoNodeIfIndexDoesNotExist 

○ testSizeReturnsCorrectSize 


● Implement the following method: Bool hasCycle() 

○ Cycles can happen if a given node references an earlier node for the “next” reference. Using your LinkedList class, implement a function to detect cycles in the list. 


● Implement a function to check if a linked list is a palindrome.

## Part 5
### Towers of Hanoi:

●Create a class to implement the Towers of Hanoi puzzle logic. You will need at least the following methods: 

● void moveDisk(uint startingRod, uint destinationRod) 

● Array<Disk> disksAtRod(uint rodIndex) 
  
● uint numberOfRods() 






