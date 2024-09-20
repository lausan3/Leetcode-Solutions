class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_mappings = {}
        recipe_indegree = {}
        curr_ingredients = deque()
        curr_ingredients.extend(supplies)
        output = []
        
        # build the mappings and indegrees
        for i in range(len(recipes)):
            recipe = recipes[i]
            ingredient_list = ingredients[i]
            recipe_indegree[recipe] = recipe_indegree.get(recipe, len(ingredient_list))
            
            for ingredient in ingredient_list:
                ingredient_mappings[ingredient] = ingredient_mappings.get(ingredient, [])
                ingredient_mappings[ingredient].append(recipe)
            
        while curr_ingredients:
            ingredient = curr_ingredients.popleft()

            if ingredient not in ingredient_mappings:
                continue
            
            recipes_ingredient_makes = ingredient_mappings[ingredient]
            
            for recipe in recipes_ingredient_makes:
                if recipe in recipe_indegree:
                    recipe_indegree[recipe] -= 1
                    
                    if recipe_indegree[recipe] == 0:
                        output.append(recipe)
                        curr_ingredients.append(recipe)
                        
                    
        return output