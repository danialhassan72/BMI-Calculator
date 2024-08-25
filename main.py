weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / height**2
status = "underweight" if bmi < 18.5 else "normal weight" if bmi < 25 else "overweight" if bmi < 30 else "obese" if bmi < 35 else "clinically obese"
print(f"Your BMI is {bmi:.2f}, you are {status}.")
