from db import conectar

# Inserir paciente com validação de CPF duplicado
def inserir_paciente(nome, cpf, data_nascimento, telefone):
    con = conectar()
    cur = con.cursor()
    try:
        # Verifica se o CPF já está cadastrado
        cur.execute('SELECT id FROM pacientes WHERE cpf = ?', (cpf,))
        if cur.fetchone():
            print("❌ Já existe um paciente cadastrado com esse CPF.")
            return

        cur.execute(
            'INSERT INTO pacientes (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)',
            (nome, cpf, data_nascimento, telefone)
        )
        con.commit()
        print("✅ Paciente cadastrado com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao inserir paciente: {e}")
    finally:
        con.close()

# Listar todos os pacientes
def listar_pacientes():
    con = conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM pacientes')
    pacientes = cur.fetchall()
    con.close()
    return pacientes

# Atualizar informações do paciente
def atualizar_paciente(paciente_id, nome, cpf, data_nascimento, telefone):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute('''UPDATE pacientes SET nome = ?, cpf = ?, data_nascimento = ?, telefone = ? WHERE id = ?''',
                    (nome, cpf, data_nascimento, telefone, paciente_id))
        con.commit()
        if cur.rowcount == 0:
            print("❌ Paciente não encontrado.")
        else:
            print("✅ Paciente atualizado com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao atualizar paciente: {e}")
    finally:
        con.close()

# Deletar paciente por ID
def deletar_paciente(paciente_id):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM pacientes WHERE id = ?', (paciente_id,))
        con.commit()
        if cur.rowcount == 0:
            print("❌ Paciente não encontrado.")
        else:
            print("✅ Paciente deletado com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao deletar paciente: {e}")
    finally:
        con.close()
