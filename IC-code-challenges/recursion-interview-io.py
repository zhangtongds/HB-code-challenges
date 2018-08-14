"""
Find the index of an item in a list using recursion.

Given a list of items:

>>> lst = ["hey", "there", "you"]
You should have a function that returns the 0-based index of a sought item:

>>> recursive_search("hey", lst)
0

>>> recursive_search("you")
2
If the item isn’t in the list, return None:

>>> recursive_search("porcupine", lst) is None
True
Important: Solve this problem only with recursion—you cannot use a for or while loop in your solution!

We’ve given you a file, recursiveindex.py, with an empty function, recursive_index:

def recursive_index(needle, haystack):
    Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
# Implement this method.


def recursive_search(word, lst, loop=0):
    if len(lst) == 0:
        return None
    if word == lst[0]:
        return loop
    else:
        loop += 1
        return recursive_search(word, lst[1:], loop)

def recursive_search(word, lst):
    if len(lst) == 0:
        return None
    if word == lst[0]:
        return 0
    idx = recursive_search(word, lst[1:])
    return 1 + idx if idx != None else None

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
    



