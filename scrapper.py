from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Scrapper:
  URL = 'https://techcrunch.com/'
  URL_ = 'https://techcrunch.com'
  CATEGORIES = ['Startups', 'Venture', 'Security', 'Crypto', 'Apps']

  def __init__(self):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless=chrome') bug to fix
    self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
    self.categories = {}


  def start_driver(self):
    self.driver.get(self.URL)
    self.driver.maximize_window() 
    self.driver.implicitly_wait(1) 


  def accept_cookies(self):
    self.driver.find_element(By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button[1]').click()
    print("cookies accepted")


  def get_categories(self):
    try:
      element = WebDriverWait(self.driver, 15).until(
          EC.presence_of_element_located((By.CLASS_NAME,"desktop-nav__body"))
      )
    except AttributeError as e:
      print('error in finding category')
      print(e)
    print("categories found")

    soup = BeautifulSoup(self.driver.page_source, 'lxml')
    navigation_menu = soup.find_all("ul", class_="navigation__main-menu")
    categories = {}
    for category in navigation_menu:
      for li in category.find_all('li', class_='menu__item'):
        if li.contents[0].text in self.CATEGORIES:
          categories[li.contents[0].text] = li.contents[0]['href']
    self.categories = categories
    return categories


  def scrappe_a_category(self, category, deepness):
    self.driver.get(self.URL_ + self.categories[category])
    self.driver.implicitly_wait(5) # gives an implicit wait 

    soup = self.find_more(deepness)
    articles = soup.find_all("article")
    print('articles found', len(articles))
    article_data = []
    author_data = []
    for article in articles:
      article_category = self.get_article_category(article)
      article_name = article.find('h2', class_='post-block__title').contents[0].text
      article_link = article.find('h2', class_='post-block__title').contents[0]['href']
      article_meta_data = article.find('div', class_='post-block__meta')
      author = self.get_article_authors(article_meta_data)
      date = article_meta_data.find('time')['datetime']
      author_data += author
      article_data.append({'article_name' : article_name, 'category': category, 'subcategory' : article_category, 'article_link': article_link, 'author': author, 'date': date})
    return (article_data, author_data)


  def find_more(self, deepness):
    for d in range(deepness):  
      try:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="tc-main-content"]/div/div[2]/button'))
        )
        print("more button found")
      except Error as e: 
        print('cant find more button')
        print(e)
      more = self.driver.find_element(By.XPATH,'//*[@id="tc-main-content"]/div/div[2]/button')
      
      self.driver.execute_script("arguments[0].click();", more)
      print('more button clicked', d)
      time.sleep(5) 
    return BeautifulSoup(self.driver.page_source, 'lxml')


  def get_article_category(self, article_soup):
    try : 
        article_category = article_soup.find('div', class_='article__primary-category').contents[0].text
    except AttributeError:
      try :
        article_category = article_soup.find('h3', class_='article__event-title').contents[0].text
      except AttributeError:
        try :
          article_category = article_soup.find('a', class_='premium-content__link').text
        except AttributeError:
          print('cant find subcategory')
          article_category = 'unknown'
    return article_category


  def get_article_authors(self, article_meta_data_soup):
    res = []
    authors = article_meta_data_soup.find_all('a')
    for author in authors:
      res.append(author.text)
    return res
