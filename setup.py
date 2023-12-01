from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'physim',
    version = '0.1.0',
    description = 'A bunch of classes that should help to make your own Physics Simulations with Python.',
    package_dir = {"": "app"},
    packages = find_packages(where = 'app'),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/JosePfs137/PhySim.git',
    author = 'JosePfs137',
    author_email = 'jose.floressald@alumno.buap.mx',
    classifiers = [
        'Programing Language :: Python :: 3.10'
    ] ,
    install_requires = [
        'numpy >= 1.26.2',
        'pygame >= 2.5.2'
    ],
    extras_require = {'dev': ['twine >= 4.0.2']},
    python_requires = '>= 3.10'

)