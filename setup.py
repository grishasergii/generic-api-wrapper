#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "requests",
    "urllib3",
    "boto3",
    "aws-requests-auth",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sergii Gryshkevych",
    author_email="",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Generic API wrapper",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["api", "wrapper", "generic", "rest api"],
    name="generic-api-wrapper",
    packages=find_packages(include=["generic_api_wrapper", "generic_api_wrapper.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/grishasergii/generic-api-wrapper",
    version="0.2.0",
    zip_safe=False,
)
