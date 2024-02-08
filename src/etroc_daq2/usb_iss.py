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
"""The USB ISS module

Contains the UsbIssI2C class, which connects to and communicates with a USB-ISS device in I2C mode

"""

from typing import Union

from usb_iss import UsbIss as UsbIssInt
from usb_iss import defs

valid_clocks = [20, 50, 100, 400, 1000]
software_clocks = [20, 50, 100, 400]
hardware_clocks = [100, 400, 1000]
use_dummy = True


class UsbIssI2C:
    """Class to handle the USB-ISS

    This class is a wrapper around the usb_iss library, providing a simplified interface for the
    usage in the ETROC DAQ assuming only I2C is used, with optional GPIO for the extra pins

    Parameters
    ----------
    port
        The port where the USB-ISS device can be found

    clock
        The clock frequency to use for I2C communication. It must be a valid clock from the
        list: 20, 50, 100, 400, 1000. For clock frequencies where there is both software and
        hardware support, the hardware version will be given precedence.

    use_serial
        Whether to use the extra pins on the USB-ISS as a serial interface, if not they will be
        GPIO (by default set to analog in). The serial port is only enabled if the baud rate is
        also set.

    baud_rate
        The baud rate to use for the serial communication

    verbose
        Whether to output detailed information to the terminal

    Raises
    ------
    SerialException
        If the serial object can not be found

    ValueError
        If a wrong value is passed to the clock configuration

    RuntimeError
        For other issues communicating with the USB-ISS device

    Examples
    --------
    >>> import etroc_daq2
    >>> usbiss = etroc_daq2.UsbIssI2C("/dev/ttyACM0")
    >>> usbiss.version()

    """

    _port: str
    _clock: int
    _verbose: bool
    _use_serial: bool
    _baud_rate: Union[int, None]
    _iss: UsbIssInt
    _version: int
    _serial: str

    def __init__(self, port: str, clock: int, use_serial: bool = False, baud_rate: Union[int, None] = None, verbose: bool = False):
        if clock not in valid_clocks:
            raise ValueError(f"Received a wrong clock value: {clock} Hz")

        self._port = port
        self._clock = clock
        self._verbose = verbose
        self._use_serial = use_serial
        self._baud_rate = baud_rate

        if self._use_serial and self._baud_rate is None:
            self._use_serial = False

        self._iss = UsbIssInt(dummy=use_dummy, verbose=self._verbose)
        self._iss.open(port)

        module_id = self._iss.read_module_id()
        if module_id != 7:
            raise RuntimeError(f"Got an unexpected value for the module ID of the USB-ISS device: {module_id}")

        self._version = self._iss.read_fw_version()
        self._serial = self._iss.read_serial_number()

        self.use_hardware = False
        if self._clock in hardware_clocks:
            self.use_hardware = True

        if not self._use_serial:
            self._iss.setup_i2c(self._clock, self.use_hardware, defs.IOType.ANALOGUE_INPUT, defs.IOType.ANALOGUE_INPUT)
        else:
            self._iss.setup_i2c_serial(self._clock, self.use_hardware, self._baud_rate)

    def __del__(self):
        if self._iss is not None:
            self._iss.close()

    @property
    def version(self) -> int:
        """The version property getter method

        This method returns the firmware version of the USB-ISS firmware

        Returns
        -------
        int
            The firmware version number.
        """
        return self._version

    @property
    def serial(self) -> str:
        """The serial_number property getter method

        This method returns the serial number of the USB-ISS firmware

        Returns
        -------
        str
            The serial number.
        """
        return self._serial
