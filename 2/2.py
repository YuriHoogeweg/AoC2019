input_file = open('input.txt', 'r')
program_array = input_file.read().split(",")

def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb

    instruction_pointer = 0

    while instruction_pointer < len(program): 
        opcode = int(program[instruction_pointer])
        if opcode == 99: break    
        
        param1 = int(program[int(program[instruction_pointer + 1])])
        param2 = int(program[int(program[instruction_pointer + 2])])
        destination_instruction_pointer = int(program[instruction_pointer + 3])

        if opcode == 1:
            program[destination_instruction_pointer] = param1 + param2
        if opcode == 2:
            program[destination_instruction_pointer] = param1 * param2

        instruction_pointer += 4

    return program[0]

# Part 1
print(run_program(program_array.copy(), 12, 2))

#Part 2
desired_output = 19690720

for noun in range(0, 99):
    for verb in range(0, 99):
        result = int(run_program(program_array.copy(), noun, verb))
        if result == desired_output:
            print (100 * noun + verb)
            break