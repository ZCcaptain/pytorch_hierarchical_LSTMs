import json

from dataclasses import dataclass

@dataclass
class Hyper(object):
    def __init__(self, path:str):
        self.__dict__ = json.load(open(path, 'r'))

