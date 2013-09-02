#!/usr/bin/env python

import os
import sys

import django-icelandic-addresses

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django-icelandic-addresses.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-icelandic-addresses',
    version=version,
    description='Django app containing a list of Icelandic addresses',
    long_description=readme + '\n\n' + history,
    author='Stefán Kjartansson',
    author_email='esteban.supreme@gmail.com',
    url='https://github.com/StefanKjartansson/django-icelandic-addresses',
    packages=[
        'django-icelandic-addresses',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-icelandic-addresses',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)