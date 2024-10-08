# pytrobot/cli/__main__.py
import click
import shutil
from pathlib import Path
from datetime import datetime

# Caminhos base para os scaffolds
from pytrobot.scaffold.state import project as state_project_scaffold
from pytrobot.scaffold.sqs import project as celery_project_scaffold
from pytrobot.scaffold.state import new_state as new_state_file
from pytrobot.scaffold.state import test_new_state as test_state_file
from pytrobot.scaffold.sqs import new_task as new_task_file
from pytrobot.scaffold.sqs import test_new_task as test_task_file

@click.group()
def cli():
    """CLI para gerenciar scaffolds do PyTrobot."""
    pass

def copy_project(src: Path, dest: Path):
    """Função auxiliar para copiar um projeto inteiro ignorando a pasta '__pycache__'."""
    try:
        if src.is_dir():
            # Adiciona lógica para ignorar '__pycache__'
            shutil.copytree(
                src, 
                dest, 
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns('__pycache__')
            )
        else:
            shutil.copy(src, dest)
        print(f"Projeto copiado com sucesso para: {dest}")
    except Exception as e:
        print(f"Erro ao copiar o projeto: {e}")

@cli.command()
@click.argument('output_path', required=False, default='.')
@click.option('-StateProject', is_flag=True, help="Copia o projeto de estado.")
@click.option('-CeleryProject', is_flag=True, help="Copia o projeto de celery.")
@click.option('-State', is_flag=True, help="Copia um novo estado.")
@click.option('-TestState', is_flag=True, help="Copia um novo teste de estado.")
@click.option('-Task', is_flag=True, help="Copia uma nova tarefa.")
@click.option('-TestTask', is_flag=True, help="Copia um novo teste de tarefa.")
def new(output_path, stateproject, celeryproject, state, teststate, task, testtask):
    """Cria um novo projeto ou componente PyTrobot no caminho especificado."""
    output_path = Path(output_path).resolve()  # Caminho onde os arquivos serão copiados

    # Gera timestamp único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if stateproject:
        src = Path(list(state_project_scaffold.__path__)[0]).resolve()
        # Cria um subdiretório com timestamp
        destination = output_path / f'project_state_{timestamp}'
        destination.mkdir(parents=True, exist_ok=True)
        copy_project(src, destination)
    elif celeryproject:
        src = Path(list(celery_project_scaffold.__path__)[0]).resolve()
        # Cria um subdiretório com timestamp
        destination = output_path / f'project_celery_{timestamp}'
        destination.mkdir(parents=True, exist_ok=True)
        copy_project(src, destination)
    elif state:
        src = Path(new_state_file.__file__).resolve()
        destination = output_path / f"{src.stem}_{timestamp}"
        copy_project(src, destination)
    elif teststate:
        src = Path(test_state_file.__file__).resolve()
        destination = output_path / f"{src.stem}_{timestamp}"
        copy_project(src, destination)
    elif task:
        src = Path(new_task_file.__file__).resolve()
        destination = output_path / f"{src.stem}_{timestamp}"
        copy_project(src, destination)
    elif testtask:
        src = Path(test_task_file.__file__).resolve()
        destination = output_path / f"{src.stem}_{timestamp}"
        copy_project(src, destination)
    else:
        print("Nenhuma opção foi selecionada. Use --help para ver as opções disponíveis.")


if __name__ == "__main__":

    import os
    import sys

    # Mude o diretório de execução para 'E:\Projetos'
    os.chdir(r'E:\Projetos')

    # Adicione os argumentos como se fossem passados pelo terminal
    sys.argv.extend(['new', '-CeleryProject'])  # Exemplo de como adicionar opções e argumentos
    
    cli()  # Executa o CLI
