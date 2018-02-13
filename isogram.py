
'''
Create a funtion called isIsogram that takes one argument, a word to test if it's an isogram. This function should return a boolean indicating whether it is an isogram (true) or not (false).
isogram is a word with no duplicate letters

'''

def is_isogram(word):
  
    print ( (True) if word and len(set(word)) == len(word) else (False) )


is_isogram('come')
is_isogram('assess') # ('assess', False)

