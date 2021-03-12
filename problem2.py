"""
-------------------------------------------------------------------------------
Name:  problem2.py
Purpose:  Determine the sides of the traingle and determine if it is a triangle
 
Author: Lue.Kyle
 
Created: 23/02/2021
------------------------------------------------------------------------------
"""
#Input the lengths of the three sides
print ("Welcome to the Triangle Checker")
side_1 = int(input("Enter the length of the first side: "))
side_2 = int(input("Enter the length of the second side: "))
side_3 = int(input("Enter the length of the third side: "))

#Calculate if it is a triangle depending on the sides and output the result
if side_3 > side_2 + side_1:
  print ("The figure is not a triangle")
elif side_2 > side_3 + side_1:
  print ("The figure is not a triangle")
elif side_1 > side_2 + side_3:
  print ("The figure is not a triangle")
elif side_1 <= side_2 + side_3:
  print ("The figure is a triangle")
elif side_2 <= side_1 + side_3:
  print ("The figure is a triangle")
elif side_3 <= side_1 + side_3:
  print ("The figure is a triangle")
