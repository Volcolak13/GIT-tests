def descending_order(num):
# Function to take any non-negative integer as an argument and return it with its digits in descending order.
    newnum = ""
    list = []
    list = [int(a) for a in str(num)]
    while list:
        max_value = max(list)
        max_index = list.index(max_value)
        newnum = newnum + str(max_value)
#        print(max_value, max_index)
        list.pop(max_index)
    return int(newnum)

num = -1
while num < 0:
    num = int(input("\nInput non-negative integer number: "))
if num >= 0 and num == int(num):
    newnum = descending_order(num)
    print ("New descending number is: ", newnum, "\n\n")

# Clever solution

# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))
# выделить несколько строк кода и нажать ctrl + /