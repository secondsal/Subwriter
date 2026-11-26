
CONFIG_PATH = ""
CONFIGS_RAW = []
CONFIGS = {}

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