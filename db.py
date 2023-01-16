import pyodbc
import textwrap

driver="{/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.1.so.2.1}"
server="TCP:SR12-PROD-78162"
database='db.INOT'
conString = textwrap.dedent(f"""\
            Driver={driver};
            Server={server};
            Database={database};
            Trusted_Connection=yes;
            """)
conn = pyodbc.connect(conString)
cursor = conn.cursor()
print(cursor)
conn.close()
