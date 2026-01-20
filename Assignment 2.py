import math

# 1. Zander size check
def check_zander_size():
    length = float(input("Enter the length of the zander (cm): "))
    size_limit = 42

    if length < size_limit:
        diff = size_limit - length
        print("The zander is too small. Release it back into the lake.")
        print(f"It is {diff:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit. You may keep it.")


# 2. Cruise ship cabin class
def cabin_description():
    cabin = input("Enter cabin class (LUX, A, B, C): ").upper()

    if cabin == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Cabin above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Windowless cabin above the car deck.")
    elif cabin == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")


# 3. Hemoglobin level check
def hemoglobin_check():
    sex = input("Enter biological sex (male/female): ").lower()
    hb = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb > 155:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
    elif sex == "male":
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb > 167:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
    else:
        print("Invalid biological sex.")


# 4. Leap year check
def is_leap_year():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# 5. Pizza value comparison
def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m ** 2
    return price_usd / area


def compare_pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")


# Main program menu
def main():
    print("Choose a program to run:")
    print("1. Zander size check")
    print("2. Cruise ship cabin class")
    print("3. Hemoglobin level check")
    print("4. Leap year check")
    print("5. Pizza value comparison")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        check_zander_size()
    elif choice == "2":
        cabin_description()
    elif choice == "3":
        hemoglobin_check()
    elif choice == "4":
        is_leap_year()
    elif choice == "5":
        compare_pizzas()
    else:
        print("Invalid choice.")


# Run the program
main()
