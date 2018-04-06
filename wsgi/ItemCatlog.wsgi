import os
import sys

activatethis = "/usr/share/ProjectItemCatlog/venv/bin/activate_this.py"

with open(activatethis) as f:
    exec(f.read(), dict(__file__=activatethis))

sys.stdout = sys.stderr

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '../..'))

sys.path.append('/usr/share/ProjectItemCatlog/')
print(sys.path)

from ProjectItemCatlog.ItemCatlog import app as application
