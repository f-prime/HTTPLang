from setuptools import setup
import sys

setup(name='HTTPLang',
      version='2.0.0',
      author='Frankie Primerano',
      author_email='max00355@gmail.com',
      packages=['httplang'],
      entry_points={
          'console_scripts': ['httplang=httplang:console_main'],
      },
      url='https://github.com/Max00355/HTTPLang',
      description='A scripting language to do HTTP routines.',
      classifiers=[
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'License :: OSI Approved :: MIT License',
          'Topic :: Utilities'
      ],
      )
