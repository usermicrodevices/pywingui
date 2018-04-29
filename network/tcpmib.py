# tcpmib.py
# Copyright (c) 2012 Maxim Kolosov

ANY_SIZE = 1

TCPIP_OWNING_MODULE_SIZE = 16

MIB_TCP_STATE = 0
MIB_TCP_STATE_CLOSED     =  1
MIB_TCP_STATE_LISTEN     =  2
MIB_TCP_STATE_SYN_SENT   =  3
MIB_TCP_STATE_SYN_RCVD   =  4
MIB_TCP_STATE_ESTAB      =  5
MIB_TCP_STATE_FIN_WAIT1  =  6
MIB_TCP_STATE_FIN_WAIT2  =  7
MIB_TCP_STATE_CLOSE_WAIT =  8
MIB_TCP_STATE_CLOSING    =  9
MIB_TCP_STATE_LAST_ACK   = 10
MIB_TCP_STATE_TIME_WAIT  = 11
MIB_TCP_STATE_DELETE_TCB = 12

TCP_CONNECTION_OFFLOAD_STATE = 0
TcpConnectionOffloadStateInHost = 0
TcpConnectionOffloadStateOffloading = 1
TcpConnectionOffloadStateOffloaded = 2
TcpConnectionOffloadStateUploading = 3
TcpConnectionOffloadStateMax = 4

TCP_RTO_ALGORITHM = 0
TcpRtoAlgorithmOther = 0
TcpRtoAlgorithmConstant = 1
TcpRtoAlgorithmRsre = 2
TcpRtoAlgorithmVanj = 3
MIB_TCP_RTO_OTHER     = 1
MIB_TCP_RTO_CONSTANT  = 2
MIB_TCP_RTO_RSRE      = 3
MIB_TCP_RTO_VANJ      = 4

from ctypes import *

from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WINXP, NTDDI_LONGHORN
from in6addr import *

class _UNION(Union):
	_fields_ = [('dwOldFieldName', c_ulong), ('enumNewFieldName', c_int)]

class MIB_TCPROW_LH(Structure):
	_fields_ = [('u', _UNION),
	('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwRemoteAddr', c_ulong),
	('dwRemotePort', c_ulong)]
	_anonymous_ = ('u',)
PMIB_TCPROW_LH = POINTER(MIB_TCPROW_LH)

class MIB_TCPROW_W2K(Structure):
	_fields_ = [('dwState', c_ulong),
	('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwRemoteAddr', c_ulong),
	('dwRemotePort', c_ulong)]
PMIB_TCPROW_W2K = POINTER(MIB_TCPROW_W2K)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	MIB_TCPROW = MIB_TCPROW_LH
	PMIB_TCPROW = PMIB_TCPROW_LH
elif NTDDI_VERSION >= NTDDI_WIN2K:
	MIB_TCPROW = MIB_TCPROW_W2K
	PMIB_TCPROW = PMIB_TCPROW_W2K
else:
	MIB_TCPROW = MIB_TCPROW_LH
	PMIB_TCPROW = PMIB_TCPROW_LH

class MIB_TCPTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCPROW * ANY_SIZE)]
PMIB_TCPTABLE = POINTER(MIB_TCPTABLE)

class MIB_TCPROW2(Structure):
	_fields_ = [('dwState', c_ulong),
	('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwRemoteAddr', c_ulong),
	('dwRemotePort', c_ulong),
	('dwOwningPid', c_ulong),
	('dwOffloadState', c_ulong)]
PMIB_TCPROW2 = POINTER(MIB_TCPROW2)

class MIB_TCPTABLE2(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCPROW2 * ANY_SIZE)]
PMIB_TCPTABLE2 = POINTER(MIB_TCPTABLE2)

class MIB_TCPROW_OWNER_PID(Structure):
	_fields_ = [('dwState', c_ulong),
	('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwRemoteAddr', c_ulong),
	('dwRemotePort', c_ulong),
	('dwOwningPid', c_ulong)]
PMIB_TCPROW_OWNER_PID = POINTER(MIB_TCPROW_OWNER_PID)

class MIB_TCPTABLE_OWNER_PID(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCPROW_OWNER_PID * ANY_SIZE)]
PMIB_TCPTABLE_OWNER_PID = POINTER(MIB_TCPTABLE_OWNER_PID)

class MIB_TCPROW_OWNER_MODULE(Structure):
	_fields_ = [('dwState', c_ulong),
	('dwLocalAddr', c_ulong),
	('dwLocalPort', c_ulong),
	('dwRemoteAddr', c_ulong),
	('dwRemotePort', c_ulong),
	('dwOwningPid', c_ulong),
	('liCreateTimestamp', c_longlong),
	('OwningModuleInfo', c_ulonglong * TCPIP_OWNING_MODULE_SIZE)]
PMIB_TCPROW_OWNER_MODULE = POINTER(MIB_TCPROW_OWNER_MODULE)

class MIB_TCPTABLE_OWNER_MODULE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCPROW_OWNER_MODULE * ANY_SIZE)]
PMIB_TCPTABLE_OWNER_MODULE = POINTER(MIB_TCPTABLE_OWNER_MODULE)


