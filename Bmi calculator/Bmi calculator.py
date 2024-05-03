while True:
    name = str(input("Please enter your name: "))

    print("Now you are going to Calculate Your BMI")

    print(name + " you have to give me your body information like")
    try:
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
    except ValueError:
        print("Invalid input. Try again.")
        continue
    print("<**-----------Your Body mass index calculated-----------**>\n")
    
    BMI = weight / (height / 100) ** 2
    print(f"Your BMI is {BMI}")
    

    if BMI <= 18.4:
        print(name + " You are underweight.")
    elif BMI <= 24.9:
        print(name + " You are healthy.")
    elif BMI <= 29.9:
        print(name + " You are overweight.")
    elif BMI <= 34.9:
        print(name + " You are severely overweight.")
    elif BMI <= 39.9:
        print(name + " You are obese.")
    else:
        print(name + " You are severely obese.")

    # Store BMI calculation in a text file
    with open("bmi_records.txt", "a") as file:
        file.write(f"Name: {name}, Height: {height} cm, Weight: {weight} kg, BMI: {BMI}\n")
    print("Your Bmi information is saved")

    again = input("Should I Calculate again (yes/no): ")
    if again.lower() == 'no':
        print("Thanks For using me!")
        break

      