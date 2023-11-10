"""""""""""
ETROC-DAQ++
"""""""""""

A new and improved DAQ for standalone ETROC testing

* Free software: Zlib license

====================
Running the software
====================
We will use a venv to isolate the ETROC-DAQ++ python installation and dependencies from that of the system and other venvs.
Create the venv with: ``python -m venv venv``.
Venv creation only needs to be done once and occasionally when you upgrade the python version installed on the system.

Before running any commands related to the DAQ, activate the venv with: ``source venv/bin/activate``

Once you are finished, you may deactivate the venv with: ``deactivate``

---------------------------
Dependencies & Installation
---------------------------
There are two options, you can run the ETROC-DAQ++ from source or from `PyPI <https://pypi.org/>`_ (Recommended).

From PyPI
---------
Make sure you activate the venv first, then simply run the command: ``python -m pip install ETROC-DAQ2``

From Source
-----------
Fetch the source from github, you may for instance clone the git repository to a local directory.
Make sure the venv is activated, then install this application with all its dependencies by running this command from the source directory: ``python -m pip install .``

----------------
Dev Dependencies
----------------
If you are working on developing the code for ETROC-DAQ++ you will need to follow the "Running the Software" instructions for setup and then for installing use the "From Source" instructions but instead of the install command in the "Dependencies" instructions, use the following command: ``python -m pip install -e .``.
Then install a few other dependencies which are only used in development:

.. code::

  python -m pip install --upgrade pytest
  python -m pip install --upgrade bump2version
  python -m pip install --upgrade pylint
  python -m pip install --upgrade build
  python -m pip install --upgrade twine

========
Dev Info
========
We are using pytest to run unit tests on the software.
See `here <https://docs.pytest.org/en/7.4.x/getting-started.html>`_ for ideas on how to get started.
Use the command `pytest` to run all the tests.

We are using bump2version to manage the version string of the software.
bump2version will automatically create a commit and a tag with the version when you use it:

- To increase the major version, use: ``bump2version major``; for example 0.1.3 to 1.0.0
- To increase the minor version, use: ``bump2version minor``; for example 0.1.3 to 0.2.0
- To increase the patch version, use: ``bump2version patch``; for example 0.1.3 to 0.1.4

We are using pylint to check the style of python code.
There is a github workflow which runs automatically on push, but you can also run it on your own with: ``pylint [file]``.
A useful command is ``pylint src`` which will check the full distribution.

The build tool is used to package the code for publishing on PyPI.
Build the release with: ``python -m build``

The twine tool is used to upload the package to PyPI.
Once the distribution files are generated with the build tool, then upload them with: ``python -m twine upload --repository testpypi dist/*``

-----------------
Restructured Text
-----------------
For information on how to use restructured text, see the cheatsheet `here <https://github.com/DevDungeon/reStructuredText-Documentation-Reference>`_ for example.
But there are other resources on the internet if you prefer.

----------
Docstrings
----------
Please use docstrings in the "NumPy/SciPy docstrings" style: `link <https://numpydoc.readthedocs.io/en/latest/format.html>`_.

--------------
pyproject.toml
--------------
Get classifiers from `here <https://pypi.org/classifiers/>`_.

More information on packaging can be found `here <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_.

There is an entry point as explained in: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
This entry point is for running the DAQ.
The entry point can be ran with the following command: ``run-etroc-daq2``
