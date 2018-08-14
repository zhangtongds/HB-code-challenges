def find_duplicate(lst):
    duplicate = None
    for i, num in enumerate(the_list):
        if num == the_list[num - 1] and i != num - 1:
            duplicate = num
        else:
            the_list[num - 1], the_list[i] = the_list[i], the_list[num - 1]
    return duplicate