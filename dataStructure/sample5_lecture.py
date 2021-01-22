'''
Create a function that returns a list of strings that are sorted alphabetically
'''

# def sort_list(lst):
#     return sorted(lst)

# a = ["sarahamarie, 'jenni", 'fady', 'anthony']
# b = sort_list(a)

# print(b)


'''
Create function that takes a string, checks if it has the same number of "x"s
and "0"s and returns either True or False

'''

# def XO(txt):
#     numberOfOs = 0 
#     numberOfXs = 0 
#     for char in txt:
#         if char == 'x' or char == 'X':
#             numberOfXs += 1
#         elif char == 'o' or char == 'O':
#             numberOfOs += 1
#     return numberOfOs == numberOfXs

# print(XO("ooxx"))
# print(XO(""))
# print(XO("ooxx"))


def get_discounts(nums, percentage):
    discount = int(percentage[:-1]) / 100
    res = []
    for n in nums:
        res.append(n * discount)
    return res

print(get_discounts([2,4,6,11], "50%"))