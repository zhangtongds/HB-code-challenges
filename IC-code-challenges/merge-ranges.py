def merge_interval(lst):
    """
    >>> merge_interval([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    
    >>> merge_interval([(1, 2), (2, 3)])
    [(1, 3)]

    >>> merge_interval([(1, 5), (2, 3)])
    [(1, 5)]

    >>> merge_interval([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]


    """

    interval = [lst[0]]
    lst.sort()
    for current_start, current_end in lst[1:]:
        result_start, result_end = interval[-1]
        if result_end >= current_start:
            interval[-1] = (min(result_start, current_start), max(result_end, current_end))
        else:
            interval.append((current_start, current_end))
            
    return interval


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
