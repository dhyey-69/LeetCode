# 1106. Parsing A Boolean Expression

# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.

# It is guaranteed that the given expression is valid and follows the given rules.

 

# Example 1:

# Input: expression = "&(|(f))"
# Output: false
# Explanation: 
# First, evaluate |(f) --> f. The expression is now "&(f)".
# Then, evaluate &(f) --> f. The expression is now "f".
# Finally, return false.
# Example 2:

# Input: expression = "|(f,f,f,t)"
# Output: true
# Explanation: The evaluation of (false OR false OR false OR true) is true.
# Example 3:

# Input: expression = "!(&(f,t))"
# Output: true
# Explanation: 
# First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
# Then, evaluate !(f) --> NOT false --> true. We return true.
 

# Constraints:

# 1 <= expression.length <= 2 * 104
# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

e = "&(|(f))"

def xyz(expression):
    def parse(expr):
        if expr == 't':
            return True
        if expr == 'f':
            return False
        if expr[0] == '!':
            return parse_not(expr)
        if expr[0] == '&':
            return parse_and(expr)
        if expr[0] == '|':
            return parse_or(expr)
        
    # Helper to parse OR expressions
    def parse_or(expr):
        # Strip the | and parentheses, then split by comma
        sub_exprs = split_expression(expr[2:-1])
        # Evaluate each subexpression, return True if any is True
        return any(parse(sub) for sub in sub_exprs)
        
    # Helper to parse AND expressions
    def parse_and(expr):
        # Strip the & and parentheses, then split by comma
        sub_exprs = split_expression(expr[2:-1])
        # Evaluate each subexpression, return False if any is False
        return all(parse(sub) for sub in sub_exprs)
        
    # Helper to parse NOT expressions
    def parse_not(expr):
        # Strip the ! and parentheses, then evaluate the inner expression
        return not parse(expr[2:-1])
        
    # Utility function to split expressions at the top level
    # We need this to handle splitting sub-expressions at commas outside parentheses
    def split_expression(expr):
        sub_exprs = []
        balance = 0
        current_expr = []
        for char in expr:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if char == ',' and balance == 0:
                sub_exprs.append(''.join(current_expr))
                current_expr = []
            else:
                current_expr.append(char)
        sub_exprs.append(''.join(current_expr))  # Add the last expression
        return sub_exprs

    # Start parsing the full expression
    return parse(expression)

print(xyz(e))