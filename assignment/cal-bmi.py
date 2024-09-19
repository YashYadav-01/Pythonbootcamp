def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi <= 16:
        return "Very underweight"
    elif bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Healthy"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Very overweight"

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is {bmi:.2f}")
print(f"You are {category}")
