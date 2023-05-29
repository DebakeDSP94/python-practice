import bs4
import requests


def getEtsyPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select(
        '#content > div > div.wt-bg-white.wt-grid__item-md-12.wt-pl-xs-1.wt-pr-xs-0.wt-pr-md-1.wt-pl-lg-0.wt-pr-lg-0.wt-bb-xs-1 > div > div.wt-mt-xs-3.wt-text-black > div:nth-child(4) > div > div > div > div.wt-grid__item-xs-7.wt-pl-xs-3 > div:nth-child(3) > div.n-listing-card__price.wt-display-block.wt-text-title-01')

    return elems[0].text.strip()


price = getEtsyPrice(
    'https://www.etsy.com/search?q=mothers+day+gifts&mosv=sese&moci=1145649644711&mosi=1134110538664&ref=hp_bubbles_MDAY23_US_CA&anchor_listing_id=1216601114&is_merch_library=true')
print('The price is ' + price)
