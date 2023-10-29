import json
from importlib import resources

def cfg_item(*items):
    data = Config.instance().data
    for key in items:
        data = data[key]
    return data

class Config:
    __instance = None
    __json_path, __json_file = "falling_letters.assets.config", "config.json"

    @staticmethod
    def instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is None:
            Config.__instance = self

            with resources.path(Config.__json_path, Config.__json_file) as json_file:
                with open(json_file) as file:
                    self.data = json.load(file)

            self.__debug = False
        else:
            raise Exception("Config is a Singleton, Only One Instance Allowed")

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value