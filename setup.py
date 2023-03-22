from setuptools import setup, find_packages

setup(
    name='coeirocore',
    version='1.1.0',
    url="https://github.com/shirowanisan/coeiroink_core",
    author="shirowanisan",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
