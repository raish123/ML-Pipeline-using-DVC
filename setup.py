from setuptools import setup,find_packages

#creating an object of setup class
setup(
    name="twitter emotion detection",
    version="0.0.1",
    author="raees",
    author_email="raees@gmail.com",
    long_description=open("readme.md").read(),
    packages=find_packages(),
    install_requires= []
    
)