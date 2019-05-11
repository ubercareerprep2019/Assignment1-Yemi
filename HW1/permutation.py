"""
@author: Olayemi Ibrahim
description: This function takes two strings and returns true if one string is a permutation of the other, false otherwise.
"""
def isStringPermutation(s1, s2):    #O(n)
    #convert input to strings if not already
    s1 = str(s1)
    s2 = str(s2)

    #if the strings are not equal in length, they can't be permutations of each other
    if(len(s1) != len(s2)):
        return False

    #sort strings 
    s1 = sorted(s1)
    s2 = sorted(s2)

    #if sorted strings are equal, they are permutations of each other 
    if s1 == s2:
        return True

    return False

"""
TEST CASES

print(isStringPermutation("hello", "ohlel"))            #True
print(isStringPermutation("hel lo", "  ohl el"))        #False
print(isStringPermutation("Hello", "ohlel"))            #False
print(isStringPermutation("Hello", "oHlel"))            #True
print(isStringPermutation("hel  lo", "ohle  l"))        #True
"""