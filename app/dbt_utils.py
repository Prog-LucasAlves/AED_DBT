import subprocess
import os

# Caminho do projeto DBT (altere se necessário)
DBT_PROJECT_PATH = os.getenv("PATH")


def run_dbt_model(model_name):
    """
    Executa um modelo DBT específico.

    :param model_name: Nome do modelo a ser executado
    :return: Mensagem de sucesso ou erro
    """
    try:
        command = ["dbt", "run", "--model", model_name]
        result = subprocess.run(command, cwd=DBT_PROJECT_PATH, capture_output=True, text=True)

        if result.returncode == 0:
            return f"✅ Modelo {model_name} executado com sucesso.\n\n{result.stdout}"
        else:
            return f"❌ Erro ao executar o modelo {model_name}.\n\n{result.stderr}"

    except Exception as e:
        return f"⚠️ Erro inesperado: {str(e)}"


def list_dbt_models():
    """
    Lista todos os modelos DBT disponíveis no projeto.

    :return: Lista de nomes dos modelos ou mensagem de erro
    """
    try:
        command = ["dbt", "ls", "--resource-type", "model"]
        result = subprocess.run(command, cwd=DBT_PROJECT_PATH, capture_output=True, text=True)

        if result.returncode == 0:
            models = result.stdout.strip().split("\n")
            return models if models else ["Nenhum modelo encontrado."]
        else:
            return [f"❌ Erro ao listar modelos: {result.stderr}"]

    except Exception as e:
        return [f"⚠️ Erro inesperado ao listar modelos: {str(e)}"]
