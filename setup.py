import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyledjr",
    version="0.0.1",
    author="Eric Parkin",
    author_email="eparkin985@gmail.com",
    description=(
        "A simple, open-source, python-based personal finace tool."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kw0nta/pyledjr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
