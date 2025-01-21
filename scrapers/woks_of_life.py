import requests
from bs4 import BeautifulSoup

def get_ingredient(li, className):
  span = li.find('span', class_=className) 
  value = span.text if span else ''
  return value

def scrape_woks_of_life(url):
  r = requests.get(url)

  # Parsing the HTML
  soup = BeautifulSoup(r.content, 'html.parser')
  ingredient_list = soup.find('ul', class_='wprm-recipe-ingredients')
  recipe_list = soup.find('ul', class_='wprm-recipe-instructions')

  ingredients = []
  recipe = [] 
  for li in ingredient_list.find_all('li', class_='wprm-recipe-ingredient'):

    ingredients.append((
      get_ingredient(li, 'wprm-recipe-ingredient-amount'),
      get_ingredient(li, 'wprm-recipe-ingredient-unit'),
      get_ingredient(li, 'wprm-recipe-ingredient-name'),
      get_ingredient(li, 'wprm-recipe-ingredient-notes'),
    ))

  for li in recipe_list.find_all('li', class_='wprm-recipe-instruction'):
    recipe_div = li.find('div', class_='wprm-recipe-instruction-text')
    recipe.append(recipe_div.find('span').text)

  return (ingredients, recipe)