from db import conectar
from datetime import datetime

# Função para agendar uma nova consulta
def agendar_consulta(paciente_id, medico_id, data, observacoes):
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute(
            'INSERT INTO consultas (paciente_id, medico_id, data, observacoes) VALUES (?, ?, ?, ?)',
            (paciente_id, medico_id, data, observacoes)
        )
        con.commit()
        print("✅ Consulta agendada com sucesso.")
    except Exception as e:
        print(f"🚨 Erro ao agendar consulta: {e}")
    finally:
        con.close()

# Função para listar consultas por paciente
from db import conectar

def listar_consultas_por_paciente(paciente_id, detalhado=False):
    con = conectar()
    cur = con.cursor()
    if detalhado:
        cur.execute('''
            SELECT c.data, c.observacoes, m.nome AS medico
            FROM consultas c
            JOIN medicos m ON c.medico_id = m.id
            WHERE c.paciente_id = ?
            ORDER BY c.data
        ''', (paciente_id,))
        resultados = cur.fetchall()
        con.close()
        return [
            f"🗓 {linha[0]} - 🧑‍⚕️ {linha[2]} - 💬 {linha[1]}"
            for linha in resultados
        ]
    else:
        cur.execute('SELECT * FROM consultas WHERE paciente_id = ?', (paciente_id,))
        resultados = cur.fetchall()
        con.close()
        return resultados
