import shutil
import sys
import subprocess
from pathlib import Path

def install():
    """Install OU branding."""
    #print("Installing OU branding to Jupyter environment.")
    pkgdir = sys.modules['classic_nb_ou_branding'].__path__[0]
    fullpath = Path(pkgdir) / "resources"
    dest = subprocess.run(['jupyter', '--config-dir'], stdout=subprocess.PIPE)
    outpath = Path(dest.stdout.decode('utf-8').strip()) / "custom"
    outpath.mkdir(parents=True, exist_ok=True)
    for f in fullpath.rglob("*"):
        #print(f"copy {f} to {outpath}")
        rf = shutil.copy(f, outpath)
        #print(f"returned {rf}")
    