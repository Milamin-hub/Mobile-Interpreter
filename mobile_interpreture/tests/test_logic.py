import unittest
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile.logic import Interpreture


class TestIntepreture(unittest.TestCase):
    def __init__(self):
        super().__init__()