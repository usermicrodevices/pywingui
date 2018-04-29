# udpmib.py
# Copyright (c) 2012 Maxim Kolosov

ANY_SIZE = 1

TCPIP_OWNING_MODULE_SIZE = 16


from ctypes import *

from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WINXP, NTDDI_LONGHORN
from in6addr import *

class _UNION(Union):
	_fields_ = [('dwOldFieldName', c_ulong), ('enumNewFieldName', c_int)]

class MIB_UDPROW(Structure):
	_fields_ = [('dwLocalAddr', c_ulong), ('dwLocalPort', c_ulong)]
PMIB_UDPROW = POINTER(MIB_UDPROW)

class MIB_UDPTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDPROW * ANY_SIZE)]
PMIB_UDPTABLE = POINTER(MIB_UDPTABLE)

class MIB_UDPROW_OWNER_PID(Structure):
	_fields_ = [('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwOwningPid', c_ulong)]
PMIB_UDPROW_OWNER_PID = POINTER(MIB_UDPROW_OWNER_PID)

class MIB_UDPTABLE_OWNER_PID(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDPROW_OWNER_PID * ANY_SIZE)]
PMIB_UDPTABLE_OWNER_PID = POINTER(MIB_UDPTABLE_OWNER_PID)

class SpecificPortBindStruct(Structure):
	_fields_ = [('SpecificPortBind', c_int)]

class _UNION_(Union):
	_fields_ = [('s', SpecificPortBindStruct), ('dwFlags', c_int)]
	_anonymous_ = ('s',)

class MIB_UDPROW_OWNER_MODULE(Structure):
	_fields_ = [('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwOwningPid', c_ulong),
	('liCreateTimestamp', c_longlong),
	('u', _UNION_),
	('OwningModuleInfo', c_ulonglong * TCPIP_OWNING_MODULE_SIZE)]
	_anonymous_ = ('u',)
PMIB_UDPROW_OWNER_MODULE = POINTER(MIB_UDPROW_OWNER_MODULE)

class MIB_UDPTABLE_OWNER_MODULE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDPROW_OWNER_MODULE * ANY_SIZE)]
PMIB_UDPTABLE_OWNER_MODULE = POINTER(MIB_UDPTABLE_OWNER_MODULE)


# The following definitions require Winsock2.

class MIB_UDP6ROW(Structure):
	_fields_ = [('dwLocalAddr', IN6_ADDR),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong)]
PMIB_UDP6ROW = POINTER(MIB_UDP6ROW)

class MIB_UDP6TABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDP6ROW * ANY_SIZE)]
PMIB_UDP6TABLE = POINTER(MIB_UDP6TABLE)

class MIB_UDP6ROW_OWNER_PID(Structure):
	_fields_ = [('ucLocalAddr', c_ubyte * 16),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('dwOwningPid', c_ulong)]
PMIB_UDP6ROW_OWNER_PID = POINTER(MIB_UDP6ROW_OWNER_PID)

class MIB_UDP6TABLE_OWNER_PID(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDP6ROW_OWNER_PID * ANY_SIZE)]
PMIB_UDP6TABLE_OWNER_PID = POINTER(MIB_UDP6TABLE_OWNER_PID)

class MIB_UDP6ROW_OWNER_MODULE(Structure):
	_fields_ = [('ucLocalAddr', c_ubyte * 16),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('dwOwningPid', c_ulong),
	('liCreateTimestamp', c_longlong),
	('u', _UNION_),
	('OwningModuleInfo', c_ulonglong * TCPIP_OWNING_MODULE_SIZE)]
	_anonymous_ = ('u',)
PMIB_UDP6ROW_OWNER_MODULE = POINTER(MIB_UDP6ROW_OWNER_MODULE)

class MIB_UDP6TABLE_OWNER_MODULE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_UDP6ROW_OWNER_MODULE * ANY_SIZE)]
PMIB_UDP6TABLE_OWNER_MODULE = POINTER(MIB_UDP6TABLE_OWNER_MODULE)

class MIB_UDPSTATS(Structure):
	_fields_ = [('dwInDatagrams', c_ulong),
	('dwNoPorts', c_ulong),
	('dwInErrors', c_ulong),
	('dwOutDatagrams', c_ulong),
	('dwNumAddrs', c_ulong)]
PMIB_UDPSTATS = POINTER(MIB_UDPSTATS)
