import unittest
import os
import sys


# Add path for logic
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile.logic import Interpreture


class TestIntepreture(unittest.TestCase):
    """ Test class Interpreture """
    def __init__(self) -> None:
        super().__init__()
