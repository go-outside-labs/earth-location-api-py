from setuptools import setup, find_packages

setup(
    name="loc",
    version='0.1',
    packages=find_packages(include=['api']),
    author="Mia Stein",
    install_requires=['python-dotenv'],
    entry_points={
        'console_scripts': ['loc=api.main:run']
    },
)