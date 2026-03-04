age = int(input("Please enter your age (in years): "))

if age >= 100:
    print("You've already turned 100!")
elif age < 0:
    print("Try again after you are born!")
else:
    years_until_100 = 100 - age
    print(f"You will be 100 in {years_until_100} years!")
