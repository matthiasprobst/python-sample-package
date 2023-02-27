# Testing
Go to the repository directory. For running all tests call

    pytest

To get a coverage report run (you need the package `pytest-cov`):

    pytest --cov --cov-report html
    
This will create a folder `covhtml/` with an `index.html` file in it.

Also, you might want to run `pylint` (static code analysis):

    pylint h5rdmtoolbox --output=.pylint
