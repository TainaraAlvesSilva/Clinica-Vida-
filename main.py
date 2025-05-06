from db import criar_tabelas
from models.medico import listar_medicos, inserir_medico, atualizar_medico, deletar_medico
from models.paciente import listar_pacientes, inserir_paciente, atualizar_paciente, deletar_paciente
from models.consulta import agendar_consulta, listar_consultas_por_paciente
from utils.geracao_relatorios import gerar_relatorio_geral_por_medico, exportar_relatorio_medico_csv
from utils.importadores import carregar_medicos_csv, importar_pacientes_json

from datetime import datetime
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def entrada_obrigatoria(msg):
    valor = input(msg).strip()
    while not valor:
        print("\033[93m⚠ Campo obrigatório. Tente novamente.\033[0m")
        valor = input(msg).strip()
    return valor

def entrada_inteiro(msg):
    while True:
        try:
            return int(entrada_obrigatoria(msg))
        except ValueError:
            print("\033[91m⚠ Valor inválido. Digite um número inteiro.\033[0m")

def entrada_data(msg):
    while True:
        valor = entrada_obrigatoria(msg)
        try:
            datetime.strptime(valor, "%Y-%m-%d")
            return valor
        except ValueError:
            print("\033[91m⚠ Data inválida. Use o formato AAAA-MM-DD.\033[0m")

def entrada_cpf(msg):
    while True:
        cpf = entrada_obrigatoria(msg)
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print("\033[91m⚠ CPF inválido. Deve conter 11 dígitos numéricos.\033[0m")

def menu():
    print("\033[95m\n═══════════════════════════════════\033[0m")
    print("\033[1m\033[94m        Clínica Popular Vida+       \033[0m")
    print("\033[95m═══════════════════════════════════\033[0m")
    print("\033[96m1.📥 Carregar dados iniciais")  # REINSERIDA
    print("2.🩺 CRUD Médico")
    print("3.🧍 CRUD Paciente")
    print("4.📅 Agendar consulta")
    print("5.📖 Consultas de um paciente")
    print("6.📊 Relatório: Consultas por médico")
    print("7.📤 Exportar relatório CSV")
    print("0.🚪 Sair\033[0m")
    print("\033[95m───────────────────────────────────\033[0m")


def menu_crud_medico():
    print("\033[94m\n━━━━ CRUD Médico ━━━━\033[0m")
    print("\033[96m1.➕ Cadastrar médico")
    print("2.📋 Listar médicos")
    print("3.✏️ Atualizar médico")
    print("4.🗑️ Deletar médico")
    print("0.🔙 Voltar\033[0m")
    print("\033[95m───────────────────────\033[0m")

def menu_crud_paciente():
    print("\033[94m\n━━━━ CRUD Paciente ━━━━\033[0m")
    print("\033[96m1.➕ Cadastrar paciente")
    print("2.📋 Listar pacientes")
    print("3.✏️ Atualizar paciente")
    print("4.🗑️ Deletar paciente")
    print("0.🔙 Voltar\033[0m")
    print("\033[95m──────────────────────────\033[0m")

def crud_medico():
    while True:
        try:
            menu_crud_medico()
            op = input("Escolha uma opção: ")
            if op == '1':
                nome = entrada_obrigatoria("Nome: ")
                crm = entrada_obrigatoria("CRM: ")
                esp = entrada_obrigatoria("Especialidade: ")
                inserir_medico(nome, crm, esp)
                print("\033[92m✅ Médico cadastrado com sucesso.\033[0m")
            elif op == '2':
                medicos = listar_medicos()
                if not medicos:
                    print("\033[93m⚠ Nenhum médico cadastrado.\033[0m")
                else:
                    for m in medicos:
                        print(m)
            elif op == '3':
                medico_id = entrada_inteiro("ID do médico: ")
                nome = entrada_obrigatoria("Nome: ")
                crm = entrada_obrigatoria("CRM: ")
                esp = entrada_obrigatoria("Especialidade: ")
                atualizar_medico(medico_id, nome, crm, esp)
            elif op == '4':
                medico_id = entrada_inteiro("ID do médico a ser deletado: ")
                deletar_medico(medico_id)
            elif op == '0':
                break
            else:
                print("\033[91m❌ Opção inválida.\033[0m")
        except Exception as e:
            print(f"\033[91m🚨 Erro inesperado: {e}\033[0m")

