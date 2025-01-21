class Recipe:
  def __init__(self, 
               name : str,
               description : str,
               servings : str,
               duration : str):
    
    self.name = name
    self.description = description
    self.servings = servings
    self.duration = duration
    self.ingredients = []
    self.steps = []

  def add_ingredient(self, ingredient):
    self.ingredients.append(ingredient)

  def add_recipe_step(self, step):
    self.steps.append(step)

  def get_all_details(self): 
    return { 
        "name": self.name, 
        "servings": self.servings,
        "description": self.description,
        "duration": self.duration,
        "ingredients": self.ingredients,
        "steps": self.steps 
    }
  
  def display_recipe(self): 
    details = self.get_all_details() 
    print(f"Recipe: {details['name']}") 
    print(f"Servings: {details['servings']}") 
    print(f"Description: {details['description']}") 
    print(f"Duration: {details['duration']}") 
    print("Ingredients:") 
    for ingredient in details['ingredients']: 
      print(f" - {ingredient}") 
    print("Steps:") 
    for i, step in enumerate(details['steps'], 1): 
      print(f"Step {i}: {step}")