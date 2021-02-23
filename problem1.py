"""
-------------------------------------------------------------------------------
Name:  problem1.py
Purpose:  Determine the speed of the car and see the cost of the fine for it
 
Author: Lue.Kyle
 
Created: 23/02/2021
------------------------------------------------------------------------------
"""
#Input the speed limit and the recorded speed of the car
speed_limit = int(input("Enter the speed limit: "))
record_speed = int(input("Enter the recorded speed of the car: "))

#Caluclate the fine of the speeding car and output the fine 
if record_speed < speed_limit:
  print ("Congratulations, you are within the speed limit!")
elif record_speed > speed_limit + 31:
  print ("You are speeding and your fine is $570")
elif record_speed > speed_limit + 21 < speed_limit + 31:
  print ("You are speeding and your fine is $270")
elif record_speed > speed_limit + 1 < speed_limit + 21:
  print ("You are speeding and your fine is $100")
