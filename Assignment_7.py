import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# --- Question 1 ---
print("--- Question 1 ---")
new_car = Car("ABC-123", 142)
print(f"Registration Number: {new_car.registration_number}")
print(f"Maximum Speed: {new_car.maximum_speed} km/h")
print(f"Current Speed: {new_car.current_speed} km/h")
print(f"Travelled Distance: {new_car.travelled_distance} km\n")

# --- Question 2 ---
print("--- Question 2 ---")
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"Current speed: {new_car.current_speed} km/h")

new_car.accelerate(-200)
print(f"Final speed after emergency brake: {new_car.current_speed} km/h\n")

# --- Question 3 ---
print("--- Question 3 ---")
# Setting up the example state
new_car.current_speed = 60
new_car.travelled_distance = 2000
print(f"Travelled distance before: {new_car.travelled_distance} km")

new_car.drive(1.5)
print(f"Travelled distance after drive(1.5): {new_car.travelled_distance} km\n")

# --- Question 4 ---
print("--- Question 4 ---")
cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg Num':<10} | {'Max Speed':<15} | {'Current Speed':<15} | {'Distance'}")
print("-" * 65)
for car in cars:
    print(f"{car.registration_number:<10} | {car.maximum_speed:<15} | {car.current_speed:<15} | {car.travelled_distance}")