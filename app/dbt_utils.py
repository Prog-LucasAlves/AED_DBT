import subprocess
import os

DBT_PROJECT_PATH = os.path.abspath("./dbt_project")


def run_dbt_model(mode_name):

    try:

        command = ["dbt", "run", "--model", mode_name]
        result = subprocess.run(command, cwd=DBT_PROJECT_PATH, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Modelo {mode_name} executado com sucesso.")
        else:
            print(f"❌ Erro ao executar o modelo {mode_name}.")

    except Exception as e:
        return f"⚠️ Erro inesperado: {str(e)}"


def list_dbt_models():
    try:
        result = subprocess.run(["dbt", "ls", "--resource-type", "model"], capture_output=True, text=True)

        if result.returncode == 0:
            models = result.stdout.strip().split("\n")
            return models if models else ["Nenhum modelo encontrado."]
        else:
            return [f"❌ Erro ao listar modelos: {result.stderr}"]

    except Exception as e:
        return [f"❌ Erro ao executar o DBT: {str(e)}"]
