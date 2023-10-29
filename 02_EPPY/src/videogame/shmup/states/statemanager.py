from shmup.states.intro import Intro
from shmup.states.gameplay import GamePlay

class StateManager:

    def __init__(self):
        self.__states = {
            "Intro" : Intro(),
            "GamePlay" : GamePlay()
        }

        self.__current_state_name = "Intro"
        self.__current_state = self.__states[self.__current_state_name]
        self.__current_state.enter()

    def handle_input(self, event):
        self.__current_state.handle_input(event)

    def update(self, delta_time):
        if self.__current_state.done:
            self.__change_state()
        self.__current_state.update(delta_time)

    def render(self, surface_dst):
        self.__current_state.render(surface_dst)

    def release(self):
        self.__current_state.release()

    def __change_state(self):
        self.__current_state.exit()

        previous_state = self.__current_state_name
        self.__current_state_name = self.__current_state.next_state
        self.__current_state = self.__states[self.__current_state_name]
        self.__current_state.previous_state = previous_state

        self.__current_state.enter()