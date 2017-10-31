from collections import Counter
import json
 

def name(nam):
  nam.split()
  cont=Counter(letter for letter in nam)
  print (json.dumps(cont,indent=3))
  j=" Appers dis many times"
  print (json.dumps(cont,indent=3,*j))
  
name('james is like me')