def crud_paciente():
    while True:
        try:
            menu_crud_paciente()
            op = input("Escolha uma opção: ")
            if op == '1':
                nome = entrada_obrigatoria("Nome: ")
                cpf = entrada_cpf("CPF (somente números): ")
                nasc = entrada_data("Data de Nascimento (AAAA-MM-DD): ")
                tel = entrada_obrigatoria("Telefone: ")
                inserir_paciente(nome, cpf, nasc, tel)
                print("\033[92m✅ Paciente cadastrado com sucesso.\033[0m")
            elif op == '2':
                pacientes = listar_pacientes()
                if not pacientes:
                    print("\033[93m⚠ Nenhum paciente cadastrado.\033[0m")
                else:
                    for p in pacientes:
                        print(p)
            elif op == '3':
                paciente_id = entrada_inteiro("ID do paciente: ")
                nome = entrada_obrigatoria("Nome: ")
                cpf = entrada_cpf("CPF (somente números): ")
                nasc = entrada_data("Data de Nascimento (AAAA-MM-DD): ")
                tel = entrada_obrigatoria("Telefone: ")
                atualizar_paciente(paciente_id, nome, cpf, nasc, tel)
            elif op == '4':
                paciente_id = entrada_inteiro("ID do paciente a ser deletado: ")
                deletar_paciente(paciente_id)
            elif op == '0':
                break
            else:
                print("\033[91m❌ Opção inválida.\033[0m")
        except Exception as e:
            print(f"\033[91m🚨 Erro inesperado: {e}\033[0m")
def executar():
    criar_tabelas()
    while True:
        try:
            menu()
            op = input("Escolha uma opção: ")

            if op == '1':
                from utils.importadores import carregar_medicos_csv, importar_pacientes_json
                carregar_medicos_csv('data/medicos.csv')
                importar_pacientes_json('data/pacientes.json')
                print("\033[92m✅ Dados carregados com sucesso.\033[0m")

            elif op == '2':
                crud_medico()

            elif op == '3':
                crud_paciente()

            elif op == '4':
                pacientes = listar_pacientes()
                if not pacientes:
                    print("\033[93m⚠ Nenhum paciente cadastrado.\033[0m")
                    continue
                print("\033[96mPacientes disponíveis:\033[0m")
                for p in pacientes:
                    print(p)

                paciente_id = entrada_inteiro("ID do paciente: ")
                if not any(p[0] == paciente_id for p in pacientes):
                    print("\033[91m❌ Paciente não encontrado.\033[0m")
                    continue

                medicos = listar_medicos()
                if not medicos:
                    print("\033[93m⚠ Nenhum médico cadastrado.\033[0m")
                    continue
                print("\033[96mMédicos disponíveis:\033[0m")
                for m in medicos:
                    print(m)

                medico_id = entrada_inteiro("ID do médico: ")
                if not any(m[0] == medico_id for m in medicos):
                    print("\033[91m❌ Médico não encontrado.\033[0m")
                    continue

                data = entrada_data("Data da consulta (AAAA-MM-DD): ")
                obs = entrada_obrigatoria("Observações: ")
                agendar_consulta(paciente_id, medico_id, data, obs)
                print("\033[92m✅ Consulta agendada com sucesso.\033[0m")

            elif op == '5':
                pid = entrada_inteiro("ID do paciente: ")
                consultas = listar_consultas_por_paciente(pid, detalhado=True)
                if consultas:
                    print("\033[96m━━ Consultas deste paciente ━━\033[0m")
                    for c in consultas:
                        print(c)
                else:
                    print("\033[93m⚠ Nenhuma consulta encontrada para este paciente.\033[0m")

            elif op == '6':
                relatorio = gerar_relatorio_geral_por_medico()
                if relatorio:
                    print("\033[96m━━ Consultas por Médico ━━\033[0m")
                    for r in relatorio:
                        print(f"👨‍⚕️ {r[0]} - 📊 {r[1]} consulta(s)")
                else:
                    print("\033[93m⚠ Nenhuma consulta registrada ainda.\033[0m")

            elif op == '7':
                medicos = listar_medicos()
                if not medicos:
                    print("\033[93m⚠ Nenhum médico cadastrado.\033[0m")
                else:
                    print("\033[96mMédicos disponíveis:\033[0m")
                    for m in medicos:
                        print(m)

                    medico_id = entrada_inteiro("Digite o ID do médico para exportar as consultas: ")
                    exportar_relatorio_medico_csv(medico_id=medico_id, detalhado=True)
                    print("\033[92m✅ Relatório exportado com sucesso.\033[0m")

            elif op == '0':
                print("\033[92m👋 Encerrando o sistema. Até logo!\033[0m")
                break

            else:
                print("\033[91m❌ Opção inválida.\033[0m")

        except Exception as e:
            print(f"\033[91m🚨 Erro inesperado: {e}\033[0m")

if __name__ == '__main__':
    executar()