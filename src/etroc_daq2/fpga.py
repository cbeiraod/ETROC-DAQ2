class FPGA:
    """Base Class to handle an FPGA

    This is a base class, so specific child classes must be implemented on top of it which further
    define the placeholder functions defined in this base class.

    Parameters
    ----------
    param_name
        A placeholder parameter name

    Raises
    ------
    RuntimeError
        For the errors that may be raised

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
