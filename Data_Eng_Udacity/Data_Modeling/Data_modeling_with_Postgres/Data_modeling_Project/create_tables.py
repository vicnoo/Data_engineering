import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    try:
        '''Creates and connects to sparkifydb database. Returns cursor and connection to DB'''
        # connect to default database
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=Otieno@1125")
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        
        # create sparkify database with UTF8 encoding
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

        # close connection to default database
        conn.close()    
        
        # connect to sparkify database
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=Otieno@1125")
        cur = conn.cursor()
        
        return cur, conn
    except psycopg2.Error as e:
        print(e)


def drop_tables(cur, conn):
    try:
        '''Drops all tables created on the database'''
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        print(e)


def create_tables(cur, conn): 
    try:
        '''Created tables defined on the sql_queries script: [songplays, users, songs, artists, time]'''
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        print(e)


def main():
    try:
        """ Function to drop and re create sparkifydb database and all related tables.
        Usage: python create_tables.py
        """
        cur, conn = create_database()
        
        drop_tables(cur, conn)
        create_tables(cur, conn)

        conn.close()
    except psycopg2.Error as e:
        print(e)


if __name__ == "__main__":
    main()
    
