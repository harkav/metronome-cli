import sys
import os

# Add the root directory (parent directory of 'tests') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now try importing from metronome.project
from metronome.project import *  # or 'from metronome.project import your_module'

from metronome.metronome import Metronome
import pytest


def test_validate_input():
    with pytest.raises(ValueError):
        validate_input("kvakk", "kvekk") 
    with pytest.raises(ValueError): 
        validate_input("3", "kvakk")
    with pytest.raises(ValueError): 
        validate_input("Kvakk", "120")
    with pytest.raises(ValueError): 
        validate_input("3", "400")
    with pytest.raises(ValueError): 
        validate_input("4", "15")


def test_increment(): 
    metronome = Metronome(3, 300)
    increment(metronome, 10)
    assert metronome.get_bpm() == 310 
    increment(metronome, 10)
    assert metronome.get_bpm() == 320 # should not go higher than 320
    increment(metronome, 10) 
    assert metronome.get_bpm() == 320 


def test_decrement(): 
    metronome = Metronome(4, 40)
    decrement(metronome, -20)
    assert metronome.get_bpm() == 20
    decrement(metronome, -20)
    assert metronome.get_bpm() == 20
    increment(metronome, 100)
    decrement(metronome, -20)
    assert metronome.get_bpm() == 100