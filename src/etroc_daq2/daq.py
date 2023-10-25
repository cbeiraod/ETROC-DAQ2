# -*- coding: utf-8 -*-
#############################################################################
# zlib License
#
# (C) 2023 Cristóvão Beirão da Cruz e Silva <cbeiraod@cern.ch>
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
#############################################################################
"""The DAQ module

Contains the DAQ class, which serves as the entry point for the DAQ process.

"""

from etroc_daq2 import __version__

class DAQ:
    """Class to handle the DAQ

    This is a temporary description

    Parameters
    ----------
    param_name
        A placeholder parameter name

    Raises
    ------
    RuntimeError
        For the errors that may be raised

    Examples
    --------
    >>> import etroc_daq2
    >>> daq = etroc_daq2.DAQ()
    >>> daq.start()

    """

    def __init__(self):
        pass

    @property
    def version(self) -> str:
        """The version property getter method

        This method returns the version of the DAQ library

        Returns
        -------
        str
            The string of the version.
        """
        return __version__

    def start(self):
        """Start the DAQ"""
        pass
