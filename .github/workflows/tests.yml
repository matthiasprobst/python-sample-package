name: Tests

on:
  push:
    branches:
      - main
      - dev


jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      max-parallel: 4
      matrix:
        os: [ ubuntu-latest, windows-latest ]
        python-version: ['3.7', '3.8', '3.9', '3.10']
    steps:
    - uses: actions/checkout@v1
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
    - name: Run pytest coverage
      run: |
        pytest --cov=samplepackage --cov-report=xml
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
        file: ./coverage.xml
