# 1900. The Earliest and Latest Rounds Where Players Compete
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

# The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

# For example, if the row consists of players 1, 2, 4, 6, 7
# Player 1 competes against player 7.
# Player 2 competes against player 6.
# Player 4 automatically advances to the next round.
# After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

# The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

# Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

 

# Example 1:

# Input: n = 11, firstPlayer = 2, secondPlayer = 4
# Output: [3,4]
# Explanation:
# One possible scenario which leads to the earliest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 2, 3, 4, 5, 6, 11
# Third round: 2, 3, 4
# One possible scenario which leads to the latest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 1, 2, 3, 4, 5, 6
# Third round: 1, 2, 4
# Fourth round: 2, 4
# Example 2:

# Input: n = 5, firstPlayer = 1, secondPlayer = 5
# Output: [1,1]
# Explanation: The players numbered 1 and 5 compete in the first round.
# There is no way to make them compete in any other round.
 

# Constraints:

# 2 <= n <= 28
# 1 <= firstPlayer < secondPlayer <= n

# n = 1
# firstPlayer = 2
# secondPlayer = 4

n = 5
firstPlayer = 1
secondPlayer = 5

def xyz(n, firstPlayer, secondPLayer):
    def simplify(n, a, b):
        if a > b:
            a, b = b, a
        if a + b >= n + 1:
            a, b = n + 1 - b, n + 1 - a
        return n, a, b

    def get_info(n, a, b):
        ll = a - 1
        rr = n - b
        aa = n - ll
        bb = 1 + rr
        return ll, rr, aa, bb

    def while_loop(n, a, b):
        ans = 1
        while a + b < n + 1:
            n = (n + 1) // 2
            ans += 1
        if b - a - 1 == 0:
            while n % 2 == 1:
                n = (n + 1) // 2
                ans += 1
        return ans

    def solve_fast(n, a, b):
        n, a, b = simplify(n, a, b)
        if a + b == n + 1:
            return 1
        if b <= (n + 1) // 2:
            return while_loop(n, a, b)

        ll, rr, aa, bb = get_info(n, a, b)
        if ll % 2 == 1 and bb - a - 1 == 0:
            if n % 2 == 0 and b == n // 2 + 1:
                return 1 + while_loop((n + 1) // 2, a, a + 1)
            else:
                return 3
        else:
            return 2

    def solve_slow(n, a, b):
        n, a, b = simplify(n, a, b)
        if a + b == n + 1:
            return 1
        if b <= n + 1 - b:
            return 1 + solve_slow((n + 1) // 2, 1, 2)
        else:
            ll, rr, aa, bb = get_info(n, a, b)
            keep = (b - bb - 1) // 2 + (n % 2)
            return 1 + solve_slow((n + 1) // 2, 1, 2 + keep)

    return [solve_fast(n, firstPlayer, secondPlayer), solve_slow(n, firstPlayer, secondPlayer)]


print(xyz(n,firstPlayer,secondPlayer))