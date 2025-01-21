from scrapers.woks_of_life import scrape_woks_of_life

def main():
  
  (ingredients, recipe) = scrape_woks_of_life('https://thewoksoflife.com/steamed-shanghai-soup-dumplings-xiaolongbao/')
  print(ingredients)

if __name__ == "__main__":
  main()