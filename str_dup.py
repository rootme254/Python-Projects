
def str_dup (word):
    #producess the word NOT in sorted manner
    '''This function takes in one string argument and removes duplicate characters'''
    
    char=set()
    
    for i in word:
        char.add(i)

    print (char)

#producess the word in sorted manner 
def dup (ls):

    lst=[]

    for i in ls:
        if i not in lst:
            lst.append(i)

    print (lst)
    
  
dup('wwoorrdd')
