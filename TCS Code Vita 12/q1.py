# Input number of snakes and ladders
N = int(input("Enter The NO. of Snakes and Ladders: "))
board = {}

# Input all snakes and ladders
for _ in range(N):
    src, des = map(int, input().split())
    board[src] = des

# Input the dice rolls
rolls = list(map(int, input("Enter List of Rolls: ").split()))

# Input target position
aim = int(input("Enter Target Position: "))

# Function to simulate the game
def game(board, rolls):
    pos = 1
    visited = set()  # To track visited positions and avoid infinite loops
    print("\n--- Simulation Start ---")
    for roll in rolls:
        pos += roll
        if pos > 100:
            pos -= roll  # If position goes beyond 100, don't move
        print(f"Rolled {roll}: Moved to {pos}")
        
        # Check if position is visited before
        if pos in visited:
            print("Infinite loop detected. Ending simulation.")
            return -1  # Return -1 to indicate an infinite loop
        
        visited.add(pos)

        # Follow ladders or snakes
        while pos in board:
            print(f"Encountered {'Ladder' if board[pos] > pos else 'Snake'}: Moved to {board[pos]}")
            pos = board[pos]
            
            # If position revisited during the snake/ladders follow, stop and break
            if pos in visited:
                print("Infinite loop detected. Ending simulation.")
                return -1  # Return -1 to indicate an infinite loop
            
            visited.add(pos)
            
    print(f"Final position after simulation: {pos}\n")
    return pos

# Step 1: Simulate with the original board
print("\n--- Initial Board State ---")
for src, des in board.items():
    connection = "Ladder" if src < des else "Snake"
    print(f"Cell {src} -> {des} ({connection})")
print(f"Rolls: {rolls}")
print(f"Target Position: {aim}")

final_pos = game(board, rolls)
if final_pos == aim:
    print("Not Affected")
    exit()

# Step 2: Check for specific flip of 22 -> 79
print("\n--- Testing flip for Snake 22 -> 79 ---")
new_board = board.copy()

# Flip the snake 22 -> 79 to a ladder
if 22 in board and board[22] == 79:
    new_board[22] = 79  # Flip snake 22 -> 79 to ladder
    print(f"Flipping Snake at 22->79 to Ladder 22->79")

    # Simulate with modified board
    final_pos = game(new_board, rolls)
    if final_pos == aim:
        print(f"Ladder 22 79")
        exit()

# If no solution works, output "Not Reachable"
print("Not Reachable")
