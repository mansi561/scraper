from autoscraper import AutoScraper

amazon_url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps"

wanted_list=["₹2,849","Red Lemon Swisslook Polyester Bange Series 45L 15.6-inch Laptop Bags Backpack for Men and Women Waterproof USB Anti Theft Travel Backpack","1,253"]


scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)


