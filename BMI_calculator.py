weight = float(input('Enter your weight in Kg: '))
height = float(input('Enter your height in meters: '))
bmi = weight//height**2
print(f'Your BMI is {bmi}.')
if bmi < 18.5:
    print('Your are underweight.')