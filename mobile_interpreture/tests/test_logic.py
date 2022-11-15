import os
import sys


# Add path for logic
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile.logic import Interpreture


i = Interpreture()
name = "line"
txt = "print('hello world')"

def test_create_folder():
    assert "files" in os.listdir()

def test_create_file():
    i.create_file(name)
    assert "%s.py" % name in os.listdir(path="files")

def test_edit_file():
    i.edit_file(txt, name)
    with open('files/%s.py' % name, "r") as file:
        assert txt == file.read()

def test_read_file():
    with open('files/%s.py' % name, "r") as file:
        assert i.read_file(name) == file.read()

def test_run_file():
    i.run_file(name)
    assert i.run_file(name) == "hello world"

def test_del_file():
    i.del_file(name)
    assert "%s.py" % name not in os.listdir(path="files")

