import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-basic-site-components',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "django",
        "wagtail",
    ],
    include_package_data=True,
    license='MIT License',
    description='Django App that provides basic wagtail related models.',
    long_description=README,
    url='https://github.com/CIGIHub/wagtail-basic-site-components',
    author='Natasha Scott',
    author_email='nscott@cigionline.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='basic_site.runtests.runtests',
)
