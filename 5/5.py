input_file = open('input.txt', 'r')
program_array = [int(instruction) for instruction in input_file.read().split(",")]

opcode_increments = { 
    1: 4,
    2: 4, 
    3: 2,
    4: 2,
    5: 0,
    6: 0,
    7: 4,
    8: 4,
    99: 0
}

def get_immediate_value(program, pointer):
    return program[pointer]

def get_position_value(program, pointer):
    return program[program[pointer]] 

def get_mode(instruction, param_num):
    # Param 3 is always immediate because 'Parameters that an instruction writes to will never be in immediate mode'
    if param_num == 3:
        return 1

    instruction_str = str(instruction)    
    modes = [int(mode) for mode in instruction_str[:len(instruction_str) - 2]]
    modes.reverse()
    
    if param_num - 1 >= len(modes):
        return 0
    
    return modes[param_num -1]    

def get_parameter_value(program, instruction, instruction_pointer, param_num):
    mode = get_mode(instruction, param_num)
    param_pointer = instruction_pointer + param_num

    return get_position_value(program, param_pointer) if mode == 0 else get_immediate_value(program, param_pointer)

def run_program(program, input):
    instruction_pointer = 0

    while instruction_pointer < len(program): 
        instruction = program[instruction_pointer]
        opcode = instruction % 100
        
        if opcode == 1:
            program[program[instruction_pointer + 3]] = get_parameter_value(program, instruction, instruction_pointer, 1) + get_parameter_value(program, instruction, instruction_pointer, 2)            
        if opcode == 2:
            program[program[instruction_pointer + 3]] = get_parameter_value(program, instruction, instruction_pointer, 1) * get_parameter_value(program, instruction, instruction_pointer, 2)            
        if opcode == 3:
            program[program[instruction_pointer + 1]] = input            
        if opcode == 4:
            val = get_parameter_value(program, instruction, instruction_pointer, 1)
            if val != 0:
                return val            
        if opcode == 5:
            instruction_pointer = get_parameter_value(program, instruction, instruction_pointer, 2) if get_parameter_value(program, instruction, instruction_pointer, 1) != 0 else instruction_pointer + 3
        if opcode == 6:
            instruction_pointer = get_parameter_value(program, instruction, instruction_pointer, 2) if get_parameter_value(program, instruction, instruction_pointer, 1) == 0 else instruction_pointer + 3
        if opcode == 7:
            program[program[instruction_pointer + 3]] = 1 if get_parameter_value(program, instruction, instruction_pointer, 1) < get_parameter_value(program, instruction, instruction_pointer, 2) else 0            
        if opcode == 8:
            program[program[instruction_pointer + 3]] = 1 if get_parameter_value(program, instruction, instruction_pointer, 1) == get_parameter_value(program, instruction, instruction_pointer, 2) else 0            
        if opcode == 99:
            return

        instruction_pointer += opcode_increments[opcode]

# Part 1
print('Part 1: ' + str(run_program(program_array.copy(), 1)))

# Part 2
print('Part 2: ' + str(run_program(program_array.copy(), 5)))