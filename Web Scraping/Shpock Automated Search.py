from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.shpock.com/en-gb')

searchElem = browser.find_element_by_css_selector('#navSearch_search-input') #copy selector
searchElem.send_keys('iPhone X') #search request item
searchElem.submit() #sumbit the search request

browser.back() #go back on the browser
browser.forward()
browser.refresh()
browser.quit()
