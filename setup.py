from os.path import dirname, join
import sys
from setuptools import setup, find_packages


with open(join(dirname(__file__), 'scrapy_rss/VERSION'), 'rt') as f:
    version = f.read().strip()


install_requires=['python-dateutil',
                  'scrapy<1.5.0' if sys.version_info[:2] == (3, 3) else 'scrapy>=1.1' if sys.version_info < (3, 6) else 'scrapy>=1.3.1',
                  'six']
if sys.version_info[:2] == (3, 3):
    install_requires.extend(['cryptography<2.0', 'pyOpenSSL<17.3.0'])

with open('README.rst') as readme:
    setup(
        name='scrapy-rss',
        version=version,
        url='https://github.com/woxcab/scrapy_rss',
        description='RSS Tools for Scrapy Framework',
        long_description=readme.read(),
        license='BSD',
        packages=find_packages(exclude=('tests',)),
        include_package_data=True,
        zip_safe=False,
        python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
        classifiers=[
            'Framework :: Scrapy',
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        install_requires=install_requires,
    )
