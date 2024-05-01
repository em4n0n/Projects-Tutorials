# Algorithm for a palindrome

def isPalindrome(bts):
    startIndex = 0
    endIndex = len(bts) -1 # a string starts at zero/think of the last index

    for x in bts:
        if bts[startIndex] != bts[endIndex]:
            return False
    return True

print(isPalindrome('racecar'))