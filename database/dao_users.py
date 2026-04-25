import sqlite3

def create_user(connection, registration, name, cpf, profile):
    cursor = None    
    try:        
        insert_users_sql = 'INSERT INTO users (registration, name, cpf, profile) VALUES (?, ?, ?, ?)'

        cursor=connection.cursor()

        cursor.execute(insert_users_sql, (registration, name, cpf, profile))

        connection.commit()
        return True, "Usuário cadastrado com Sucesso!"
    
    except sqlite3.IntegrityError as error:
        msg = str(error)
        if "UNIQUE" in msg:
            return False, "Usuário já cadastrado."
        elif "CHECK" in msg:
            return False, "Perfil Inválido"
        else:
            return False, f'Erro de Integridade {error}'
        
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

      
        
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()

def get_all_users(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
          
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()

def update_user(connection, registration, name, cpf, profile):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute('UPDATE users SET name = ?, cpf = ?, profile = ? WHERE registration = ?', (name, cpf, profile, registration))

        connection.commit()
        return True, "Cadastro alterado com Sucesso!"
    
    except sqlite3.IntegrityError as error:
        msg = str(error)
        if "UNIQUE" in msg:
            return False, "CPF já cadastrado."
        elif "CHECK" in msg:
            return False, "Perfil inválido"
        else:
            return False, f"Erro de integridade: {error}"
        
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()

def delete_user(connection, registration):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM users WHERE registration = ?', (registration,))
        connection.commit()
        return True, "Usuário excluído com Sucesso!"
    except sqlite3.OperationalError as error:
        return False, f"Erro de acesso ao banco de dados: {error}"
    except sqlite3.Error as error:
        return False, f"Erro no banco de dados: {error}"
    finally:
        if cursor:
            cursor.close()
