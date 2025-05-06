import csv
import json
from models.medico import inserir_medico
from models.paciente import inserir_paciente

def carregar_medicos_csv(path):
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if all(row.get(k, '').strip() for k in ('nome', 'crm', 'especialidade')):
                    inserir_medico(row['nome'].strip(), row['crm'].strip(), row['especialidade'].strip())
                else:
                    print(f"⚠ Dados incompletos ignorados: {row}")
        print("✅ Médicos importados com sucesso.")
    except FileNotFoundError:
        print(f"❌ Arquivo '{path}' não encontrado.")
    except Exception as e:
        print(f"🚨 Erro ao importar médicos: {e}")

def importar_pacientes_json(path):
    try:
        with open(path, encoding='utf-8') as jsonfile:
            pacientes = json.load(jsonfile)
            for p in pacientes:
                if all(p.get(k, '').strip() for k in ('nome', 'cpf', 'data_nascimento', 'telefone')):
                    inserir_paciente(p['nome'].strip(), p['cpf'].strip(), p['data_nascimento'].strip(), p['telefone'].strip())
                else:
                    print(f"⚠ Dados incompletos ignorados: {p}")
        print("✅ Pacientes importados com sucesso.")
    except FileNotFoundError:
        print(f"❌ Arquivo '{path}' não encontrado.")
    except json.JSONDecodeError:
        print(f"❌ Erro ao ler o JSON: formato inválido em '{path}'.")
    except Exception as e:
        print(f"🚨 Erro ao importar pacientes: {e}")