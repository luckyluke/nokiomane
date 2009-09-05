# TODO:da rifinire

from distutils.core import setup

import nokiomane

# Metadata
NAME = "nokiomane"
VERSION = nokiomane.__version__
DESCRIPTION = "Nokia PC-Suite clone based on Gammu"
AUTHOR = "Luca Dariz"
AUTHOR_EMAIL = "luca.dariz@gmail.com"
URL = nokiomane.__url__
LICENSE = nokiomane.__license__

# Setup
setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      platforms=["any"],
      packages=packages,
      cmdclass=doc_commands,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Communications :: Chat',
          'Topic :: Communications :: Telephony',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ])
