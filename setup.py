# encoding: utf-8
# Copyright 2008-2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from setuptools import setup, find_packages
import os.path

# Package data
# ------------

_name            = 'edrndmcc.appserver'
_version         = '1.2.0'
_description     = 'EDRN DMCC Application Server policy'
_url             = 'http://cancer.jpl.nasa.gov/'
_downloadURL     = 'http://oodt.jpl.nasa.gov/dist/edrndmcc-appserver'
_author          = 'Sean Kelly'
_authorEmail     = 'sean.kelly@jpl.nasa.gov'
_maintainer      = 'Sean Kelly'
_maintainerEmail = 'sean.kelly@jpl.nasa.gov'
_license         = 'Proprietary'
_namespaces      = ['edrndmcc']
_zipSafe         = False
_keywords        = 'web policy zope plone jpl nasa caltech edrn cancer detection appserver application server'
_testSuite       = 'edrn.rdf.tests.test_suite'
_entryPoints     = {
    'z3c.autoinclude.plugin': ['target=plone'],
}
_requirements = [
    'edrn.rdf',
    'edrn.theme',
    'Plone',
    'plone.app.ldap',
    'setuptools',
]
_extras = {
    'test': ['plone.app.testing'],
}
_classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Plone',
    'Intended Audience :: Healthcare Industry',
    'Intended Audience :: Science/Research',
    'License :: Other/Proprietary License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

# Setup Metadata
# --------------

def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDescription = _header + '\n\n' + _read('README.txt') + '\n\n' + _read('docs', 'INSTALL.txt') + '\n\n' \
    + _read('docs', 'HISTORY.txt') + '\n\n' + _read('docs', 'LICENSE.txt')
open('doc.txt', 'w').write(_longDescription)

setup(
    author=_author,
    author_email=_authorEmail,
    classifiers=_classifiers,
    description=_description,
    download_url=_downloadURL,
    entry_points=_entryPoints,
    extras_require=_extras,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_longDescription,
    maintainer=_maintainer,
    maintainer_email=_maintainerEmail,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages(exclude=['ez_setup', 'distribute_setup', 'bootstrap']),
    url=_url,
    version=_version,
    zip_safe=_zipSafe,
)