# The following definitions require Winsock2.

class MIB_TCP6ROW(Structure):
	_fields_ = [('State', c_int),# enum MIB_TCP_STATE
	('LocalAddr', IN6_ADDR),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('RemoteAddr', IN6_ADDR),
	('dwRemoteScopeId', c_ulong),
	('dwRemotePort', c_ulong)]
PMIB_TCP6ROW = POINTER(MIB_TCP6ROW)

class MIB_TCP6TABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCP6ROW * ANY_SIZE)]
PMIB_TCP6TABLE = POINTER(MIB_TCP6TABLE)

class MIB_TCP6ROW2(Structure):
	_fields_ = [('LocalAddr', IN6_ADDR),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('RemoteAddr', IN6_ADDR),
	('dwRemoteScopeId', c_ulong),
	('dwRemotePort', c_ulong),
	('State', c_int),# enum MIB_TCP_STATE
	('dwOwningPid', c_ulong),
	('dwOffloadState', c_ulong)]# enum TCP_CONNECTION_OFFLOAD_STATE
PMIB_TCP6ROW2 = POINTER(MIB_TCP6ROW2)

class MIB_TCP6TABLE2(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCP6ROW2 * ANY_SIZE)]
PMIB_TCP6TABLE2 = POINTER(MIB_TCP6TABLE2)

class MIB_TCP6ROW_OWNER_PID(Structure):
	_fields_ = [('ucLocalAddr', c_ubyte * 16),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('ucRemoteAddr', c_ubyte * 16),
	('dwRemoteScopeId', c_ulong),
	('dwRemotePort', c_ulong),
	('dwState', c_ulong),
	('dwOwningPid', c_ulong)]
PMIB_TCP6ROW_OWNER_PID = POINTER(MIB_TCP6ROW_OWNER_PID)

class MIB_TCP6TABLE_OWNER_PID(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCP6ROW_OWNER_PID * ANY_SIZE)]
PMIB_TCP6TABLE_OWNER_PID = POINTER(MIB_TCP6TABLE_OWNER_PID)

class MIB_TCP6ROW_OWNER_MODULE(Structure):
	_fields_ = [('ucLocalAddr', c_ubyte * 16),
	('dwLocalScopeId', c_ulong),
	('dwLocalPort', c_ulong),
	('ucRemoteAddr', c_ubyte * 16),
	('dwRemoteScopeId', c_ulong),
	('dwRemotePort', c_ulong),
	('dwState', c_ulong),
	('dwOwningPid', c_ulong),
	('liCreateTimestamp', c_longlong),
	('OwningModuleInfo', c_ulonglong * TCPIP_OWNING_MODULE_SIZE)]
PMIB_TCP6ROW_OWNER_MODULE = POINTER(MIB_TCP6ROW_OWNER_MODULE)

class MIB_TCP6TABLE_OWNER_MODULE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_TCP6ROW_OWNER_MODULE * ANY_SIZE)]
PMIB_TCP6TABLE_OWNER_MODULE = POINTER(MIB_TCP6TABLE_OWNER_MODULE)

class MIB_TCPSTATS_LH(Structure):
	_fields_ = [('u', _UNION),
	('dwRtoMin', c_ulong),
	('dwRtoMax', c_ulong),
	('dwMaxConn', c_ulong),
	('dwActiveOpens', c_ulong),
	('dwPassiveOpens', c_ulong),
	('dwAttemptFails', c_ulong),
	('dwEstabResets', c_ulong),
	('dwCurrEstab', c_ulong),
	('dwInSegs', c_ulong),
	('dwOutSegs', c_ulong),
	('dwRetransSegs', c_ulong),
	('dwInErrs', c_ulong),
	('dwOutRsts', c_ulong),
	('dwNumConns', c_ulong)]
	_anonymous_ = ('u',)
PMIB_TCPSTATS_LH = POINTER(MIB_TCPSTATS_LH)

class MIB_TCPSTATS_W2K(Structure):
	_fields_ = [('dwRtoAlgorithm', c_ulong),
	('dwRtoMin', c_ulong),
	('dwRtoMax', c_ulong),
	('dwMaxConn', c_ulong),
	('dwActiveOpens', c_ulong),
	('dwPassiveOpens', c_ulong),
	('dwAttemptFails', c_ulong),
	('dwEstabResets', c_ulong),
	('dwCurrEstab', c_ulong),
	('dwInSegs', c_ulong),
	('dwOutSegs', c_ulong),
	('dwRetransSegs', c_ulong),
	('dwInErrs', c_ulong),
	('dwOutRsts', c_ulong),
	('dwNumConns', c_ulong)]
PMIB_TCPSTATS_W2K = POINTER(MIB_TCPSTATS_W2K)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	MIB_TCPSTATS = MIB_TCPSTATS_LH
	PMIB_TCPSTATS = PMIB_TCPSTATS_LH
elif NTDDI_VERSION >= NTDDI_WIN2K:
	MIB_TCPSTATS = MIB_TCPSTATS_W2K
	PMIB_TCPSTATS = PMIB_TCPSTATS_W2K
