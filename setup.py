import re

from setuptools import find_packages
from setuptools import setup


with open('hrtool_api/__init__.py', 'r') as fd:
    version_re = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(version_re, fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='polls',
    version=version,
    description='bla',
    author='user',
    author_email='office@google.com',
    install_requires=[
        'Django==1.9.0',
        'django-phrase'
    ],
    url='http://www.google.com/',
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests"
        ]
    )
)
