import click

import shutil
import sys
import subprocess
from pathlib import Path
#import jupyter_core
import json

@click.group()
def cli():
	pass

@cli.command()
@click.option('--conda', '-c',  help='Name of conda environment')
def install(conda):
    """Install OU branding."""
    #print("Installing OU branding to Jupyter environment.")
    pkgdir = sys.modules['classic_nb_ou_branding'].__path__[0]
    fullpath = Path(pkgdir) / "resources"
    
    # TO DO - should we get the config via:
    # import jupyter_core
    # jupyter_core.paths.jupyter_config_dir()
    # Or maybe the following, which gives env paths:
    # jupyter_core.paths.jupyter_config_path()
    # Then have a cli arg that lets you install to an env?
    # eg list includes:
    # '/Users/tonyhirst/opt/miniconda3/envs/r_env/etc/jupyter',
    # jupyter-core.paths is a new thing
    # and we can't risk upgrading jupyter-core?
    if conda:
        #paths = jupyter_core.paths.jupyter_config_path()
        dest = subprocess.run(['jupyter', '--paths', '--json'], stdout=subprocess.PIPE)
        paths = json.loads(dest.stdout.decode('utf-8'))["config"]
        found = False
        for path in paths:
            if f"envs/{conda}" in path:
                found = True
                dest = Path(path)
                break
        if not found:
            # TO DO raise a proper warning
            print(f"No environment found called {conda}")
            exit(-1)
    else:
        dest = subprocess.run(['jupyter', '--config-dir'], stdout=subprocess.PIPE)
        dest = Path(dest.stdout.decode('utf-8').strip())
    outpath = dest / "custom"
    outpath.mkdir(parents=True, exist_ok=True)
    for f in fullpath.rglob("*"):
        #print(f"copy {f} to {outpath}")
        rf = shutil.copy(f, outpath)
        #print(f"returned {rf}")
