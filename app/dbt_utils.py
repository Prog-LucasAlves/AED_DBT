import subprocess
import os

# Caminho do projeto DBT
DBT_PROJECT_PATH = os.path.abspath("./dbt_project")


# Função para encontrar o caminho do dbt no Render
def get_dbt_path():
    dbt_path = subprocess.run(["which", "dbt"], capture_output=True, text=True).stdout.strip()

    if not dbt_path:
        dbt_path = "/opt/render/project/src/.venv/bin/dbt"  # Caminho padrão no Render

    return dbt_path


DBT_PATH = get_dbt_path()


def list_dbt_models():
    """ Lista todos os modelos DBT disponíveis no projeto. """
    try:
        if not os.path.exists(DBT_PATH):
            return ["❌ DBT não encontrado. Verifique a instalação."]

        command = [DBT_PATH, "dbt", "ls", "--resource-type", "model"]
        result = subprocess.run(command, cwd=DBT_PROJECT_PATH, capture_output=True, text=True)

        if result.returncode == 0:
            models = result.stdout.strip().split("\n")
            return models if models else ["Nenhum modelo encontrado."]
        else:
            return [f"❌ Erro ao listar modelos: {result.stderr}"]

    except Exception as e:
        return [f"⚠️ Erro inesperado ao listar modelos: {str(e)}"]
