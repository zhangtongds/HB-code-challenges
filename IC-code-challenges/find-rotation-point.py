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
    mid_point = int(len(words)/2)
    while mid_point != 0:
        if words[0] < words[mid_point]:
            mid_point = int((len(words) + mid_point)/2)
        else:
            mid_point = int(mid_point/2) 
    return mid_point