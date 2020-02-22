from distutils.core import setup
import os

DIRECTORY = os.path.dirname(__file__)
READ_ME = open(os.path.join(DIRECTORY, "README.md")).read()
VERSION = open(os.path.join(DIRECTORY, "fscleaner", "VERSION.txt")).read()

setup(
  name = 'fscleaner',
  packages = ['fscleaner'],
  version = VERSION,
  license='MIT',
  description = 'file system folder cleaner and file remover',
  long_description=READ_ME,
  long_description_content_type="text/markdown",
  author = 'Subham Kumar',
  author_email = 'subhamkumarchandrawansi@gmail.com',
  url = 'https://github.com/isubham/fscleaner.git',
  download_url = 'https://github.com/isubham/fscleaner/archive/v0.1.tar.gz',
  keywords = ['file rename', 'folder rename', 'delte file with types'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Desktop Environment :: File Managers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ]
)