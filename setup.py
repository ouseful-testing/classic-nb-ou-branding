from setuptools import setup

setup(
    name="classic_nb_ou_branding",
    packages=["classic_nb_ou_branding"],
    version='0.0.4',
    author="Tony Hirst",
    author_email="tony.hirst@gmail.com",
    description="Install OU custom brnading for classic Jupyter notebook.",
    long_description='''
    A simple "dummy" package that installs custom branding elements for classic Jupyter notebook.
    ''',
    long_description_content_type="text/markdown",
    install_requires=["click"],
    include_package_data=True,
    package_data={'': ['resources/*']},
    entry_points='''
        [console_scripts]
        ou_nb_branding=classic_nb_ou_branding.cli:cli
    '''
)


