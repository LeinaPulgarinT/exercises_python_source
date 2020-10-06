from store_connection import connection

# Read client table from store database
def read(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM client;')
            
            clients = cursor.fetchall()
            for client in clients:
                print(client[0])
            
            # por si quiero acceder a un solo registro
            #print(clients[0][0])
    except Exception as e:
        print("An error occurred while query: ", e)
    finally:
        connection.close()
#read(connection)

# Read client table from store database using fetchone()
def read(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM client;')
            
            client = cursor.fetchone()
            while client:
                print(client)
                client = cursor.fetchone()

    except Exception as e:
        print("An error occurred while query: ", e)
    finally:
        connection.close()

#read(connection)

# Read client table from store database using WHERE and LIKE
def read(connection):
    try:
        with connection.cursor() as cursor:
            query = 'SELECT * FROM client WHERE lastname like ?;'
            search = 'st'
            cursor.execute(query, (f'c%{search}%'))

            client = cursor.fetchone()
            while client:
                print(client)
                client = cursor.fetchone()

    except Exception as e:
        print("An error occurred while query: ", e)
    finally:
        cursor.close()
        connection.close()

read(connection)