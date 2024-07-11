
from setuptools import setup, find_packages

setup(
        name='ApiTest',
        version='1.0.0',
        author='3cloud',
        package_dir={'': 'src'},
        packages=find_packages('src'),
        zip_safe=False,
        install_requires=[
            'requests==2.31.0'
            ]
        )

