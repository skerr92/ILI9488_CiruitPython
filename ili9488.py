try:
    # used for typing only
    from typing import Any
except ImportError:
    pass

import displayio

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/skerr92/ILI9488_CircuitPython.git"

_INIT_SEQUENCE = (
    b"\xE0\x00\x03\x09\x08\x16\x0A\x3F\x78\x4C\x09\x0A\x08\x16\x1A\x0F"
    b"\xE1\x00\x16\x19\x03\x0F\x05\x32\x45\x46\x04\x0E\x0D\x35\x37\x0F"
    b"\xC0\x17\x15"
    b"\xC1\x41"
    b"\xC5\x00\x12\x80"
    b"\x36\48"
    b"\x3A\x66"
    b"\xB0\x00"
    b"\xB1\xA0"
    b"\xB4\x02"
    b"\xB6\x02\x02\x3B"
    b"\xB7\xC6"
    b"\xF7\xA9\x51\x2C\x82"
    b"\x11\x80\x78"  # Exit Sleep then delay 0x78 (120ms)
    b"\x29\x80\x78"  # Display on then delay 0x78 (120ms)
)


# pylint: disable=too-few-public-methods
class ILI9488(displayio.Display):
    """
    ILI9488 display driver

    :param displayio.FourWire bus: bus that the display is connected to
    """

    def __init__(self, bus: displayio.FourWire, **kwargs: Any):
        super().__init__(bus, _INIT_SEQUENCE, **kwargs)
