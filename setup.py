from setuptools import setup, find_packages

setup(
    name='accmodels',
    version='0.0.0',
    url='https://github.com/rdemaria/accmodels.git',
    author='Riccardo De Maria',
    author_email='riccardo.de.maria@cern.ch',
    description='Package for accmodels',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
