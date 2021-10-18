import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = ["rock"+rock,"paper"+paper,"scissor"+scissors]
i=int(input("enter 0 for rock,1 for paper and 2 for sessior\n"))
if i>=3: 
  print("Invalid Number")
else :
  print("valid number ")  
  ur = list1[i]
  print(ur)

  com = rd.randint(0,2)
  cm = list1[com]
  print(cm)

  if cm == ur :
    print("Draw")
  elif ur==list1[0] and cm==list1[1] :
    print("you win ")
  elif ur==list1[0] and cm==list1[2] :
   print("you win ")
  elif  ur==list1[1] and cm==list1[0] :
   print("you win ")
  elif   ur==list1[1] and cm==list1[2] :
   print("Oops You loose")
  elif  ur==list1[2] and cm==list1[0] :
   print("you win ")
  elif   ur==list1[2] and cm==list1[1] :
   print("Oops You loose")
  


   
