from setuptools import find_packages, setup

setup(
    name='qulib',
    packages=find_packages(include=['qulib']),
    version='0.1.0',
    description='quantum library for operators, protocols, algorithms, and applications',
    author='Anurag K S V',
    license='MIT',
    install_requires=['qiskit','matplotlib'],
)