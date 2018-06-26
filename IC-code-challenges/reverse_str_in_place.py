def reverse(lst):
    """

    >>> reverse(['a', 'b', 'c', 'd', 'e'])
    ['e', 'd', 'c', 'b', 'a']

    """
    for i in range(int(len(lst)/2)):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp
    return lst

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
