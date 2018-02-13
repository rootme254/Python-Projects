#function that calculates power without any module import .

def power(base,pwr):


    if pwr == 1:

        print (base)


    elif pwr == 0:
        
         print (1)


    else:
          result =1
          count =0
          while (count < pwr):
              
              result *= base

              count += 1
              
          print (result)


power (5,4)
#input()#this is here so that whenever u run the code it does not exit until user cancels
