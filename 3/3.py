import time

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y    

    def manhattan_distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

class Line:
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    steps = 0

    def __init__(self, start_x, start_y, instruction, steps):
        self.steps = steps
        direction = instruction[0:1]
        distance = int(instruction[1:]) 

        self.start_x = start_x
        self.start_y = start_y

        if direction == "U":
            self.end_y = start_y + distance
        elif direction == "D":
            self.end_y = start_y - distance
        else: 
            self.end_y = start_y

        if direction == "R":
            self.end_x = start_x + distance
        elif direction == "L":
            self.end_x = start_x - distance
        else:
            self.end_x = start_x

    def get_points(self):
        points = []
        x = self.start_x
        y = self.start_y
        
        while x != self.end_x or y != self.end_y:
            points.append(Point(x, y))
            if self.end_x > x:
                x += 1
            elif self.end_x < x:
                x -=1
            elif self.end_y > y:
                y += 1
            elif self.end_y < y:
                y -= 1   
        return points

    def intersects_with_point(self, x, y):
        return x >= self.start_x and x <= self.end_x and y >= self.start_y and y <= self.end_y  
    
    def intersects_with_line(self, line):
        if line.start_x < self.start_x and line.end_x < self.end_x:
            return False
        if line.start_y < self.start_y and line.end_y < self.end_y:
            return False
        if line.start_x > self.start_x and line.end_x > self.end_x:
            return False
        if line.start_y > self.start_y and line.end_y > self.end_y:
            return False   

        return True

    def get_intersecting_points(self, line):
        line1_points = self.get_points()
        line2_points = line.get_points()

        intersecting_points = []

        for p1 in line1_points:
            for p2 in line2_points:
                if p1.x == p2.x and p1.y == p2.y:
                    intersecting_points.append(p1)
        
        return intersecting_points

    def total_steps_at_point(self, point):
        return self.steps + point.manhattan_distance(Point(self.start_x, self.start_y))
            
def create_lines_from_instructions(instructions):
    lines = []
    previous_x = 0
    previous_y = 0
    steps = 0

    for instruction in instructions:
        new_line = Line(previous_x, previous_y, instruction, steps)
        steps += abs(previous_x - new_line.end_x) + abs(previous_y - new_line.end_y)
        previous_x = new_line.end_x
        previous_y = new_line.end_y
        lines.append(new_line)
    
    return lines

# Part 1 
def part1():
    input_file = open('input.txt', 'r')
    wires_strings = input_file.read().split("\n")

    wire1_lines = create_lines_from_instructions(wires_strings[0].split(","))
    wire2_lines = create_lines_from_instructions(wires_strings[1].split(","))

    shortest_distance = float('inf')
    starting_point = Point(0, 0)

    for line in wire1_lines:
        for line2 in wire2_lines:
            if (line.intersects_with_line(line2)):
                for point in line.get_intersecting_points(line2):
                    distance = point.manhattan_distance(starting_point)
                    if distance < shortest_distance and distance > 0:
                        shortest_distance = distance   

    return shortest_distance

# Part 2
def part2():
    input_file = open('input.txt', 'r')
    wires_strings = input_file.read().split("\n")

    wire1_lines = create_lines_from_instructions(wires_strings[0].split(","))
    wire2_lines = create_lines_from_instructions(wires_strings[1].split(","))

    shortest_combined_steps = float('inf')

    for line in wire1_lines:
        for line2 in wire2_lines:
            if (line.intersects_with_line(line2)):
                for intersection in line.get_intersecting_points(line2):
                    combined_steps_distance = line.total_steps_at_point(intersection) + line2.total_steps_at_point(intersection)                    
                    if combined_steps_distance < shortest_combined_steps and combined_steps_distance > 0:
                        shortest_combined_steps = combined_steps_distance

    return shortest_combined_steps

start = time.time()
part1_result = part1()
end = time.time()
print('Part 1: ' + str(part1_result) + '. Took ' + str(round(end - start, 2)) + ' seconds')

start = time.time()
part2_result = part2()
end = time.time()
print('Part 2: ' + str(part2_result) + '. Took ' + str(round(end - start, 2)) + ' seconds')