import pyodbc
import textwrap

driver="{/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.1.so.2.1}"
server="SR12-PROD-78162"
conString = textwrap.dedent(f"""\
            Driver={driver};
            Server={server};
            Trusted_Connection=yes;
            """)

print(conString)
conn = pyodbc.connect(conString)
cursor = conn.cursor()
