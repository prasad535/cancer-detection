from setuptools import setup, find_packages

setup(
    name = 'cancer',
    version= '0.0.0',
    author='Prasad Nagineni',
    author_email='prasad.nagineni12345@gmail.com',
    package_dir={"":"src"},
    packages = find_packages(where="src")
)