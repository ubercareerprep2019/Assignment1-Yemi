def isStringPermutation(s1, s2):
    if(len(s1) != len(s2)):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True

    return False

if __name__ == '__main__':
    print("*****PERMUTATION CHECK*****")
    str1 = input("Please enter base string: ")
    str2 = input("Please enter comparison string: ")

    if(isStringPermutation(str1, str2)):
        print("Yeet :)")
    else:
        print("no yeet :(")
