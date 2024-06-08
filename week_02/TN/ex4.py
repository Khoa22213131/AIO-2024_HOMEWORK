import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from TL.ex4 import levenshtein_distance

print(levenshtein_distance("hola", "hello"))
