import sqlite3
from sqlite3 import Error

database = r"C:\Users\elcuni\Documents\CODE\datascientest\datascience_DB.db"
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def get_all_article():
  conn = create_connection(database)
  sql = '''SELECT * FROM article;'''
  cur = conn.cursor()
  cur.execute(sql)
  return cur.fetchall()


def get_article_by_name(article_name):
  conn = create_connection(database) 
  sql = '''SELECT * FROM article WHERE name = (:article_name);'''
  cur = conn.cursor()
  cur.execute(sql, {'article_name':article_name})
  return cur.fetchall()


def get_article_by_author(author):
  conn = create_connection(database)
  sql = '''SELECT author.name, article.name, article.link, article.category, article.subcategory, article.date_creation 
           FROM author
           INNER JOIN article_author aa on aa.id_author = author.id
           INNER JOIN article on aa.id_article = article.id
           WHERE author.name = (:author);'''
  cur = conn.cursor()
  cur.execute(sql, {'author':author})
  return cur.fetchall()


def get_article_by_category(category):
  conn = create_connection(database) 
  sql = '''SELECT * FROM article WHERE category = (:category);'''
  cur = conn.cursor()
  cur.execute(sql, {'category': category})
  return cur.fetchall()
