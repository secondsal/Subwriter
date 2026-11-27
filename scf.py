
CONFIG_PATH = ""
CONFIGS_RAW = []
CONFIGS = {}

class LangString:
    def __init__(self, x = str):
        self.lang: str = x
        self.var_string = "~" # customize if you want

        
    def export(self, vars: list):
        full = self.lang
        for i, var in enumerate(vars):
            full = full.replace("~", str(vars[i]), 1)
        return full

def set_right_type(x):
    try:
        return int(x)
    except ValueError:
        pass
    try:
        return float(x)
    except ValueError:
        pass
    try:
        return bool(x)
    except ValueError:
        pass
    return x

def conf_make(configs: list[str]):
    global CONFIGS
    for conf in CONFIGS_RAW:
        l, r = conf.split("=")
        CONFIGS[l] = set_right_type(r)

def load_config(path):
    global CONFIGS_RAW
    try:
        with open(path, "r") as file:
            CONFIGS_RAW = file.read().split(",")
            conf_make(CONFIGS_RAW)
    except FileNotFoundError:
        print("ERROR: File not found")

def get_config(key):
    try:
        return CONFIGS[key]
    except KeyError:
        return None 

def simple_conf_key_get(confKey, innerKey, dataDict: dict):
    return dataDict[str(get_config(confKey))][innerKey]