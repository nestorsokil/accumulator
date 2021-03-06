import setuptools

with open("README.md", "r") as rmd:
    long_description = rmd.read()

setuptools.setup(
    name="accumulator-aio",
    version="0.1.0",
    author="Nestor Sokil",
    author_email="nestor0603@gmail.com",
    description="Async Python3 client for Apache Accumulo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nestorsokil/accumulator-aio",
    packages=[
        "accumulator-aio"
    ],
    install_requires=[
        'thriftpy2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
)
