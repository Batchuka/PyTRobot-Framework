# pytrobot/cli/main.py

from invoke import tasks
from invoke.collection import Collection
from invoke.program import Program

# Importe suas tarefas aqui
from pytrobot.tasks import build, new

namespace = Collection()
namespace.add_task(build, name="build") #type:ignore
namespace.add_task(new, name="new") #type:ignore

# Adicione mais tarefas conforme necessário

class PyTRobotCLI(Program):
    def __init__(self):
        super().__init__(namespace=namespace, name='PyTRobot', version='3.0.0')

    # Você pode adicionar aqui lógicas adicionais para sua CLI

program = PyTRobotCLI()

if __name__ == "__main__":
    program.run()