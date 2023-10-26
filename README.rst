"""""""""""
ETROC-DAQ++
"""""""""""

A new and improved DAQ for standalone ETROC testing

====================
Running the software
====================

We will use a venv to isolate the ETROC-DAQ++ python installation and dependencies from that of the system and other venvs. Create the venv with: `python -m venv venv`. Venv creation only needs to be done once and occasional when you upgrade th epython version installed on the system.

Before running any commands related to the DAQ, activate the venv with: `source venv/bin/activate`

Once you are finished, you may deactivate the venv with: `deactivate`

------------
Dependencies
------------
Make sure you activate the venv first, then install this application with all its dependencies: `pip install .`

----------------
Dev Dependencies
----------------
If you are working on developing the code for ETROC-DAQ++ you will need to follow the "Running the Software" instructions for setup and then instead of the install command in the "Dependencies" instructions, use the following command: `pip install -e .`.
Then install a few other dependencies which are only used in development:
```
python -m pip install --upgrade pytest
python -m pip install --upgrade bump2version
python -m pip install --upgrade build
python -m pip install --upgrade twine
```
========
Dev Info
========
We are using pytest to run unit tests on the software. See [here](https://docs.pytest.org/en/7.4.x/getting-started.html) for ideas on how to get started. Use the command `pytest` to run all the tests.

We are using bump2version to manage the version string of the software. bump2version will automatically create a commit and a tag with the version when you use it:
  * To increase the major version, use: `bump2version major`; for example 0.1.3 to 1.0.0
  * To increase the minor version, use: `bump2version minor`; for example 0.1.3 to 0.2.0
  * To increase the patch version, use: `bump2version patch`; for example 0.1.3 to 0.1.4

The build tool is used to package the code for publishing on PyPI. Build the release with `python -m build`

The twine tool is used to upload the package to PyPI. Once the distribution files are generated with the build tool, then upload them with: `python -m twine upload --repository testpypi dist/*`

---
Restructured Text
-----------------
For information on how to use restructured text, see the cheatsheet [here](https://github.com/DevDungeon/reStructuredText-Documentation-Reference) for example.
But there are other resources on the internet if you prefer.

----------
Docstrings
----------
Please use docstrings in the "NumPy/SciPy docstrings" style: [link](https://numpydoc.readthedocs.io/en/latest/format.html).

--------------
pyproject.toml
--------------
Get classifiers from [here](https://pypi.org/classifiers/)

More information on packaging can be found [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

There is an entry point as explained in: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
This entry point is for running the DAQ.
The entry point can be ran with the following command: `run-etroc-daq2`
