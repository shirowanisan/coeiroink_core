from setuptools import setup, find_packages

setup(
    name='coeirocore',
    version='1.0.3',
    url="https://github.com/shirowanisan/coeiroink_core",
    author="shirowanisan",
    license="LGPL license",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
