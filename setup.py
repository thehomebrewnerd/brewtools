import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brewtools",
    version="0.0.1",
    author="Nate Parsons",
    author_email="brewtools@hopsandcode.com",
    description="A package of brewing tools and calculators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thehomebrewnerd/brewtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)