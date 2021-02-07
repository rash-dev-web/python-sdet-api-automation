import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read("properties.ini")
    return config
