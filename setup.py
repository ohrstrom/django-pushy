from distutils.core import setup

setup(
    name='pushy',
    version='0.0.1',
    author='Jonas Ohrstrom',
    author_email='ohrstrom@hazelfire.com',
    packages=['pushy',],
    #scripts=[],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Django push gateway.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.4.1",
        "redis >= 2.7.2",
    ],
)