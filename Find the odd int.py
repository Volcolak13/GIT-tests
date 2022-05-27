from itertools import count


def find_it(seq):
#   Given an array of integers, find the one that appears an odd number of times.
#   There will always be only one integer that appears an odd number of times.

    cou = [seq.count(i) for i in seq]
    j=0
    for i in cou:
        if (i % 2) != 0:
            while j < 1:
                odd_index = cou.index(i)
                odd_number = seq[odd_index]
                j = j + 1
                print(odd_number)

#   CLEVER SOLUTION

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]
odd_num = find_it(seq)

#DONE