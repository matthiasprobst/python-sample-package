Overview
========

This is a sample package

.. note::

   This project is under current development!

The packges comes with a sub-package:
  - :doc:`subpackage/index`: Naming standards mostly for attributes in the HDF5 files


Installation
------------
The repository requires python 3.8. or higher.

Install from source from github:

.. code:: sh

   python3.8 -m pip install https://github.com/matthiasprobst/python-sample-package

Clone and install from source:

.. code:: sh

   git clone https://github.com/matthiasprobst/python-sample-package
   python3.8 -m pip install samplepackage/

You may install optional dependencies:

.. code:: sh

   python3.8 -m pip install "samplepackage[scipy]"  # installs dependencies to convert datasets to vtk
   python3.8 -m pip install "samplepackage[test]"  # installs pytecplot to build tecplot-readable HDF5 files
   python3.8 -m pip install "samplepackage[docs]"  # installs e.g. netCDF4 which isneeded to convt n files
   python3.8 -m pip install "samplepackage[complete]"  # installs all avbove plus dependencies for testing and documentation


.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Documentation

    Getting Started <gettingstarted/index>
    subpackage <subpackage/index>

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Repository

   GitHub Repository <https://github.com/matthiasprobst/python-sample-package>

