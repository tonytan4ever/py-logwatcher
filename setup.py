'''
Python Logfile Watcher
================
A Python impelmentation of tail, with additional feature of callback of
incoming lines, file rotation handling and many more.
'''

import os
import sys

import pip
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


pip_session = pip.download.PipSession(retries=3)


def get_requirements():
    pip_session = pip.download.PipSession(retries=3)
    requirements = pip.req.parse_requirements(
                    "requirements.txt",
                    session=pip_session)
    install_requires = []
    dependency_links = []
    for req in requirements:
        if req.link is not None:
            dependency_links.append(req.link.url)
        install_requires.append(str(req.req))

    return install_requires, dependency_links


def get_long_description():
    with open('README.md') as f:
        rv = f.read()
    return rv


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '-xrs',
            '--cov', 'flask_saml',
            '--cov-report', 'term-missing',
            '--pep8',
            '--flakes',
            '--cache-clear'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


if os.path.exists("requirements.txt"):
    install_requires, dependency_links = get_requirements()
else:
    install_requires, dependency_links = (None, None)

setup(
    name='py-logwatcher',
    version='0.0.0',
    url='https://github.com/tonytan4ever/py-logwatcher',
    license='MIT',
    author='Tony Tan',
    author_email='tonytan198211@gmail.com',
    description=('Python implementation of tail -- A log file watcher'),
    long_description=get_long_description(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    dependency_links=dependency_links,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Cross-platform',
        'Intended Audience :: Developers/Sys Admins',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: DevOps :: System',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
