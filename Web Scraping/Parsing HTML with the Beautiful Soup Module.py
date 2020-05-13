import bs4
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
# use headers to seem like a real person and not a bot

res = requests.get('https://www.shpock.com/en-gb/i/XpmCRmj-WmYKGPKa/airpod-pros', headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser') # html.parser --> gets rid of the warning tells python we are going to parse html
elems = soup.select('''#__next > div.Box-sc-1u5jpde-0.Page__Stretch-sc-1ci33si-0.jvNtNw > div.Box-sc-1u5jpde-0.bvVOVO >
div > div.Grid-v1gqlc-0.iaRTXw > div.Column-g2ubk8-0.hQRHjG > div.Box-sc-1u5jpde-0.gVHmXL > p > span''') #copy css path from inspect element of price (copy selector)
print(elems[0].text.strip())

