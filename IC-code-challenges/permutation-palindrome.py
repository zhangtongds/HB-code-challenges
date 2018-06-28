
# not good for tast case 'abbb' etc.


# def has_palindrome_permutation(the_string):

#     # Check if any permutation of the input is a palindrome
#     if len(the_string) % 2 == 0:
#         if len(set(the_string)) == len(the_string)/2:
#             return True
#     else:
#         if len(set(the_string)) == len(the_string)/2 + 1 :
#             return True

#     return False

# better sloution

def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    seen = set()
    for word in the_string:
        if word in seen:
            seen.remove(word)
        else:
            seen.add(word)
    return len(seen) <= 1

