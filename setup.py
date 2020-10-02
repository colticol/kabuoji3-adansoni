"""Learn more: https://github.com/kennethreitz/setup.py."""
import os
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kabuoji3-adansoni',
    version='0.0.1',
    description='get stock data from https://kabuoji3.com/',
    long_description=readme,
    author='colticol',
    author_email='colticol@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/colticol/kabuoji3-adansoni',
    license=license,
)
