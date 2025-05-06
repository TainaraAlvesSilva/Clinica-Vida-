from db import conectar

# Inserir médico com validação de CRM duplicado

def inserir_medico(nome, crm, especialidade):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute('SELECT id FROM medicos WHERE crm = ?', (crm,))
        if cur.fetchone():
            print("❌ Já existe um médico cadastrado com esse CRM.")
            return

        cur.execute('INSERT INTO medicos (nome, crm, especialidade) VALUES (?, ?, ?)',
                    (nome, crm, especialidade))
        con.commit()
    except Exception as e:
        print(f"🚨 Erro ao inserir médico: {e}")
    finally:
        con.close()

# Listar todos os médicos cadastrados

def listar_medicos():
    con = conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM medicos')
    medicos = cur.fetchall()
    con.close()
    return medicos

# Atualizar os dados de um médico existente

def atualizar_medico(medico_id, nome, crm, especialidade):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute('''UPDATE medicos SET nome = ?, crm = ?, especialidade = ? WHERE id = ?''',
                    (nome, crm, especialidade, medico_id))
        con.commit()
        if cur.rowcount == 0:
            print("❌ Médico não encontrado.")
        else:
            print("✅ Médico atualizado com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao atualizar médico: {e}")
    finally:
        con.close()

# Remover médico do sistema

def deletar_medico(medico_id):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM medicos WHERE id = ?', (medico_id,))
        con.commit()
        if cur.rowcount == 0:
            print("❌ Médico não encontrado.")
        else:
            print("✅ Médico deletado com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao deletar médico: {e}")
    finally:
        con.close()