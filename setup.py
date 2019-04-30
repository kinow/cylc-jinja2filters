from setuptools import setup

setup_requires = [
    'isodatetime==1!2.0.*',
    'jinja2>=2.10.1, <2.11.0',
]

setup(
    # cylc namespace package
    packages=['cylc.jinja2filters'],
    setup_requires=setup_requires
)
