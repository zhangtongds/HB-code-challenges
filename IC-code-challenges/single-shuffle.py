  def is_single_riffle(half1, half2, shuffled_deck):
    
    if not len(shuffled_deck):
        return True
    if len(shuffled_deck) != len(half1) + len(half2):
        return False

    elif len(half1) > 0 and shuffled_deck[0] == half1[0]:
        return is_single_riffle(half1[1:], half2, shuffled_deck[1:])
    elif len(half2) > 0 and shuffled_deck[0] == half2[0]:
        return is_single_riffle(half1, half2[1:], shuffled_deck[1:])

    return False





