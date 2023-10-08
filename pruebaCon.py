import pandas as pd
from sqlalchemy import create_engine

host = "localhost"
user = "root"
password = ""
database = "migracion_server"
tabla = "hhistorias"

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

consulta_sql = f'SELECT * FROM {tabla}'

df = pd.read_sql_query(consulta_sql, engine)

engine.dispose()

print(df)