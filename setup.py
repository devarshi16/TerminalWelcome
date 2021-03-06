import setuptools
from setuptools import find_packages
import os

def find_data(relpath, folder):
    dir_content = []
    path = os.path.join(relpath, folder)
    tree = [(dirname, filenames) for dirname, _, filenames in os.walk(path)
            if filenames]

    for root, files in tree:
        path = os.path.relpath(root, relpath)
        dir_content.extend(map(lambda x: os.path.join(path, x), files))

    return dir_content


def package_data(relpath, folders):
    all_files = []
    for folder in folders:
        all_files.extend(find_data(relpath, folder))

    return all_files


long_description = """
Put a custom message and/or 
a pokemon ASCII art and/or 
a random oneliner when you start your terminal
NOTE: do $ sudo pip install poketerm
You need sudo permissions for this to work
"""
setuptools.setup(
     name='poketerm',  
     version='0.9.2',
     author="devarshi16",
     author_email="devershigpt6@gmail.com",
     description="Custom terminal welcome messages, pokemon ASCII art, and random one-liner!($sudo pip install poketerm)",
     long_description=long_description,
     url="https://github.com/devarshi16/TerminalWelcome",
     packages=find_packages(),
     keywords="terminal ascii-art shell-script welcomemessage bash pikachu bulbasaur pokemon-terminal pokemon linux linux-shell meowth",
     package_data={
         "src":["*.ini","*.default","*.py"]
     },
     include_package_data=True,
     classifiers=[
         "Development Status :: 4 - Beta",
         "Programming Language :: Python",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX :: Linux",
     ],
     entry_points = {
         "console_scripts": ['poketerm = src.main:main']
     },
     python_requires=">=2.7",
     install_requires=[
        'readchar>=2.0.1',
        'termcolor>=1.1.0'
     ],
 )
