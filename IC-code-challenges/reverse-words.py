def reverse_words(message):
    """
    >>> reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l'])
    ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']
    """

    for i in range(int(len(message)/2)):
        message[i], message[-i-1] = message[-i-1], message[i]
    start = 0
    end = 1
    
    for i in range(len(message)):
        if message[i] == " ":
            end = i 
            message[start:end] = reversed(message[start:end])
            start = i+1
    message[start:] = reversed(message[start:])

    return message

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
