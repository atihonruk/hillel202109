from setuptools import setup

setup(
    name='yourscript',
    version='0.1',
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        yourscript=main:cli
    ''',
)
