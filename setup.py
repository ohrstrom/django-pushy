from distutils.core import setup

setup(
    name='pushy',
    version='0.0.1',
    author='Jonas Ohrstrom',
    author_email='ohrstrom@hazelfire.com',
    packages=['pushy',],
    #scripts=[],
    url='https://github.com/ohrstrom/django-pushy/',
    license='LICENSE.txt',
    description='Django push gateway.',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.4.1",
        "redis >= 2.7.2",
    ],
)