import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from TL.ex3 import word_count, file_path

result = word_count(file_path)

print(result["man"])
