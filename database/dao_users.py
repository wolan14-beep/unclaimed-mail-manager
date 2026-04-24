import sqlite3

def create_user(connection, registration, name, cpf, profile):
    cursor = None    
    try:        
        insert_users_sql = 'INSERT INTO users (registration, name, cpf, profile) VALUES (?, ?, ?, ?)'

        cursor=connection.cursor()

        cursor.execute(insert_users_sql, (registration, name, cpf, profile))

        connection.commit()
        return True, "Usuário cadastrado com Sucesso!"
    
    except sqlite3.IntegrityError:
        return False, "Usuário já cadastrado."
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()

def get_user_by_registration(connection, registration, cpf):
    cursor = None
    try:
        cursor = connection.cursor()

        look_for_users = 'SELECT * FROM users WHERE registration = ? AND cpf = ?'
        cursor.execute(look_for_users, (registration, cpf))

        user = cursor.fetchone()

        if user:
            return user
        else:
            return "User not found"

        
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()