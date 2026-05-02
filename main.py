from database.connection import create_connection, create_tables
from database.dao_users import *

connection = create_connection()
create_tables(connection)

print("Banco gerado com SUCESSO!")


ok, msg = create_user(connection, 89887784, "Eduardo Pereira Guedes", "377039808", "admin")
print(ok, msg)

# ok, msg = delete_user(connection, 89887784)
# print(ok, msg)