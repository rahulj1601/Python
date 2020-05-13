import copy

spam = ['A','B','C','D']
cheese = copy.deepcopy(spam)
# This will make a completely new copy of spam
# This prevents the lists from just sharing the same reference number
# When changing one list the other list will not be affected in this case
