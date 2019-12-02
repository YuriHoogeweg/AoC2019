import math

input_file = open('input.txt', 'r')
module_masses = input_file.readlines()

#Part 1
def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2

total_fuel = 0

for mass in module_masses:
    total_fuel += calculate_fuel(mass)

print(total_fuel)

total_fuel = 0
# Part 2
for mass in module_masses:        
    fuel = calculate_fuel(mass)
    total_fuel += fuel

    fuel_mass = calculate_fuel(fuel)

    while fuel_mass > 0:
        total_fuel += fuel_mass
        fuel_mass = calculate_fuel(fuel_mass)

print(total_fuel)