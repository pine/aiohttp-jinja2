import codecs
import os
import re

from setuptools import setup

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'aiohttp_jinja2', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

install_requires = ['aiohttp>=3.0.0', 'jinja2>=2.7']


setup(name='aiohttp-jinja2',
      version=version,
      description=("jinja2 template renderer for aiohttp.web "
                   "(http server for asyncio)"),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: AsyncIO',
      ],
      author='Andrew Svetlov',
      author_email='andrew.svetlov@gmail.com',
      url='https://github.com/aio-libs/aiohttp_jinja2/',
      license='Apache 2',
      packages=['aiohttp_jinja2'],
      python_requires='>=3.5.3',
      install_requires=install_requires,
      include_package_data=True)
