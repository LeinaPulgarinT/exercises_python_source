from store_connection import connection

# Insert a new client
def update(connection):
    try:
        with connection.cursor() as cursor:
            query = 'UPDATE client SET  address_c = ? \
                WHERE id_client = ?;'

            cursor.execute(query, ('Cali', 9))
            connection.commit()
    except Exception as e:
        print("An error occurred while updating record: ", e)
    finally:
        cursor.close()
        connection.close()
update(connection)
