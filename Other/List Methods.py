spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
# Returns the index of the item inside the list

spam.append("hai")
# Adds the item to the end of the list

spam.insert(1, 'chicken')
# The item is inserted at the index 1 of the list, no values are deleted

spam.remove('hello')
# Removes the first item from the list called 'hello'

nums = [1,5,-1,4]
nums.sort()
# Will sort the list from smallest to largest
# Sort can also work for a list of strings where they will be alphabetised
spam.sort(reverse=True)
# The items will be sorted in reverse order

names = ["Alice", "Bob", "Carol", "alisa", "Zara", "chris"]
names.sort()
# When sorting a list of lower and upper case letters, the upper case letter words are brought to the front
names.sort(key = str.lower)
# Will sort out the items ignoring upper or lower case


