from setuptools import setup, find_packages
import os

version = '1.3'

setup(name='upc.genweb.serveis',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Team @ UPCnet',
      author_email='plone.team@upcnet.es',
      url='https://github.com/upcnet/upc.genweb.serveis/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upc', 'upc.genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
