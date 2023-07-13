# SPDX-FileCopyrightText: 2023 Oak Development Technologies
# SPDX-License-Identifier: MIT
# Generic Circuit Python Driver for ILI9488 320x480 displays
try:
    # used for typing only
    from typing import Any
except ImportError:
    pass

import displayio

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/skerr92/ILI9488_CircuitPython.git"

_INIT_SEQUENCE = (
    b"\xE0\x00\x07\x0C\x05\x13\x09\x36\xAA\x46\x09\x10\x0D\x1A\x1E\x1F"
    b"\xE1\x00\x20\x23\x04\x10\x06\x37\x56\x49\x04\x0C\x0A\x33\x37\x0F"
    b"\xC0\x0E\x0E"
    b"\xC1\x44"
    b"\xC5\x00\x40\x00\x40"
    b"\x36\x48"
    b"\x3A\x66"
    b"\xB0\x00"
    b"\xB1\xA0\x11"
    b"\xB4\x02"
    b"\xB6\x02\x02\x3B"
    b"\xB7\x06"
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
