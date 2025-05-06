from db import conectar
import csv
import os
from datetime import datetime

# Consulta o número de consultas por médico usando LEFT JOIN

def gerar_relatorio_geral_por_medico():
    con = conectar()
    cur = con.cursor()
    cur.execute('''
        SELECT m.nome, COUNT(c.id) as total
        FROM medicos m
        LEFT JOIN consultas c ON m.id = c.medico_id
        GROUP BY m.id
    ''')
    relatorio = cur.fetchall()
    con.close()
    return relatorio

# Exporta os dados do relatório para um arquivo CSV com timestamp
from db import conectar
import csv

def consultas_por_medico():
    con = conectar()
    cur = con.cursor()
    cur.execute('''
        SELECT m.nome, COUNT(c.id) as total
        FROM medicos m
        LEFT JOIN consultas c ON m.id = c.medico_id
        GROUP BY m.id
    ''')
    relatorio = cur.fetchall()
    con.close()
    return relatorio

    # Cração do relatorio por médico
def exportar_relatorio_medico_csv(medico_id=None, detalhado=False, caminho=None):
    con = conectar()
    cur = con.cursor()

    if detalhado and medico_id is not None:
        cur.execute('''
            SELECT m.nome, p.nome, c.data, c.observacoes
            FROM consultas c
            JOIN medicos m ON c.medico_id = m.id
            JOIN pacientes p ON c.paciente_id = p.id
            WHERE m.id = ?
            ORDER BY c.data
        ''', (medico_id,))
        dados = cur.fetchall()
        cabecalho = ['Médico', 'Paciente', 'Data', 'Observações']
    else:
        dados = consultas_por_medico()
        cabecalho = ['Nome do Médico', 'Número de Consultas']

    con.close()

    # Garante que a pasta "relatorios" exista
    if not caminho:
        if not os.path.exists("relatorios"):
            os.makedirs("relatorios")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = f"relatorios/relatorio_consultas_{timestamp}.csv"

    with open(caminho, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cabecalho)
        writer.writerows(dados)
    print(f"✅ Relatório exportado para: {caminho}")
