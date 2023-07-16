import pypyodbc as odbc 

DRIVE_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-U7K3B00\SQL2022'
DATABASE_NAME = 'one'

connection = f"""
    DRIVER={{{DRIVE_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
conn = odbc.connect(connection)
print(conn)