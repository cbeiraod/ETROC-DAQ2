from .fpga import FPGA


class LegacyFPGA(FPGA):
    """Class to handle an FPGA using the legacy Eth communication protocol

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
        return 0

    def start(self):
        """Start the DAQ"""
        pass
