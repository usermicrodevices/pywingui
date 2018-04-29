# ifmib.py
# Copyright (c) 2012 Maxim Kolosov

ANY_SIZE = 1

MAXLEN_PHYSADDR = 8
MAXLEN_IFDESCR = 256
MAX_INTERFACE_NAME_LEN = 256

from ctypes import *

class MIB_IFNUMBER(Structure):
	_fields_ = [('dwValue', c_ulong)]
PMIB_IFNUMBER = POINTER(MIB_IFNUMBER)

class MIB_IFROW(Structure):
	_fields_ = [('wszName', c_wchar * MAX_INTERFACE_NAME_LEN),
	('dwIndex', c_ulong),# enum IF_INDEX
	('dwType', c_ulong),# enum IFTYPE
	('dwMtu', c_ulong),
	('dwSpeed', c_ulong),
	('dwPhysAddrLen', c_ulong),
	('bPhysAddr', c_ubyte * MAXLEN_PHYSADDR),
	('dwAdminStatus', c_ulong),
	('dwOperStatus', c_ulong),# enum INTERNAL_IF_OPER_STATUS
	('dwLastChange', c_ulong),
	('dwInOctets', c_ulong),
	('dwInUcastPkts', c_ulong),
	('dwInNUcastPkts', c_ulong),
	('dwInDiscards', c_ulong),
	('dwInErrors', c_ulong),
	('dwInUnknownProtos', c_ulong),
	('dwOutOctets', c_ulong),
	('dwOutUcastPkts', c_ulong),
	('dwOutNUcastPkts', c_ulong),
	('dwOutDiscards', c_ulong),
	('dwOutErrors', c_ulong),
	('dwOutQLen', c_ulong),
	('dwDescrLen', c_ulong),
	('bDescr', c_ubyte * MAXLEN_IFDESCR)]
PMIB_IFROW = POINTER(MIB_IFROW)

class MIB_IFTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_IFROW * ANY_SIZE)]
PMIB_IFTABLE = POINTER(MIB_IFTABLE)
