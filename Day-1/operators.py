# Assignment operators: =, +=, -=
# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \nDiscount: {discount} \nDiscountedPrice:{disPrice}")

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus           #Meaning of salary+=bonus => salary=salary+bonus
# print("Salary with Bonus",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")

# salary-=tds          #salary=salary-tds

# print("Salary after tax",salary)

# Comparison operators: ==, >, >=, <, != etc.

# if(condition):
#  #code
# else :
#  #code

# age=int(input("Enter your age"))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("you are not eligible to cast your vote , You have to wait")

# print("End of Program")

# age=int(input("Enter your age"))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("Sorry!!! You are not eligible ")

# print("End of Program")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in Exam")
# else:
#     print("Clear the exam")



# != means not equal to
# accessCode=input("Enter Access Code:\t")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Welcome to your course")

# == means equal
# 

  

#Logical operators: and, or, not.

# mathMarks=int(input("Enter marks otained in Mathematics: "))
# phyMarks=int(input("Enter marks obtained in Physics: "))
# cheMarks=int(input("Enter marks obtained in Chemistry: "))


# if((mathMarks>=50) and (phyMarks>=55) and(cheMarks>=60)):
#      print("You are eligible to sit in pre exam of MBBS")
# else:
#      print("You have not got the required marks")

# idProof=input("Enter Id proof you have: \t")
# if((idProof=="passport")or(idProof=="dl")or(idProof=="voter id")):
#     print(f"Valid Id {idProof} we accept here")
# else:
#     print("Only passport,dl and voter id are accepted as Identity Proof")
#     print(f"{idProof}:is not valid ID here")

# mathMarks=int(input("Enter marks otained in Mathematics: \t"))
# gapYear=int(input("Enter Year gap if any otherwise Zero :\t "))
# if((mathMarks<=55) or (gapYear != 0)):
#     print("Not Eligible for BTech")
# else:
#     print("Eligible for BTech")
name=input("Enter User Name")
if(not name):
    print("Error!!!")
else:
    print("Welcome",name)
    