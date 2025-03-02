def calculate_initial_angles(time):
    hours, minutes = map(int, time.split(":"))
    # Minute hand moves 6 degrees per minute
    minute_angle = minutes * 6
    # Hour hand moves 30 degrees per hour + 0.5 degrees per minute
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    return hour_angle, minute_angle

def move_cost(direction, angle_to_move, A, B, X, Y):
    # Calculate cost based on direction (clockwise or counterclockwise)
    if direction == "clockwise":
        return angle_to_move * A * Y
    else:  # counterclockwise
        return angle_to_move * B * Y

def calculate_min_cost(hour_angle, minute_angle, A, B, X, Y, target_angle):
    # Calculate the current angle between the two hands
    initial_angle = abs(hour_angle - minute_angle) % 360
    
    # The interior angle is the smallest angle between the two hands
    interior_angle = min(initial_angle, 360 - initial_angle)
    
    # The exterior angle is the remaining part of the circle
    exterior_angle = 360 - interior_angle
    
    # We need to calculate costs for both possible movements
    min_cost = float("inf")
    
    # Move the hour and minute hands to form the target angle
    for target in [interior_angle, exterior_angle]:
        # Cost for moving hour hand clockwise and minute hand counterclockwise
        hour_move = target * X
        minute_move = target * Y
        cost = hour_move + move_cost("counterclockwise", minute_move, A, B, X, Y)
        min_cost = min(min_cost, cost)
        
        # Cost for moving hour hand counterclockwise and minute hand clockwise
        hour_move = target * X
        minute_move = target * Y
        cost = hour_move + move_cost("clockwise", minute_move, A, B, X, Y)
        min_cost = min(min_cost, cost)

    return min_cost

# Read the input
initial_time = input().strip()
Q = int(input())
A, B, X, Y = map(int, input().split())

# Calculate initial angles for hour and minute hands
hour_angle, minute_angle = calculate_initial_angles(initial_time)

# Total cost initialization
total_cost = 0

# Process each query
for _ in range(Q):
    target_angle = int(input())
    total_cost += calculate_min_cost(hour_angle, minute_angle, A, B, X, Y, target_angle)

# Output the total minimum cost
print(total_cost)
