from setuptools import setup, find_packages
import io
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
def find_version(*file_paths):
    pathname = os.path.join(here, *file_paths)
    with io.open(pathname, mode='r', encoding='latin1') as verf:
        version_file = verf.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.MULTILINE)
    print version_file
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
description = "Python Microframework for REST endpoints"
long_description = description
with io.open('DESCRIPTION.rst', encoding='utf-8') as descf:
    long_description = descf.read()

setup(
    name="resto",
    version=find_version('resto', '__init__.py'),
    description=description,
    long_description=long_description,
    url='http://github.com/rafaelpivato/resto',
    author='Rafael Pivato',
    author_email='rafael@pivato.info',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='rest framework micro microframework wsgi',
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
)
