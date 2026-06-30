import psycopg2

def connection_pg():
    connection = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        port=5433
    )
    return connection

if __name__ == "__main__":
    conn = connection_pg()
    print("Connected to the database successfully!")
    conn.close()