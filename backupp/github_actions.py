"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from pathlib import Path


# from .menu import yedekle_this, yedekle_this_onayisteme
from datetime import datetime
from dataclasses import dataclass
import sys
import os


# @dataclass
class GithubActions:
    def is_testing(self):
        return "hostedtoolcache" in sys.argv[0]


class PytestTesting:
    def is_testing(self):
        return "bin/pytest" in sys.argv[0]


def get_input(msg, default=None):
    if GithubActions().is_testing() or PytestTesting().is_testing():
        if not default:
            print("currently testing with no default ")
            return False
        return default
    ans = input(msg)
    return ans
