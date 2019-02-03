
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pylinenotify',
    version='1.1.3',
    description='using LineNotify more easily',
    url='https://github.com/reud/PyLineNotify',
    author='reud',
    author_email='mail@reud.net',
    license='MIT',
    install_requires=['requests'],
    keywords='LineNotify',
    classifiers=[
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/reud/PyLineNotify/issues',
        'Source': 'https://github.com/reud/PyLineNotify',
    },
    packages=find_packages(),
)