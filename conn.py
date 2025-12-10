import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'MSI\SQLEXPRESS'
DATABASE_NAME = 'employee.db'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABSE={DATABASE_NAME};
    Trust_Connection=yes;
"""


conn = odbc.connect(connection_string)
print(conn)