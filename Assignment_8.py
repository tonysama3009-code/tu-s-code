import random

# --- Questions 1, 2, and 3: Elevator and Building ---

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print("Invalid floor.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        print(f"\nRunning elevator {elevator_num} to floor {target_floor}:")
        self.elevators[elevator_num - 1].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n--- FIRE ALARM! All elevators returning to bottom floor ---")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1}:")
            elevator.go_to_floor(self.bottom)

# Testing Building and Elevators
my_building = Building(1, 10, 3)
my_building.run_elevator(1, 5)
my_building.run_elevator(2, 8)
my_building.fire_alarm()


# --- Question 4: The Race Class ---

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(0, min(self.current_speed + change, self.maximum_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Reg Num':<10} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance'}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.maximum_speed:<8} km/h | {car.current_speed:<10} km/h | {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

# Main program for the Race
competitors = [Car(f"ABC-{i}", random.randint(150, 200)) for i in range(1, 11)]
grand_derby = Race("Grand Demolition Derby", 8000, competitors)

hours_elapsed = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours_elapsed += 1
    
    # Print status every 10 hours
    if hours_elapsed % 10 == 0:
        print(f"\n--- Status at Hour {hours_elapsed} ---")
        grand_derby.print_status()

# Final status update
print(f"\n--- FINAL RESULTS (Total Hours: {hours_elapsed}) ---")
grand_derby.print_status()