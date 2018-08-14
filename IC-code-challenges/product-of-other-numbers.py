# O(n**2) method

def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError
    products = []
    for i, item in enumerate(int_list):
        product = 1
        for j in range(len(int_list)):            
            if j != i:
                product *= int_list[j]
        products.append(product)
    return products
