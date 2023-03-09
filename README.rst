Sample package
==============

|Codecov|

Sample package including general package structure, testing with pytest and documentation with sphinx.

If you want to create your own package, you can use this package as a starting point.

*Note, that the repository is under current development!*

Installation
------------
If you use `anaconda`, you may first create an environment:

     conda create -n sampleprojet python=3.8
     conda activate samplepackage

Here's a conda [cheatsheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).

Navigate to the repository directory.

For development:

    pip install -e ".[complete]"

otherwise

    pip install ".[complete]"

To only install special functionality, e.g. only vtk support in addition to core dependencies, run:

    pip install (-e) ".[docs]"


Documentation
-------------
Documentation can be build following the README.md in the doc/ folder

Testing
-------
Go [here](samplepackage/tests/README.md) for instructions on how to run tests.


Contribution
------------
Feel free to contribute.

Publishing
----------
See [here](https://packaging.python.org/tutorials/packaging-projects/) for more information.
Here's a quick summary:

    # generate distribution packages
    python -m pip install --upgrade build
    python -m build

    # upload to pypi
    python -m pip install --upgrade twine
    python -m twine upload --repository testpypi dist/*

    # Install from testpypi:
    py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

    # If everything worked until here, upload to pip:
    python -m twine upload dist/*


GitHub Actions
--------------
[Quickstart](https://docs.github.com/en/actions/quickstart)

To get code coverage, you need register at codecov.io and add a token to your repository secrets. Everything
will be explained [here](https://app.codecov.io/gh/<github-account>/<your-repo-name>/new)
Then add the image to your README file.

.. |Codecov| image:: https://codecov.io/gh/matthiasprobst/python-sample-package/branch/dev/graph/badge.svg
    :target: https://codecov.io/gh/matthiasprobst/python-sample-package