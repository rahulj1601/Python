import bs4, requests, pyperclip

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('''#__next > div.Box-sc-1u5jpde-0.Page__Stretch-sc-1ci33si-0.jvNtNw > div.Box-sc-1u5jpde-0.bvVOVO >
div > div.Grid-v1gqlc-0.iaRTXw > div.Column-g2ubk8-0.hQRHjG > div.Box-sc-1u5jpde-0.gVHmXL > p > span''')
    return elems[0].text.strip()


price = getAmazonPrice(pyperclip.paste())
print("The price is " + price)
