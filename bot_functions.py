# handler_funcs
"""Functions needed for the bot."""

import yaml
from os import path as ospath
from sys import path as syspath


def getconfig(config_file):
    """Get config from file and return object."""
    # Open file and read config
    with open(ospath.join(syspath[0], config_file), 'r') as stream:
        try:
            config = yaml.load(stream, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            print(exc)
    return config
