import math

input_file = open('input.txt', 'r')
module_masses = input_file.readlines()
fuel = 0

for mass in module_masses:
    fuel += math.floor(int(mass) / 3) - 2

print(fuel)