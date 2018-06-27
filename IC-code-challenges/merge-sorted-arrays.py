def merge_lists(a_lst, b_lst):

    """
    >>> merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    """

    i = 0
    j = 0
    merged_list = []
    while i < len(a_lst) and j < len(b_lst):
       
            if a_lst[i] < b_lst[j]:
                merged_list.append(a_lst[i])
                i += 1
            else:
                merged_list.append(b_lst[j])
                j += 1
    if i < len(a_lst):
        merged_list.extend(a_lst[i:])
    if j < len(b_lst):
        merged_list.extend(b_lst[j:])
    return merged_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
