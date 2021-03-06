import os
import sys

import starfish


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(starfish.__file__)))
os.environ["TESTING"] = "1"
sys.path.append(os.path.join(ROOT_DIR, "docs", "source", "usage", "iss"))


def test_iss_pipeline_in_docs():
    # Just importing the file and verifying it runs for now
    __import__('iss_pipeline')
