from store_connection import connection

# Insert a new client
def create(connection):
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO client(id_client, \
                name_client, lastname, address_c, phone, \
                email) values(?,?,?,?,?,?);"
            cursor.excute(
                query, (
                    9, 'Daniela', 'Silva', 'Cairo',
                    5435632, 'dani@gmail.com'
                    )
            )
            connection.commit()
    except Exception as e:
        print("An error occurred while inserting record: ", e)
    finally:
        cursor.close()
        connection.close()
create(connection)