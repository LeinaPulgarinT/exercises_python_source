import pyodbc
server = '127.0.0.1'
name_db = 'store'
user_name = 'sa'
password = 'Yonomelase1.,'

# connect python with database
try:
    connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
    server+';DATABASE='+name_db+';UID='+user_name+';PWD=' + password
    )
except Exception as e:
    print("An error occurred connecting SQL Server: ", e)

