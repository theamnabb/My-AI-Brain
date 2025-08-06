
print("BMI Calculator App ")

userWeight = float(input("Enter your weight in kg: "))
userHeight = float(input("Enter your height in meters: "))

userHeightSquared = userHeight ** 2
userBMI = userWeight / userHeightSquared

print("Your BMI is: ", userBMI)