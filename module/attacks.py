"""
Enum for different attacks
"""

from enum import Enum


class Attacks(Enum):
    NOT_ATTACKED = -1
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
