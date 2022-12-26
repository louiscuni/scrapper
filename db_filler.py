import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def close_connection(conn):
    conn.close()


def create_article(conn, article):
    sql = ''' INSERT OR IGNORE INTO article(name, link, category, subcategory, date_creation)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, article)
    conn.commit()
    return cur.lastrowid


def get_article_id(conn, article):
    author_id_sql = '''SELECT id FROM article WHERE name = (:article)'''
    cur = conn.cursor()
    cur.execute(author_id_sql, {'article': article})
    res = cur.fetchone()[0]
    return res


def create_author(conn, author):
    sql = ''' INSERT OR IGNORE INTO author(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, author)
    conn.commit()
    return cur.lastrowid


def get_author_id(conn, author):
    author_id_sql = '''SELECT id FROM author WHERE name = (:author)'''
    cur = conn.cursor()
    cur.execute(author_id_sql, {'author': author})
    res = cur.fetchone()[0]
    return res


def create_article_author(conn, article_author):
    sql = ''' INSERT OR IGNORE INTO article_author(id_article, id_author)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, article_author)
    conn.commit()
    return cur.lastrowid
