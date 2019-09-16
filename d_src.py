"""@package DiscreteSource

Модуль с описанием класса дискретного источника
"""

import json
import random
from fractions import Fraction
import keyboard
import time


def check_correctness(src_desc):
    models = [_ for _ in src_desc["models"].keys()]
    switches = [_ for _ in src_desc["switches"].keys()]
    for switch in src_desc["source"]:
        if switch not in switches:
            return True
    for switch in src_desc["switches"].values():
        for model in switch:
            if model not in models:
                return True
    return False


def check_model(what, where):
    keys = where.keys()
    for model in what:
        if model in keys:
            return False
    return True


def check_switch(what, where):
    keys = where.keys()
    for switch in what:
        if switch in keys:
            return False
    return True


class DiscreteSource:
    src = dict()

    def __init__(self, desc_file):
        try:
            self.src = json.load(desc_file)
            if check_correctness(self.src):
                raise KeyError
            self.current_switch = 0
            self.current_model = ""
        except KeyError:
            print("KeyError caught. Check file for keys.")
            raise KeyError
        except json.JSONDecodeError:
            print("JSONDecodeError: Invalid file.")
            raise Exception

    def choose_model(self):
        models = [_ for _ in self.src["switches"][self.src["source"][self.current_switch]].keys()]
        weights = [_ for _ in self.src["switches"][self.src["source"][self.current_switch]].values()]
        self.current_switch = (self.current_switch + 1) % len(self.src["source"])
        self.current_model = random.choices(models, weights=[float(Fraction(i)) for i in weights])[0]

    '''
        @brief Random sequence generating
        @param amount size of sequence
    '''
    # def generate(self, amount, out_file):
    def generate(self, amount):
        size = amount if amount > 0 else 1
        seq = []
        while size:
            self.choose_model()
            symbols = [_ for _ in self.src["models"][self.current_model].keys()]
            weights = [_ for _ in self.src["models"][self.current_model].values()]
            out_symbol = random.choices(symbols, weights=[float(Fraction(i)) for i in weights])[0]
            self.current_switch = (self.current_switch + 1) % len(self.src["source"])
            # out_file.write(out_symbol)
            # print(out_symbol, end='')
            if amount > 0:
                seq.append(out_symbol)
                size -= 1
            else:
                print(out_symbol, end='')
                time.sleep(0.1)
                if keyboard.is_pressed('q'):
                    size -= 1
        return seq

    '''
        Auxiliary functions
    '''
    def print_to_file(self, out_file):
        with open(out_file, "w") as out:
            json.dump(self.src, out, indent=4)

    def add_model(self, model_desc):
        if check_model(model_desc, self.src["models"]):
            self.src["models"].update(model_desc)

    def add_switch(self, switch_desc):
        if check_switch(switch_desc, self.src["switches"]):
            self.src["switches"].update(switch_desc)

    def add_switch_to_sequence(self, position, switch_name):
        self.src["source"].insert(position, switch_name)

    def del_model(self, key):
        self.src["models"].pop(key, None)

    def del_switch(self, key):
        print("NOTE: deleting switch affects \"source\", thus deleted switch is deleted there too")
        self.src["switches"].pop(key)
        self.src["source"].remove(key)
