# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


with open('README.rst') as readme:
    long_description = readme.read()


def recursive_requirements(requirement_file, libs, links, path=''):
    if not requirement_file.startswith(path):
        requirement_file = os.path.join(path, requirement_file)
    with open(requirement_file) as requirements:
        for requirement in requirements.readlines():
            if requirement.startswith('-r'):
                requirement_file = requirement.split()[1]
                if not path:
                    path = requirement_file.rsplit('/', 1)[0]
                recursive_requirements(requirement_file, libs, links,
                                       path=path)
            elif requirement.startswith('-f'):
                links.append(requirement.split()[1])
            else:
                libs.append(requirement)

libraries, dependency_links = [], []
recursive_requirements('requirements.txt', libraries, dependency_links)

setup(
    name='django-sympa',
    version='0.1.1',
    packages=find_packages(),
    install_requires=libraries,
    dependency_links=dependency_links,
    long_description=long_description,
    description='Add a view to interact with sympa',
    author='v-eye',
    author_email='arnaud.grausem@gmail.com',
    maintainer='di-dip-unistra',
    maintainer_email='di-dip@unistra.fr',
    url='https://github.com/unistra/django-sympa/',
    download_url='',
    license='PSF',
    keywords=['django', 'Université de Strasbourg', 'sympa', 'mail', 'users'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email :: Mailing List Servers'
    ]
)
