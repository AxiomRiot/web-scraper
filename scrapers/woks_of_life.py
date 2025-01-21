import requests
from scrapers.recipe import Recipe
from bs4 import BeautifulSoup

def get_ingredient(li, className):
  span = li.find('span', class_=className) 
  value = span.text if span else ''
  return value

def scrape_woks_of_life(url):
  r = requests.get(url)

  # Parsing the HTML
  soup = BeautifulSoup(r.content, 'html.parser')

  ingredients = []
  recipe = []

  # Recipe Name
  name = soup.find('h2', class_='wprm-recipe-name').text

  # Recipe Description
  description = soup.find('div', class_='wprm-recipe-summary').text
  
  # Recipe Servings
  servings = soup.find('span', class_='wprm-recipe-servings').text

  # Recipe Duration
  days_span = soup.find('span', class_='wprm-recipe-total_time-days')
  hours_span = soup.find('span', class_='wprm-recipe-total_time-hours')
  minutes_span = soup.find('span', class_='wprm-recipe-total_time-minutes')

  days = days_span.text if days_span else ""
  hours = hours_span.text if hours_span else ""
  minutes = minutes_span.text if minutes_span else ""

  recipe = Recipe(
    name,
    description,
    servings,
    (days, hours, minutes)
  )

  # Recipe Ingredients
  for ingredient_group in soup.find_all('div', class_='wprm-recipe-ingredient-group'):
    ingredient_list = ingredient_group.find('ul', class_='wprm-recipe-ingredients')
    for li in ingredient_list.find_all('li', class_='wprm-recipe-ingredient'):
      recipe.add_ingredient((
        get_ingredient(li, 'wprm-recipe-ingredient-amount'),
        get_ingredient(li, 'wprm-recipe-ingredient-unit'),
        get_ingredient(li, 'wprm-recipe-ingredient-name'),
        get_ingredient(li, 'wprm-recipe-ingredient-notes'),
      ))

  # Recipe Steps
  for recipe_group in soup.find_all('div', class_='wprm-recipe-instruction-group'):
    recipe_list = recipe_group.find('ul', class_='wprm-recipe-instructions')
    for li in recipe_list.find_all('li', class_='wprm-recipe-instruction'):
      recipe_div = li.find('div', class_='wprm-recipe-instruction-text')
      recipe.add_recipe_step(recipe_div.text) if recipe_div.text else recipe.append(recipe_div.find('span').text)

  return recipe