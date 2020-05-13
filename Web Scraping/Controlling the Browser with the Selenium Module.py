from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
elem.click()
elems = browser.find_elements_by_css_selector('p') #find the paragraphs by using the css tag 'p'
print(len(elems))


elem = browser.find_element_by_css_selector('#calibre_link-1610 > p:nth-child(8)')
print(elem.text) #getting text from a portion of the website
