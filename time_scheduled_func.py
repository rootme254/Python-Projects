#simple sheduler to run a program
'''
start with 1000ms
'''
import calendar as k
import schedule
import time


def show_date():
 
   print ('THE CALENDER IS BELOW ')
   print (k.month(2017,2))
   
# NOTE RUNNS AFTER TIME SPECIFIED
schedule.every(1).minutes.do(show_date)

while True :
  schedule.run_pending()
  time.sleep(1)
  
