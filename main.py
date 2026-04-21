from database.connection import create_connection, create_tables

connection = create_connection()
create_tables(connection)

print("Banco gerado com SUCESSO!")