"""Reusable cryptopals module."""

from base64 import b64encode
from binascii import hexlify, unhexlify

def hex_to_base64(s):
    """Converts a hex string to base64."""
    return b64encode(unhexlify(s))

def fixed_xor(s1, s2):
    """XORs two hex strings."""
    return hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s2):]), unhexlify(s2))))


