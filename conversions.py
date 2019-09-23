"""CONVERSIONS."""


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': 'Florian Zah',
'Credits': [],
'Date': '18.09.2019',
'Description': 'Different conversion to and from: hex, bin, ascii, ...',
'Last Modification': 'dd.mm.yyyy',
'Licence': '',
'Maintainer': 'Florian Zah',
'Status': 'Production',
'Tags': ['convert', 'conversion', 'hex', 'ascii', 'bin', 'encode', 'decode', 'encript', 'decript'],
'Title': 'CONVERSION',
'Usage': '.',
'Version': '1.0.0'}
"""

def hex_to_ascii(text):
    """Convert from hex to ascii."""
    text = text.replace('0x', '') #  daca e sub forma 0x: 0x680x740x740x70
    print(bytes.fromhex(text).decode('utf-8'))


hex_to_ascii(b)


def ascii_to_hex(text):
    """."""
    text_final = ''
    for letter in text:
        h = str(hex(ord(letter)))
        text_final += h
    print(text_final)


#  ascii_to_hex('char')


def binary_to_ascii(text):
    """b_to_a = binary to ascii; 01010011 0110111 00100000 = 8 bit/char."""
    n = int(text, 2)
    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())


#  binary_to_ascii()


def ascii_to_binary(text):
    """a_to_b = ascii to binary."""
    print(bin(int.from_bytes(text.encode(), 'big')))


#  ascii_to_binary()
