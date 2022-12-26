import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print('wut')
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = Path.cwd() + "\datascience_DB.db"
    
    sql_create_article_table = """ CREATE TABLE IF NOT EXISTS article (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL UNIQUE,
                                        link text NOT Null,
                                        category text NOT Null,
                                        subcategory text NOT Null,
                                        date_creation text NOT Null
                                    ); """

    sql_create_author_table = """CREATE TABLE IF NOT EXISTS author (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL UNIQUE
                                );"""

    sql_create_article_author_table = """CREATE TABLE IF NOT EXISTS article_author (
                                        id_article integer NOT NULL,
                                        id_author integer NOT NULL,
                                        PRIMARY KEY (id_article, id_author),
                                        FOREIGN KEY (id_article) REFERENCES article (id),
                                        FOREIGN KEY (id_author) REFERENCES author (id)
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_article_table)

        # create tasks table
        create_table(conn, sql_create_author_table)

        # create tasks table
        create_table(conn, sql_create_article_author_table)
        print("done")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()