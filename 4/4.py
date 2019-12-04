input_file = open('input.txt', 'r')
min_value, max_value = input_file.read().split("-")

def contains_two_adjacent_digits(password: str):
    for i in range(0, 10):
        substr = str(i) + str(i)
        if password.find(substr) >= 0:
            return True            
    return False

def contains_exactly_two_adjacent_digits(password: str):
    for i in range(0, 10):
        substr = str(i) + str(i)
        found_index = password.find(substr)
        if (found_index >= 0 and 
            ( # First digit of the string or the digit prior is different
                found_index - 1 < 0 or 
                password[found_index - 1] != str(i)
            ) and 
            ( # Last digit of the string or the digit after is different
                found_index + 2 >= len(password) or 
                password[found_index + 2] != str(i)
            )): 
            return True            
    return False

def password_string_to_int_array(password: str):
    return [int(char) for char in password]

def increment_password(arr: list, position: int):
    if position == 0:
        arr[position] += 1        
    elif arr[position] == 9:
        arr[position] = 0
        return increment_password(arr, position - 1)
    else:
        arr[position] += 1        

    for i in range(0, 6):
        min_value = 0 if i == 0 else max(arr[0:i])
        if arr[i] < min_value:
            arr[i] = min_value
    return int(''.join(str(e) for e in arr))

def find_valid_passwords_part1(min_value, max_value):
    valid_passwords = []
    current_password = increment_password(password_string_to_int_array(min_value), 5)

    while current_password <= int(max_value):        
        password_str = str(current_password)
        if contains_two_adjacent_digits(password_str):
            valid_passwords.append(current_password)
        current_password = increment_password(password_string_to_int_array(password_str), 5)

    return valid_passwords    

def find_valid_passwords_part2(min_value, max_value):
    valid_passwords = []
    current_password = increment_password(password_string_to_int_array(min_value), 5)

    while current_password <= int(max_value):        
        password_str = str(current_password)
        if contains_exactly_two_adjacent_digits(password_str):
            valid_passwords.append(current_password)
        current_password = increment_password(password_string_to_int_array(password_str), 5)

    return valid_passwords   

# Part 1 
print(len(find_valid_passwords_part1(min_value, max_value)))

# Part 2
print(len(find_valid_passwords_part2(min_value, max_value)))