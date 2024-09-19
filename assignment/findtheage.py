from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

# Example usage
birth_year = 2003
print(f"The age is {calculate_age(birth_year)} years.")