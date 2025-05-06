import sqlite3
import os

# Define o caminho relativo ao banco de dados
CAMINHO_DB = os.path.join(os.path.dirname(__file__), 'vida_mais.db')

# Função de conexão com o SQLite
def conectar():
    return sqlite3.connect(CAMINHO_DB)

# Função para criar as tabelas se ainda não existirem
def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL UNIQUE,
            especialidade TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            data_nascimento TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER,
            medico_id INTEGER,
            data TEXT NOT NULL,
            observacoes TEXT,
            FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY(medico_id) REFERENCES medicos(id)
        )
    ''')

    con.commit()
    con.close()
