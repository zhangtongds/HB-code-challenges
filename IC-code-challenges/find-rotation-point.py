# O(n) method

def find_rotation_point(words):

    # Find the rotation point in the list
    if len(words) < 2:
        if words[0] > words[1]:
            return 1
        else:
            return 0
            
    for i in range(len(words)-1):
        if words[i] > words[i+1]:
            return i+1

    return 0

# O(logn) method

def find_rotation_point(words):
    left = 0
    right = len(words) - 1
    
    while left < right-1:
        middle = int((left + right)/2)
        if words[left] < words[middle]:
            left = middle
        else:
            right = middle
    return 0 if words[left] < words[right] else right

# recursion method
def find_rotation_point(words):
    left = 0
        right = len(words) - 1
        if right - left == 1:
            return 0 if words[left] < words[right] else right
        middle = int((left + right)/2)
        if words[left] < words[middle]:
            left = middle
        else:
            right = middle
        return left + find_rotation_point(words[left:right+1])
