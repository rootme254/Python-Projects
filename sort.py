'''

Write a function my_sort which takes in a list of numbers (integers).
The function should return a list of sorted numbers such
that odd numbers come first and even numbers come last.

'''
def my_sort(integers):
  
  lst=[]
  
  lst1=[]
  
  for num in integers:

  
    if num % 2 != 0:
      lst.append(num)
      lst.sort()
    else:
      lst1.append(num)
      lst1.sort()


  joined=lst+lst1
    
  print (joined)


integers=[1,2,3,4,5,6,7,8,9]
  

n=[20,9,6,4,5,11,1]
my_sort(n)



 
