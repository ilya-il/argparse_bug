__author__ = 'ilya_il'

import argparse

parser = argparse.ArgumentParser(description='Check required mutually exclusive group')

g = parser.add_mutually_exclusive_group(required=True)
g.add_argument('-F', help="F argument")
g.add_argument('-D', help="D argument")

args = parser.parse_args()
