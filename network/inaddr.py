# inaddr.py
# Copyright (c) 2012 Maxim Kolosov

from ctypes import *

class S_UN_B(Structure):
	_fields_ = [('s_b1', c_ubyte),
	('s_b2', c_ubyte),
	('s_b3', c_ubyte),
	('s_b4', c_ubyte)]
class S_UN_W(Structure):
	_fields_ = [('s_w1', c_ushort), ('s_w2', c_ushort)]
class S_UN(Union):
	_fields_ = [('S_un_b', S_UN_B), ('S_un_w', S_UN_W), ('S_addr', c_ulong)]
class IN_ADDR(Structure):
	_fields_ = [('S_un', S_UN)]
PIN_ADDR = POINTER(IN_ADDR)

#define s_addr  S_un.S_addr /* can be used for most tcp & ip code */
#define s_host  S_un.S_un_b.s_b2    // host on imp
#define s_net   S_un.S_un_b.s_b1    // network
#define s_imp   S_un.S_un_w.s_w2    // imp
#define s_impno S_un.S_un_b.s_b4    // imp #
#define s_lh    S_un.S_un_b.s_b3    // logical host
