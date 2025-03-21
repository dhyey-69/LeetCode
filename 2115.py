# Code
# Testcase
# Test Result
# Test Result
# 2115. Find All Possible Recipes from Given Supplies
# Medium
# Topics
# Companies
# Hint
# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

 

# Example 1:

# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# Example 2:

# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# Example 3:

# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

# Constraints:

# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.

# r = ["bread"]
# i = [["yeast","flour"]]
# s = ["yeast","flour","corn"]

# r = ["bread","sandwich"]
# i = [["yeast","flour"],["bread","meat"]]
# s = ["yeast","flour","meat"]

r = ["bread","sandwich","burger"]
i = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
s = ["yeast","flour","meat"]



def xyz(recipes,ingredients,supplies):
        graph = {}
        in_degree = {recipe: 0 for recipe in recipes}
        
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        queue = list(supplies)
        available_recipes = set(supplies)
        result = []
        
        while queue:
            ingredient = queue.pop(0)
            
            if ingredient in graph:
                for recipe in graph[ingredient]:
                    in_degree[recipe] -= 1
                    if in_degree[recipe] == 0:
                        result.append(recipe)
                        queue.append(recipe)
                        available_recipes.add(recipe)
        
        return result


print(xyz(r,i,s))