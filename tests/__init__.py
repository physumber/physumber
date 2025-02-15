"""
Test suite for physumber
"""


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
import pytest  # Now should work
import physumber.sumbermath  # Now should work
import physumber.sumberphysics  # Now should work
