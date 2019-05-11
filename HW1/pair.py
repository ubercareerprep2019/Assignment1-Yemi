"""
@author: Olayemi Ibrahim
description: This function takes an array of integers and a target integer to which the array elements must sum. 
It returns an array of all pairs of integers from the input array whose sum equals the target.
"""

def pairThatEqualSum(arr, sum):     #O(n)
    ret = []

    for element in arr:
        
        #compliment = "compliment" of element so if sum is 10 and elemnt is 4 the complement is 6
        compliment = sum - element

        #check if compliment is in array
        if compliment in arr:

            #make sure that compliment found isn't a duplicate of itself
            if compliment == element and arr.count(compliment) < 2:
                continue

            #make sure value pair isn't already present
            if [element, compliment] and [compliment, element] not in ret:

                #add to return list
                ret.append([element, compliment])

    return ret

"""
TEST CASES

print(pairThatEqualSum([1,2,3,4,5,6,7,8,9,10], 10))     #[[1, 9], [2, 8], [3, 7], [4, 6]]
print(pairThatEqualSum([1, 2, 3], 6))                   #[]
print(pairThatEqualSum([], 0))                          #[]
print(pairThatEqualSum([50,50,100,200,300], 100))       #[[50, 50]]
print(pairThatEqualSum([1,3,4,6,7,8,9,2], 20))`         #[]`

"""

