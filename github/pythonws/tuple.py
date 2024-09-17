# myTuple=("yash","yash","yash","yash",)
# print(myTuple[1])

# for item in myTuple:
#     print(item)


#DICTIONARY
# myDict={
#     "keys":"values",
#     "name":"yash",
#     "email":"yash@gmail.com"
#     }

# print(type(myDict))

# print(myDict)

# for item in myDict:
#     print(myDict[item])

# print(myDict.get("keys"))

# myDict["name"]="ram"
# print(myDict)




#oops concept
# class & object

# class Yash:
#     age=21
#     print("air force")

# #create bject and pass class properties
# yash = Yash()
# print(yash.age)

#age calculate
# bornYear = int(input("enter born year"))
# currentYear = int(input("enter current year"))
# class AgeCalculator:
#     ageInYear = currentYear - bornYear
#     # dob="29 april 2003"
# age = AgeCalculator()
# print(age.ageInYear)


#polymorphism method overloading
def age(dob1):
  print(dob1)

def age(dob1,name):
   print(dob1,name)

   x=age("29 april 2003")
#    y=age("29 april 2003","Yash Yadav")