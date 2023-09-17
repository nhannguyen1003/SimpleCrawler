from pathlib import Path
import os
url = "aaa"

with open(os.path.join(Path.cwd(),f"{url}.text"), "w") as f:
    f.write("Hihi")