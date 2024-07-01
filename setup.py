from setuptools import setup, find_packages

setup(
    name='analisis_enfermedades',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'experta',
        'python-dotenv',
        'pytest'
    ],
)
