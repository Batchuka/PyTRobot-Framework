from time import sleep

from pytrobot.core.decortador.state import State, First
from pytrobot.core.decortador.multithread import Thread
from pytrobot.core.strategy.state.base_state import BaseState

@First
@State('OrderState', 'DeadState')
class HungryState(BaseState):
    """Estado inicial: o robô está com fome e quer pizza."""
    def on_entry(self):
        self.logger.info("I am hungry!")
    
    def execute(self):
        self.logger.info("If I don't eat anything soon, I'm going to die")
        self.time_to_die
        pass

    def on_exit(self):
        self.logger.info("I'm going to order pizza")
    
    def on_error(self, e):
        self.logger.error("I don't know how to order a pizza... it seems like it's the end of me.")

    @Thread
    def time_to_die(self):
        """
        Monitor the time until the robot dies of hunger.
        """
        time_limit = 30  # Time in seconds until the robot dies of hunger
        elapsed_time = 0
        
        while elapsed_time < time_limit:
            sleep(1)
            elapsed_time += 1
            self.logger.warning(f"Time remaining: {time_limit - elapsed_time} seconds")
        
        # Se o tempo limite for atingido, transição para o estado "Dead"
        self.logger.warning("Too much time without pizza. I'm going die.")
        self.transition('DeadState')
