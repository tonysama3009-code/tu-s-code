# Question 1
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        continue

numbers.sort(reverse=True)
print("The five greatest numbers:")
for num in numbers[:5]:
    print(num)


# Question 2
num = int(input("Enter an integer: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# Question 3
cities = []
for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("\nCities entered:")
for city in cities:
    print(city)


# Question 4
def calculate_sum(int_list):
    total = 0
    for number in int_list:
        total += number
    return total

def main_q4():
    test_list = [10, 20, 30, 40, 50]
    result = calculate_sum(test_list)
    print(f"The sum of the list is: {result}")

main_q4()


# Question 5
def remove_odd_numbers(int_list):
    even_list = []
    for number in int_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

def main_q5():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cut_down_list = remove_odd_numbers(original_list)
    print(f"Original list: {original_list}")
    print(f"Cut-down list: {cut_down_list}")

main_q5()