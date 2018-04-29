# in6addr.py
# Copyright (c) 2012 Maxim Kolosov

# IPv6 Internet address (RFC 2553)
# This is an 'on-wire' format structure.

from ctypes import *

class IN6_ADDR(Structure):
	_fields_ = [('Byte', c_ubyte * 16), ('Word', c_ushort * 8)]
PIN6_ADDR = POINTER(IN6_ADDR)
