
from setuptools import setup, find_namespace_packages


setup(
    name='qtoggleserver-raspigpio',
    version='unknown-version',
    description='qToggleServer driver for Raspberry Pi GPIOs based on raspi-gpio',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),
)
