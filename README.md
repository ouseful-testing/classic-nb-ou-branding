# classic-nb-ou-branding
Simple script to install OU branding to Jupyter `nbclassic` notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ouseful-testing/classic-nb-ou-branding/HEAD?urlpath=tree)

<img width="536" alt="image" src="https://user-images.githubusercontent.com/82988/220650261-d03ea376-9c0d-4412-8381-5d6893937bd2.png">



```
pip install --upgrade  git+https://github.com/ouseful-testing/classic-nb-ou-branding.git
```

To install the custom branding pack into the `nbclassic` customisation path:

```
ou_nb_branding install
```

In a conda env, run:

```
ou_nb_branding install --conda ENVIRONMENT_NAME
```

The `ENVIRONMENT_NAME` is the name of the conda envt you want to install into if you installed and are running the jupyter server in the env; In M348 defaults , this means running:
 
`ou_nb_branding install --conda r_env`
 
Getting the path to install into is a hack, so it may break (I only tested on Mac; repo is at: https://github.com/ouseful-testing/classic-nb-ou-branding )...
 
Without the `--conda` switch, the installation defaults to whatever home Jupyter environment path is found. So in a simple envt, eg the TM358 (not tested) environment, just run:
 
`ou_nb_branding install`
 
For JupyterLab (not tested in the new notebook UI ), here’s another branding hack: https://github.com/innovationOUtside/jupyterlab_ou_brand_extension
