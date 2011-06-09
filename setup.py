from setuptools import setup, find_packages
import os

version = '0.1a4'

setup(
    name='django-ordering',
    version=version,
    description='Simple order tracking app',
    long_description=open('README.txt').read() + '\n' +
                     open(os.path.join('docs', 'HISTORY.txt')).read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='',
    author='Walter Scheper',
    author_email='scheper@unc.edu',
    url='https://github.com/wfscheper/django-ordering',
    license='',
    packages=find_packages('src', exclude=['ez_setup', 'ordering.tests']),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'django>=1.3,<1.4',
        'south>=0.7,<0.8',
    ],
)
