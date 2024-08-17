import subprocess
from pathlib import Path

for i in range(5):
    subprocess.check_call(["py", "write_files_starter_code.py"])
    
print(Path("read_files.py").suffix)