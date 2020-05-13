import copy

spam = ['A','B','C','D']
cheese = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L']]
cheese = copy.deepcopy(spam)

print(spam)
print(cheese)
