from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from nirmaha import __version__ as version

setup(
    name="nirmaha",
    version=version,
    description="Equipment Rental Management System",
    author="Rajesh Medampudi",
    author_email="rajesh@simbotix.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
