import sys
from os import path, getcwd
root_path = path.abspath(getcwd())
sys.path += [root_path + "/src"]

from fct_sum import *

def test_sum():
    assert my_sum(1,2) == 3
    
    