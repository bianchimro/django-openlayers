from setuptools import setup, find_packages
import os


setup(
    name='django-openlayers',
    version='0.1.0',
    description='Django Openlayers reusable app',
    long_description=open('README.rst').read(),
    author='Mauro Bianchi',
    author_email='bianchimro@gmail.com',
    license='BSD',
    url='https://github.com/bianchimro/django-openlayers',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)

