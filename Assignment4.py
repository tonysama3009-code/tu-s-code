import re

# 1. Check university course code format
def is_valid_course_code(code):
    return bool(re.fullmatch(r"[A-Z]{3}\d{3}", code))


# 2. Check valid hex color
def is_valid_hex_color(color):
    return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", color))


# 3. Find all numbers and calculate their sum
def sum_of_numbers(text):
    numbers = re.findall(r"\d+", text)
    return sum(map(int, numbers))


# 4. Hide phone numbers
def hide_phone_numbers(text):
    return re.sub(r"(\+84\d+|\b\d{10}\b)", "[REDACTED]", text)


# ---------------- Example Testing ----------------

print(is_valid_course_code("TEC001"))
print(is_valid_hex_color("#1A2B3C"))

text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_of_numbers(text))

text2 = "Call me at 0878296005 or +84878296005 tomorrow."
print(hide_phone_numbers(text2))
