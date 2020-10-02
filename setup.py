import setuptools

__version__ = '0.0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_name",
    version=__version__,
    author="katmai",
    author_email="katmai.mobil@gmail.com",
    description="PACKAGE DESCRIPTION",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katmai1/template-python-package",
    packages=setuptools.find_packages(),
    
    # OPTIONAL
    # entry_points = {
    #     'console_scripts': ['package_name_bin = package_name:main',],
    # },
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    install_requires=[
        'versionner',
    ],
)