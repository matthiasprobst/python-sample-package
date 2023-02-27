# Sample package

Sample package including general package structure, testing with pytest and documentation with sphinx.

If you want to create your own package, you can use this package as a starting point.

*Note, that the repository is under current development!*

## Installation
If you use `anaconda`, you may first create an environment:

     conda create -n sampleprojet python=3.8
     conda activate samplepackage

Navigate to the repository directory.

For development:

    pip install -e ".[complete]"
otherwise

    pip install ".[complete]"

To only install special functionality, e.g. only vtk support in addition to core dependencies, run:

    pip install (-e) ".[docs]"


## Documentation
Documentation can be build following the README.md in the doc/ folder

## Testing
Go [here](samplepackage/tests/README.md) for instructions on how to run tests.


## Contribution
Feel free to contribute.
