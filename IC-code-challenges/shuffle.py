import random
def shuffle(the_list):
    rest = len(the_list)
    while rest != 0:
        rand_i = random.randint(0, rest-1)
        the_list[len(the_list)-rest],the_list[rand_i] = the_list[rand_i], the_list[len(the_list)-rest]
        rest -= 1
    return the_list


sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list