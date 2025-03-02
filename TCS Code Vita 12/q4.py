# Define the valid segment map for digits and operators.
segment_map = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|'],
    '+': ['   ', ' _|', ' _|'],
    '-': ['   ', ' _ ', '   '],
    '=': ['   ', '|_|', '|_|'],
    '%': [' _ ', '  |', ' _|'],
    '*': ['   ', '| |', '  |'],
}

# Function to check if a character's display matches any of the valid segment patterns
def compare_display(display, correct_pattern):
    for i in range(3):
        if display[i].strip() != correct_pattern[i].strip():
            return False
    return True

# Function to find the faulty character
def find_faulty_character(N, display_lines):
    # Width of each character in the display
    char_width = 3
    # List to hold all the character displays
    equation_displays = []

    # Extract each character's 3x3 display from the input
    for i in range(N):
        char_display = [
            display_lines[0][i * char_width:(i + 1) * char_width],
            display_lines[1][i * char_width:(i + 1) * char_width],
            display_lines[2][i * char_width:(i + 1) * char_width]
        ]
        equation_displays.append(char_display)

    # Check each character's display against the valid segment patterns
    for idx, display in enumerate(equation_displays):
        print(f"Checking character at index {idx + 1}: {display}")
        
        # Assume the character is faulty
        is_faulty = True
        
        # Compare the current display with the valid segment patterns
        for char, correct_pattern in segment_map.items():
            print(f"Comparing with pattern for '{char}': {correct_pattern}")
            if compare_display(display, correct_pattern):
                print(f"Character '{char}' matches the display.")
                # If a match is found, the character is not faulty
                is_faulty = False
                break
        
        if is_faulty:
            print(f"Faulty character found at index {idx + 1}: {display}")
            # If no match is found, this character is faulty
            return idx + 1  # Return 1-based index of the faulty character

    # If no faulty character is found, return 0 or an appropriate value
    return 0

# Input reading
N = int(input())  # Number of characters in the equation
display_lines = [input().strip() for _ in range(3)]  # The 3 lines of the display

# Solve and print the result6
print(find_faulty_character(N, display_lines))
