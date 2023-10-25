# ETROC-DAQ++
A new and improved DAQ for standalone ETROC testing

## Running the software

We will use a venv to isolate the ETROC-DAQ++ python installation and dependencies from that of the system and other venvs. Create the venv with: `python -m venv venv`. Venv creation only needs to be done once and occasional when you upgrade th epython version installed on the system.

Before running any commands related to the DAQ, activate the venv with: `source venv/bin/activate`

Once you are finished, you may deactivate the venv with: `deactivate`

### Dependencies

### Dev Dependencies
If you are working on developing the code for ETROC-DAQ++ you will need to follow the "Running the Software" instructions as well as the "Dependencies" instructions in order to install all the base tools, then install a few other dependencies which are only used in development:
```
python -m pip install --upgrade bump2version
```

## Dev Info
We are using bump2version to manage the version string of the software. bump2version will automatically create a commit and a tag with the version when you use it:
  * To increase the major version, use: `bump2version major`; for example 0.1.3 to 1.0.0
  * To increase the minor version, use: `bump2version minor`; for example 0.1.3 to 0.2.0
  * To increase the patch version, use: `bump2version patch`; for example 0.1.3 to 0.1.4