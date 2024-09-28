c = [4, -1, 4, -2, 4]
o = [[2, 4]]

def robot(commands, obstacles):
    robot_x = 0
    robot_y = 0
    max_distance = 0
    direction = "North"
    
    obstacle_set = set(map(tuple, obstacles))
    
    for i in commands:

        if i == -1:
            if direction == "North":
                direction = "East"
            elif direction == "East":
                direction = "South"
            elif direction == "South":
                direction = "West"
            elif direction == "West":
                direction = "North"

        elif i == -2:
            if direction == "North":
                direction = "West"
            elif direction == "West":
                direction = "South"
            elif direction == "South":
                direction = "East"
            elif direction == "East":
                direction = "North"

        else:
            for _ in range(i):
                next_x, next_y = robot_x, robot_y
                if direction == "North":
                    next_y += 1
                elif direction == "East":
                    next_x += 1
                elif direction == "South":
                    next_y -= 1
                elif direction == "West":
                    next_x -= 1
                
                if (next_x, next_y) not in obstacle_set:
                    robot_x, robot_y = next_x, next_y
                    max_distance = max(max_distance, robot_x**2 + robot_y**2)
                else:
                    break

    return max_distance

print(robot(c, o))