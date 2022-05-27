def high_and_low(numbers):
    # CODEWARS #3 In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
    # All numbers are valid Int32, no need to validate them.
    # There will always be at least one number in the input string.
    # Output string must be two numbers separated by a single space, and highest number is first. 
    num=[]
    for i in numbers.split():
        num.append(int(i))
    numbers=str(max(num))+" "+str(min(num))
    #print(max(num),min(num))
    # num=sorted(num, reverse=True)
    # numbers = [num[0]," ",num[-1]]
    print(numbers)
    return numbers

# CLever solution
# def high_and_low(numbers):
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))

# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])

numbers = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
resultat = high_and_low(numbers)
