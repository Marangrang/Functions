from setuptools import setup, find_packages

setup(
    name='Rangz',
    version='0.1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Marangrang/Rangz',
    author='marangrang Tsepetsi',
    author_email='mtsepetsi2@gmail.com'
)
