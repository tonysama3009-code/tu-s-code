

data = [
    "Alice,85",
    "Bob,90",
    "Tony,95",
    "skibi,69",
    "",
    "Python is fun",
    "Charlie,78",
    "Python programming"
]

def count_non_blank_lines(lines):
    count = 0
    for line in lines:
        if line.strip():
            count += 1
    return count


def find_keyword_lines(lines, keyword):
    line_numbers = []
    for index, line in enumerate(lines, start=1):
        if keyword in line:
            line_numbers.append(index)
    return line_numbers


def convert_to_uppercase(lines):
    upper_lines = []
    for line in lines:
        upper_lines.append(line.upper())

    # lưu ra file output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        for line in upper_lines:
            f.write(line + "\n")


def calculate_average_score(lines):
    total = 0
    count = 0

    for line in lines:
        parts = line.split(",")

        if len(parts) == 2 and parts[1].isdigit():
            total += float(parts[1])
            count += 1

    if count == 0:
        return 0

    return total / count


# ====== CHẠY CHƯƠNG TRÌNH ======

print("1. Non-blank lines:",
      count_non_blank_lines(data))

print("2. Lines containing keyword:",
      find_keyword_lines(data, "Python"))

convert_to_uppercase(data)
print("3. Uppercase content saved to output.txt")

print("4. Average score:",
      calculate_average_score(data))
