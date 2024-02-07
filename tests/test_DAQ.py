import pytest


def test_version():
    import etroc_daq2

    version = '0.0.0'

    assert version == etroc_daq2.DAQ().version
