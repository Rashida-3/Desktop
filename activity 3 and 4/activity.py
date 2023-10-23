
def add(num1,num2):
    ''''it should add two numbere'''
    ans=num1+num2
    return ans

''' this is for extension'''
def sub(num1,num2):
    ans=num1-num2
    return ans

'''this is for division key word'''
def div(num1,num2):
    ans=num1/num2
    return ans

'''mutiplication'''
def mult(num1,num2):
    ans=num1*num2
    return ans


while True:
    print("a.add","b.subtraction","c.division","d.multiplication")

    choice=int(input("select your choice: "))

    num1=int(input("enter your 1st number:"))

    num2=int(input("enter your 2nd number:"))

    if choice==1:
        print(f"{num1}+{num2}={add(num1,num2)}")
    elif choice==2:
        print(f"{num1}-{num2}={sub(num1,num2)}") 
    elif choice==3:
        print(f"{num1}/{num2}={div(num1,num2)}")  
    elif choice==4:
        print(f"{num1}*{num2}={mult(num1,num2)}")

    permission=input("do you want to perform your calculator:") 
    # if permission=="No":
    #     break
    # elif permission=="Yes":
    #     continue


    if permission=="no":
        break

  











