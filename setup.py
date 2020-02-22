from distutils.core import setup

setup(
  name = 'fscleaner',
  packages = ['fscleaner'],
  version = "0.2",
  license='MIT',
  description = 'file system folder cleaner and file remover',
  author = 'Subham Kumar',
  author_email = 'subhamkumarchandrawansi@gmail.com',
  url = 'https://github.com/isubham/fscleaner.git',
  download_url = 'https://github.com/isubham/fscleaner/archive/v0.1.1.tar.gz',
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