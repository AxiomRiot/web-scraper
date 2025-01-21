from scrapers.woks_of_life import scrape_woks_of_life

def main():
  
  (ingredients, recipe) = scrape_woks_of_life('https://thewoksoflife.com/steamed-shanghai-soup-dumplings-xiaolongbao/')

  for ingredient in ingredients:
    print(f"{ingredient[0]} {ingredient[1]} {ingredient[2]} {ingredient[3]}")

  for index, step in enumerate(recipe):
    print(f"{index} {step}")

if __name__ == "__main__":
  main()