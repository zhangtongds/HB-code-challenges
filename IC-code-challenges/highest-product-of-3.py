#O(nlogn) method
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError
    list_of_ints.sort()
    return max(list_of_ints[-1] * list_of_ints[-2] * list_of_ints[-3], list_of_ints[-1] * list_of_ints[0] * list_of_ints[1])


# O(n) method
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError
    highest_product_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    max_product_2 = list_of_ints[0] * list_of_ints[1]
    min_product_2 = list_of_ints[0] * list_of_ints[1]
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    for num in list_of_ints[2:]:
        highest_product_3 = max(highest_product_3, max_product_2 * num, min_product_2 * num)
        max_product_2 = max(max_product_2, highest * num, lowest * num)
        min_product_2 = min(min_product_2, highest * num, lowest * num)
        highest = max(highest, num)
        lowest = min(lowest, num)
    return highest_product_3