import math
#SIMPLE CALCULATOR
#defining fuctions
def add(a,b):
  print("\nthe sum is ",a+b,"\n")
def sub(a,b):
  print("\nthe difference is ",a-b,"\n")
def mul(a,b):
  print("\nthe product is ",a*b,"\n")
def div(a,b):
  try :
      c=a/b
      print("\nthe result is ",c,"\n")
  except:
      print("\nZeroDivisionError\n")
#giving choices to the user
print("===========================================================")
print("SIMPLE CALCULATOR")
print("===========================================================")
print("\n")
print("OPERATIONS")
print(""" 1. Addition
2.Subtraction
3.Multiplication
4.Division
5.Square root of number 
6. exponent (x^y)
7.Exit\n""")
print("===========================================================")
 
#get choice from the user
while True:
  ch=int(input("enter choice(1-7):"))
  print("\n")
  if ch not in (1,2,3,4,5,6,7):
    print("invalid choice , pls choose choice(1-7)")
  if ch==1:
      print("===========================================================")
      a=int(input("enter number 1:"))
      b=int(input("enter number 2:"))
      add(a,b)
      print("===========================================================")
   
  elif ch==2:
      print("===========================================================")
      a=int(input("enter number 1:"))
      b=int(input("enter number 2:"))
      sub(a,b)
      print("===========================================================")
      
  elif ch==3:
      print("===========================================================")
      a=int(input("enter number 1:"))
      b=int(input("enter number 2:"))
      mul(a,b)
      print("===========================================================")
      
  elif ch==4:
      print("===========================================================")
      a=int(input("enter number 1:"))
      b=int(input("enter number 2:"))
      div(a,b)
      print("===========================================================")

  elif ch==5:
      print("===========================================================")
      a=int(input("enter number 1:"))
      b=math.sqrt(a)
      print("\nthe square root of",a," is ",b,"\n")
      print("===========================================================")
      
  elif ch==6:
      print("===========================================================")
      a=int(input("enter num 1:"))
      b=int(input("enter num 2:"))
      c=pow(a,b)
      print(" the result is ",c,"\n")
      print("===========================================================")

  elif ch==7:
      print("""=========================================================== 
  Thank you for using Calculator
        Have a great day!
===========================================================""")
      break
    
