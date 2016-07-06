# -*- coding: utf-8 -*-
import time
import sys
import math

import pingo

try:
    print("Loading board...")
    board = pingo.detect.get_board()
    print("Its ok...")
except Exception as e:
    print("Error on get_board: {}".format(e))
    sys.exit(1)

