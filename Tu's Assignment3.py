#task 1: Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number, end=",")
    number += 1 

#task 2: Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
print("Chương trình chuyển đổi Inches sang Centimeters")
print("Nhập số âm để thoát chương trình")
while True:
    inches = float(input("Enter your inches (negative to quit): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm} cm")

#task 3: Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
print("Chương trình tìm số nhỏ nhất và lớn nhất")
print("Nhập các số (nhấn Enter để kết thúc)")
numbers = []

while True:
    user_input = input("Nhập một số: ")
    
    if user_input == "":  # Kiểm tra rỗng
        break
    
    try:
        number = float(user_input)  # Chuyển sang float
        numbers.append(number)
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")

if len(numbers) > 0:
    smallest = min(numbers)
    largest = max(numbers)
    
    print("\n" + "=" * 45)
    print(f"Các số đã nhập: {numbers}")
    print(f"Số nhỏ nhất: {smallest}")
    print(f"Số lớn nhất: {largest}")
else:
    print("\nKhông có số nào được nhập!")

#task 4:
#Write a game where the computer draws a random integer between 1 and 10.
#The user tries to guess the number until they guess the right number
#After each guess the program prints out a text: Too high, Too low or Correct.
#Notice that the computer must not change the number between guesses.
import random

print("=" * 50)
print("        CHÀO MỪNG ĐẾN VỚI GAME ĐOÁN SỐ")
print("=" * 50)
print("Tôi có một số đặc biệt từ 1 đến 10.")
print("Hãy thử đoán xem!")
print("-" * 50)

secret = random.randint(1, 10)
while True:
    guess = int(input("Guess a number (1-10): "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct")
        break

#task 5: 
#Write a program that asks the user for a username and password.
#If either or both are incorrect, the program ask the user to enter the username and password again.
#This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. 
#After five failed attempts the program prints out Access denied. The correct username is python and password rules.
print("=" * 50)
print("          HỆ THỐNG XÁC NHẬN")
print("=" * 50)
correct_user = "python"
correct_pass = "rules"

attempts = 0
while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_user and password == correct_pass:
        print("Welcome")
        break  # Thoát vòng lặp khi đăng nhập thành công
    else:
        attempts += 1
        if attempts == 5:
            print("Access denied")
        else:
            print(f"Sai thông tin! Còn {5 - attempts} lần thử.")

#task 6: 
#Write a function that extracts the middle character of a given string. If the string length is even, extract the middle two characters.
print("=" * 50)
print("          CHƯƠNG TRÌNH LẤY KÝ TỰ GIỮA CÁC CHUỖI")
print("=" * 50)
def take_middle_character(text):
    length = len(text)
    middle = length // 2 
    print(f"\n---phân tích chuỗi từ '{text}'---")  
    print(f"Độ dài text: {length}")
    print(f"Vị trí giữa: {middle}")
    
    if length % 2 == 0:
        return text[length//2 - 1:length//2 + 1]
    else:
        return text[length//2]
user_word=input("Mời bạn nhập từ mà bạn mong muốn: ")
result = take_middle_character(user_word)
print(f"Ký tự giữa: {result}")

#task 7: Write a function that takes a phrase and returns an acronym using the first letter of each word, capitalized.
#Input: "unidentified foreign object"
#Output: "UFO
print("=" * 50)
print("          CHƯƠNG TRÌNH TẠO TỪ VIẾT TẮT (ACRONYM)")
print("=" * 50)
def generate_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
user_text = input("Can you please enter your text: ")
outcome = generate_acronym(user_text)
print(f"this is your acronym: {outcome}")