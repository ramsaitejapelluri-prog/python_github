# creating variables and data types

name="saiteja"
age=20
height=1.75
student=True
print(name,age,height,student)


#sting formating

print(f"name: {name} , age: {age} , height: {height}, student: {student}")

#arithmetic operations

print("age is:",age)
age_in_months=age*12
age_in_days=age*365
remainder=age%7
age_raised=age**2

print("age in months:",age_in_months)
print("age in days:",age_in_days)
print("remainder when age is divided by 7:",remainder)
print("age is raisedto power of 2:",age_raised)

#this is were are using for user age calculating in months ,days..etc


age=int(input("enter your age:"))
age_in_months=age*12
age_in_days=age*365
remainder=age%7
age_raised=age**2

print("age in months:",age_in_months)
print("age in days:",age_in_days)
print("remainder when age is divided by 7:",remainder)
print("age is raisedto power of 2:",age_raised)
