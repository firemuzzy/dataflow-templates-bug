from __future__ import absolute_import
from __future__ import print_function

import setuptools

REQUIRED_PACKAGES = []

setuptools.setup(
    name='tfidf-review-noun-chunks',
    version='0.0.1',
    author='mcharkin',
    author_email='michael@lablablab.com',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages()
)