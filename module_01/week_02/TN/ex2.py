import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from TL.ex2 import count_chars

print(count_chars("smiles"))
