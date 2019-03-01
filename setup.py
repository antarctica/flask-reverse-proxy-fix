import os  # noqa: F401

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flask-reverse-proxy-fix",
    version=f"0.1.1",
    author="British Antarctic Survey",
    author_email="webapps@bas.ac.uk",
    description="Python Flask middleware for applications running under a reverse proxy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antarctica/flask-reverse-proxy-fix",
    license='Open Government Licence v3.0',
    install_requires=['flask'],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Development Status :: 5 - Production/Stable",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
)
