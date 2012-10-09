from setuptools import setup, find_packages

version = '0.4'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='plonesocial.activitystream',
    version=version,
    description="This package provides views for plonesocial.microblog status updates and other user activities in Plone",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='plone socbiz social microblog activity stream',
    author='Guido Stevens',
    author_email='guido.stevens@cosent.net',
    url='http://github.com/cosent/plonesocial.activitystream',
    license='gpl',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonesocial'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        # -*- Extra requirements: -*-
        ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
    )
