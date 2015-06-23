"""Reusable cryptopals module."""

import base64

def hex_to_base64(string):
    """Converts a hex string to base64."""
    return base64.b64encode(bytearray.fromhex(string).decode())
