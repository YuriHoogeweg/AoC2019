input_file = open('input.txt', 'r')
program_array = [int(instruction) for instruction in input_file.read().split(",")]

def get_parameter_value(program, first_instruction, instruction_pointer, param_number):
    instruction_str = str(first_instruction)    
    modes = [int(mode) for mode in instruction_str[:len(instruction_str) - 2]]
    modes.reverse()
    mode = modes[param_number - 1] if param_number - 1 < len(modes) else 0

    initial_param_value = int(program[instruction_pointer + param_number])

    if mode == 0:
        return int(program[initial_param_value])
    if mode == 1: 
        return initial_param_value

def run_program(program, input):
    instruction_pointer = 0

    while instruction_pointer < len(program): 
        first_instruction = program[instruction_pointer]
        opcode = first_instruction % 100                        
        
        if opcode == 1:
            program[program[instruction_pointer + 3]] = get_parameter_value(program, first_instruction, instruction_pointer, 1) + get_parameter_value(program, first_instruction, instruction_pointer, 2)
            instruction_pointer += 4
        if opcode == 2:
            program[program[instruction_pointer + 3]] = get_parameter_value(program, first_instruction, instruction_pointer, 1) * get_parameter_value(program, first_instruction, instruction_pointer, 2)
            instruction_pointer += 4
        if opcode == 3:
            program[program[instruction_pointer + 1]] = input
            instruction_pointer += 2            
        if opcode == 4:
            print(get_parameter_value(program, first_instruction, instruction_pointer, 1))
            instruction_pointer += 2
        if opcode == 5:
            instruction_pointer = get_parameter_value(program, first_instruction, instruction_pointer, 2) if get_parameter_value(program, first_instruction, instruction_pointer, 1) != 0 else instruction_pointer + 3
        if opcode == 6:
            instruction_pointer = get_parameter_value(program, first_instruction, instruction_pointer, 2) if get_parameter_value(program, first_instruction, instruction_pointer, 1) == 0 else instruction_pointer + 3
        if opcode == 7:
            program[program[instruction_pointer + 3]] = 1 if get_parameter_value(program, first_instruction, instruction_pointer, 1) < get_parameter_value(program, first_instruction, instruction_pointer, 2) else 0
            instruction_pointer += 4
        if opcode == 8:
            program[program[instruction_pointer + 3]] = 1 if get_parameter_value(program, first_instruction, instruction_pointer, 1) == get_parameter_value(program, first_instruction, instruction_pointer, 2) else 0
            instruction_pointer += 4

# Part 1
print(run_program(program_array.copy(), 5))