# 1079. Letter Tile Possibilities
# Medium
# Topics
# Companies
# Hint
# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1
 

# Constraints:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

t1 = "AAB"
# t1 = "AAABBC"
# t1 = "V"

def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    total += 1
                    counter[tile] -= 1
                    total += backtrack(counter)
                    counter[tile] += 1
            return total

def xyz(tiles):
    counter = {}
    for tile in tiles:
        counter[tile] = counter.get(tile, 0) + 1
        
    return backtrack(counter)

print(xyz(t1))