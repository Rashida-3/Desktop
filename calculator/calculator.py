def add(num1,num2):
  '''It take 2 parameter num1 and num2, adding both the parameter and store the result in ans variable and return ans'''
  ans = num1 + num2
  return ans

def substract(num1,num2):
  '''The function takes 2 parameter num1 and num2 subtract it and store the result in ans'''
  ans = num1 - num2
  return ans

def divide(num1,num2):
  '''the function takes 2 parameter num1 ans num2 ans store result in ans variable'''
  ans = num1/num2
  return ans

def multiply(num1,num2):
  '''takes 2 parameter num1 and nnum2 multiply it and store it in ans'''
  ans = num1*num2
  return ans

while True:
  print("A.add B.substract C.divide D.multiply")
  choice = int(input("enter choice : "))

  num1 = int(input("enter num1 : "))
  num2 = int(input("enter num2 : "))

  if choice == 1:
    print(f"{num1} + {num2} = {add(num1,num2)}")

  elif choice == 2:
    print(f"{num1} - {num2} = {substract(num1,num2)}")

  elif choice == 3:
    print(f"{num1} / {num2} = {divide(num1,num2)}")

  elif choice == 4:
    print(f"{num1} * {num2} = {multiply(num1,num2)}")

  else:
    print('Invlid permission')
  permission = input(" do you want to continue yes / no  ")[0].lower()
  if permission == 'n':
    break


  

