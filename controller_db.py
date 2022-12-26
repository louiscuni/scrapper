from db_filler import *
from scrapper import Scrapper

database = r"C:\Users\elcuni\Documents\CODE\datascientest\datascience_DB.db"

def get_raw_data():
  scrappy = Scrapper()
  scrappy.start_driver()
  scrappy.accept_cookies()
  category = scrappy.get_categories()
  article = []
  author = []
  for c in category.keys():
      current_articles, current_author = scrappy.scrappe_a_category(c, 0)
      article += current_articles
      author += current_author
  return (article, set(author))

def fill_authors(authors):
  conn = create_connection(database)
  with conn:
      for author in authors:
        create_author(conn, (author,))
  close_connection(conn)


def fill_articles(articles):
  conn = create_connection(database)
  for article in articles:
    authors = article['author']
    article_data = (article['article_name'], article['article_link'], article['category'], article['subcategory'], article['date'])
    create_article(conn, article_data)
    article_id = get_article_id(conn, article['article_name'])
    for author in authors:
      author_id = get_author_id(conn, author)
      create_article_author(conn, (article_id, author_id))
  close_connection(conn)


def main():
  articles, authors = get_raw_data()
  fill_authors(authors)
  print('authors done')
  fill_articles(articles)

if __name__ == '__main__':
    main()