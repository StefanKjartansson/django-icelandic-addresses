#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import codecs


try:
    from setuptools import setup, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, Command  # noqa
from distutils.command.install import INSTALL_SCHEMES


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')

    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


extra = {}

# -*- Python 3 -*-
is_py3k = sys.version_info[0] == 3
if is_py3k:
    extra.update(use_2to3=True)


NAME = 'django-icelandic-addresses'


class RunTests(Command):
    description = 'Run the django test suite from the tests dir.'
    user_options = []
    extra_env = {}
    extra_args = []

    def run(self):
        for env_name, env_value in self.extra_env.items():
            os.environ[env_name] = str(env_value)

        this_dir = os.getcwd()
        testproj_dir = os.path.join(this_dir, 'tests')
        os.chdir(testproj_dir)
        sys.path.append(testproj_dir)
        from django.core.management import execute_manager
        os.environ['DJANGO_SETTINGS_MODULE'] = os.environ.get(
                        'DJANGO_SETTINGS_MODULE', 'settings')
        settings_file = os.environ['DJANGO_SETTINGS_MODULE']
        settings_mod = __import__(settings_file, {}, {}, [''])
        prev_argv = list(sys.argv)
        try:
            sys.argv = [__file__, 'test', 'ice_addresses'] + self.extra_args
            execute_manager(settings_mod, argv=sys.argv)
        finally:
            sys.argv = prev_argv

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    long_description = 'See http://github.com/StefanKjartansson/django-icelandic-addresses'


setup(
    author='Stefán Kjartansson',
    author_email='esteban.supreme@gmail.com',
    description='Django app containing a list of Icelandic addresses',
    license='BSD',
    name=NAME,
    packages=['ice_addresses'],
    platforms=['any'],
    url='https://github.com/StefanKjartansson/django-icelandic-addresses',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    ],
    cmdclass={'test': RunTests},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    long_description=long_description,
    **extra
)
