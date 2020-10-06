from store_connection import connection

# Delete a record
def delete(connection):
    try:
        with connection.cursor() as cursor:
            query = 'DELETE FROM client WHERE id_client = ?;'

            cursor.execute(query, (9))
            connection.commit()
    except Exception as e:
        print("An error occurred while deleting record: ", e)
    finally:
        cursor.close()
        connection.close()
delete(connection)