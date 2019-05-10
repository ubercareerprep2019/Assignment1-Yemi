import itertools


def pairThatEqualSum(arr, sum):

    ret = []
    for pair in itertools.combinations(arr, r=2):
        if pair[0]+pair[1] == sum:
            ret.append(pair)
    
    return ret



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = input("Enter sum: ")
   
    print(pairThatEqualSum(arr, int(sum)))
