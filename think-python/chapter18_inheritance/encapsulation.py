"""
Start by writing functions that read and write global variables (when necessary).
Once you get the program working, look for associations between global variables and the functions that use them.
Encapsulate related variables as attributes of an object.
Transform the associated functions into methods of the new class.
"""


class Markov:
    """so that each variable can be used in more than one executions"""
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()


