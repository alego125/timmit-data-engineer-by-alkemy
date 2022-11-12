# No puede conectarse al servidor ERROR EN EL SERVERNAME
# import pytds
# with pytds.connect('DESKTOP-0L9GVII/SQLEXPRESS', 'SQL_DML', 'timmit', '1234') as conn:
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM Proveedor WHERE Ciudad LIKE '%Ramos%'")
#         informacion = cur.fetchall()
#         print(informacion)
# conn = pytds.connect('DESKTOP-0L9GVII\SQLEXPRESS', 'SQL_DML', 'timmit', 'anubis90')
# cursor = conn.cursor()
# informacion = cursor.fetchall()
# print(informacion)


import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-0L9GVII\SQLEXPRESS;DATABASE=SQL_DML;UID=timmit;PWD=1234')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Proveedor WHERE Ciudad LIKE '%Ramos%'")
informacion = cursor.fetchone()
print(informacion)
