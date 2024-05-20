from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(filename: str)->List[str]:
    '''
    Read requirements file and return list of requirements
    '''
    requirements=[]
    with open(filename, 'r') as file:
        requirements=file.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Zeel',
    author_email='zeelbhatt0425@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)