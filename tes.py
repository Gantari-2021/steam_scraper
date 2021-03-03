import requests
from bs4 import BeautifulSoup



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
url = 'https://store.steampowered.com/games#p=0&tab=TopSellers'
r = requests.get( url, headers=headers )
soup = BeautifulSoup( r.text, 'html.parser' )

top_sellers = soup.find_all( 'a', attrs={'class': 'tab_item'} )

for top_seller in top_sellers:
    print('Titles:', top_seller.find('div', attrs={'class':'tab_item_name'}).text)
    print('Images:', top_seller.find('div', attrs={'class':'tab_item_cap'}).find('img'))
    print('Tags:', top_seller.find('div', attrs={'class':'tab_item_top_tags'}).text)
    print('Price:', top_seller.find('div', attrs={'class':'discount_original_price'}))


