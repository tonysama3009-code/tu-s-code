import random

# Task 1
# Print 5 greatest numbers entered by user

def top_five_numbers():
    nums = []
    while True:
        s = input("Enter a number (empty to stop): ")
        if s == "":
            break
        nums.append(float(s))

    nums.sort(reverse=True)
    print("Top 5 greatest numbers:", nums[:5])


# Task 2
# Month → Season

def month_to_season():
    seasons = ("spring", "summer", "autumn", "winter")
    month = int(input("Enter month (1-12): "))

    if month in (12, 1, 2):
        print(seasons[3])
    elif month in (3, 4, 5):
        print(seasons[0])
    elif month in (6, 7, 8):
        print(seasons[1])
    elif month in (9, 10, 11):
        print(seasons[2])
    else:
        print("Invalid month")


# Task 3
# Names using set

def unique_names():
    names = set()

    while True:
        name = input("Enter name (empty to stop): ")
        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nFinal name list:")
    for n in names:
        print(n)


# Task 4
# Word frequency using dictionary

def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


# Task 5
# Remove odd numbers

def remove_odds(lst):
    return [x for x in lst if x % 2 == 0]


# Task 6(BONUS)
# Monte Carlo approximation of Pi

def approximate_pi():
    N = int(input("Enter number of random points: "))
    inside = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y <= 1:
            inside += 1

    pi = 4 * inside / N
    print("Approximate value of π:", pi)


# Main Program

print("\n--- Question 1 ---")
top_five_numbers()

print("\n--- Question 2 ---")
month_to_season()

print("\n--- Question 3 ---")
unique_names()

print("\n--- Question 4 ---")
text = input("Enter text: ")
print(word_frequency(text))

print("\n--- Question 5 ---")
lst = list(map(int, input("Enter integers separated by space: ").split()))
print("Original list:", lst)
print("Without odd numbers:", remove_odds(lst))

print("\n--- Question 6 (BONUS) ---")
approximate_pi()
