# ipmib.py
# Copyright (c) 2012 Maxim Kolosov

ANY_SIZE = 1

MIB_IPADDR_PRIMARY      = 0x0001 # Primary ipaddr
MIB_IPADDR_DYNAMIC      = 0x0004 # Dynamic ipaddr
MIB_IPADDR_DISCONNECTED = 0x0008 # Address is on disconnected interface
MIB_IPADDR_DELETED      = 0x0040 # Address being deleted
MIB_IPADDR_TRANSIENT    = 0x0080 # Transient address
MIB_IPADDR_DNS_ELIGIBLE = 0X0100 # Address is published in DNS.

MIB_IPROUTE_TYPE_OTHER    = 1
MIB_IPROUTE_TYPE_INVALID  = 2
MIB_IPROUTE_TYPE_DIRECT   = 3
MIB_IPROUTE_TYPE_INDIRECT = 4

MIB_IPROUTE_METRIC_UNUSED = -1
MIB_USE_CURRENT_TTL         = -1
MIB_USE_CURRENT_FORWARDING  = -1

ICMP6_INFOMSG_MASK = 0x80

MIB_IPFORWARD_TYPE = 0
MIB_IPROUTE_TYPE_OTHER    = 1
MIB_IPROUTE_TYPE_INVALID  = 2
MIB_IPROUTE_TYPE_DIRECT   = 3
MIB_IPROUTE_TYPE_INDIRECT = 4

MIB_IPNET_TYPE = 0
MIB_IPNET_TYPE_OTHER   = 1
MIB_IPNET_TYPE_INVALID = 2
MIB_IPNET_TYPE_DYNAMIC = 3
MIB_IPNET_TYPE_STATIC  = 4

MIB_IPSTATS_FORWARDING = 0
MIB_IP_FORWARDING     = 1
MIB_IP_NOT_FORWARDING = 2


from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WINXP, NTDDI_WINXPSP1, NTDDI_LONGHORN
from ifmib import *

class MIB_IPADDRROW_XP(Structure):
	_fields_ = [('dwAddr', c_ulong),
	('dwIndex', c_ulong),# enum IF_INDEX
	('dwMask', c_ulong),
	('dwBCastAddr', c_ulong),
	('dwReasmSize', c_ulong),
	('unused1', c_ushort),
	('wType', c_ushort)]
PMIB_IPADDRROW_XP = POINTER(MIB_IPADDRROW_XP)

class MIB_IPADDRROW_W2K(Structure):
	_fields_ = [('dwAddr', c_ulong),
	('dwIndex', c_ulong),# enum IF_INDEX
	('dwMask', c_ulong),
	('dwBCastAddr', c_ulong),
	('dwReasmSize', c_ulong),
	('unused1', c_ushort),
	('unused2', c_ushort)]
PMIB_IPADDRROW_W2K = POINTER(MIB_IPADDRROW_W2K)

if NTDDI_VERSION >= NTDDI_WINXP:
	MIB_IPADDRROW = MIB_IPADDRROW_XP
	PMIB_IPADDRROW = PMIB_IPADDRROW_XP
elif NTDDI_VERSION >= NTDDI_WIN2K:
	MIB_IPADDRROW = MIB_IPADDRROW_W2K
	PMIB_IPADDRROW = PMIB_IPADDRROW_W2K
else:
	MIB_IPADDRROW = MIB_IPADDRROW_XP
	PMIB_IPADDRROW = PMIB_IPADDRROW_XP

class MIB_IPADDRTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', PMIB_IPADDRROW * ANY_SIZE)]
PMIB_IPADDRTABLE = POINTER(MIB_IPADDRTABLE)

class MIB_IPFORWARDNUMBER(Structure):
	_fields_ = [('dwValue', c_ulong)]
PMIB_IPFORWARDNUMBER = POINTER(MIB_IPFORWARDNUMBER)

class _UNION(Union):
	_fields_ = [('dwOldFieldName', c_ulong), ('enumNewFieldName', c_int)]

class MIB_IPFORWARDROW(Structure):
	_fields_ = [('dwForwardDest', c_ulong),
	('dwForwardMask', c_ulong),
	('dwForwardPolicy', c_ulong),
	('dwForwardNextHop', c_ulong),
	('dwForwardIfIndex', c_ulong),
	('u1', _UNION),
	('u2', _UNION),
	('dwForwardAge', c_ulong),
	('dwForwardNextHopAS', c_ulong),
	('dwForwardMetric1', c_ulong),
	('dwForwardMetric2', c_ulong),
	('dwForwardMetric3', c_ulong),
	('dwForwardMetric4', c_ulong),
	('dwForwardMetric5', c_ulong)]
	_anonymous_ = ('u1', 'u2')
PMIB_IPFORWARDROW = POINTER(MIB_IPFORWARDROW)

class MIB_IPFORWARDTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong),
	('table', MIB_IPFORWARDROW * ANY_SIZE)]
PMIB_IPFORWARDTABLE = POINTER(MIB_IPFORWARDTABLE)

class MIB_IPNETROW_LH(Structure):
	_fields_ = [('dwIndex', c_ulong),
	('dwPhysAddrLen', c_ulong),
	('bPhysAddr', c_ubyte * MAXLEN_PHYSADDR),
	('dwAddr', c_ulong),
	('u', _UNION)]
	_anonymous_ = ('u',)
PMIB_IPNETROW_LH = POINTER(MIB_IPNETROW_LH)

class MIB_IPNETROW_W2K(Structure):
	_fields_ = [('dwIndex', c_ulong),
	('dwPhysAddrLen', c_ulong),
	('bPhysAddr', c_ubyte * MAXLEN_PHYSADDR),
	('dwAddr', c_ulong),
	('dwType', c_ulong)]
PMIB_IPNETROW_W2K = POINTER(MIB_IPNETROW_W2K)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	MIB_IPNETROW = MIB_IPNETROW_LH
	PMIB_IPNETROW = PMIB_IPNETROW_LH
elif NTDDI_VERSION >= NTDDI_WIN2K:
	MIB_IPNETROW = MIB_IPNETROW_W2K
	PMIB_IPNETROW = PMIB_IPNETROW_W2K
else:
	MIB_IPNETROW = MIB_IPNETROW_LH
	PMIB_IPNETROW = PMIB_IPNETROW_LH

class MIB_IPNETTABLE(Structure):
	_fields_ = [('dwNumEntries', c_ulong), ('table', MIB_IPNETROW * ANY_SIZE)]
PMIB_IPNETTABLE = POINTER(MIB_IPNETTABLE)

class MIB_IPSTATS_LH(Structure):
	_fields_ = [('u', _UNION),
	('dwDefaultTTL', c_ulong),
	('dwInReceives', c_ulong),
	('dwInHdrErrors', c_ulong),
	('dwInAddrErrors', c_ulong),
	('dwForwDatagrams', c_ulong),
	('dwInUnknownProtos', c_ulong),
	('dwInDiscards', c_ulong),
	('dwInDelivers', c_ulong),
	('dwOutRequests', c_ulong),
	('dwRoutingDiscards', c_ulong),
	('dwOutDiscards', c_ulong),
	('dwOutNoRoutes', c_ulong),
	('dwReasmTimeout', c_ulong),
	('dwReasmReqds', c_ulong),
	('dwReasmOks', c_ulong),
	('dwReasmFails', c_ulong),
	('dwFragOks', c_ulong),
	('dwFragFails', c_ulong),
	('dwFragCreates', c_ulong),
	('dwNumIf', c_ulong),
	('dwNumAddr', c_ulong),
	('dwNumRoutes', c_ulong)]
	_anonymous_ = ('u',)
PMIB_IPSTATS_LH = POINTER(MIB_IPSTATS_LH)

class MIB_IPSTATS_W2K(Structure):
	_fields_ = [('dwForwarding', c_ulong),
	('dwDefaultTTL', c_ulong),
	('dwInReceives', c_ulong),
	('dwInHdrErrors', c_ulong),
	('dwInAddrErrors', c_ulong),
	('dwForwDatagrams', c_ulong),
	('dwInUnknownProtos', c_ulong),
	('dwInDiscards', c_ulong),
	('dwInDelivers', c_ulong),
	('dwOutRequests', c_ulong),
	('dwRoutingDiscards', c_ulong),
	('dwOutDiscards', c_ulong),
	('dwOutNoRoutes', c_ulong),
	('dwReasmTimeout', c_ulong),
	('dwReasmReqds', c_ulong),
	('dwReasmOks', c_ulong),
	('dwReasmFails', c_ulong),
	('dwFragOks', c_ulong),
	('dwFragFails', c_ulong),
	('dwFragCreates', c_ulong),
	('dwNumIf', c_ulong),
	('dwNumAddr', c_ulong),
	('dwNumRoutes', c_ulong)]
PMIB_IPSTATS_W2K = POINTER(MIB_IPSTATS_W2K)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	MIB_IPSTATS = MIB_IPSTATS_LH
	PMIB_IPSTATS = PMIB_IPSTATS_LH
elif NTDDI_VERSION >= NTDDI_WIN2K:
	MIB_IPSTATS = MIB_IPSTATS_W2K
	PMIB_IPSTATS = PMIB_IPSTATS_W2K

class MIBICMPSTATS(Structure):
	_fields_ = [('dwMsgs', c_ulong),
	('dwErrors', c_ulong),
	('dwDestUnreachs', c_ulong),
	('dwTimeExcds', c_ulong),
	('dwParmProbs', c_ulong),
	('dwSrcQuenchs', c_ulong),
	('dwRedirects', c_ulong),
	('dwEchos', c_ulong),
	('dwEchoReps', c_ulong),
	('dwTimestamps', c_ulong),
	('dwTimestampReps', c_ulong),
	('dwAddrMasks', c_ulong),
	('dwAddrMaskReps', c_ulong)]
PMIBICMPSTATS = POINTER(MIBICMPSTATS)

class MIBICMPINFO(Structure):
	_fields_ = [('icmpInStats', MIBICMPSTATS), ('icmpOutStats', MIBICMPSTATS)]

class MIB_ICMP(Structure):
	_fields_ = [('stats', MIBICMPINFO)]
PMIB_ICMP = POINTER(MIB_ICMP)

class MIBICMPSTATS_EX_XPSP1(Structure):
	_fields_ = [('dwMsgs', c_ulong),
	('dwErrors', c_ulong),
	('rgdwTypeCount', c_ulong * 256)]
PMIBICMPSTATS_EX_XPSP1 = POINTER(MIBICMPSTATS_EX_XPSP1)
if NTDDI_VERSION >= NTDDI_WINXPSP1:
	MIBICMPSTATS_EX = MIBICMPSTATS_EX_XPSP1
	PMIBICMPSTATS_EX = PMIBICMPSTATS_EX_XPSP1

class MIB_ICMP_EX_XPSP1(Structure):
	_fields_ = [('icmpInStats', MIBICMPSTATS_EX), ('icmpOutStats', MIBICMPSTATS_EX)]
PMIB_ICMP_EX_XPSP1 = POINTER(MIB_ICMP_EX_XPSP1)
if NTDDI_VERSION >= NTDDI_WINXPSP1:
	MIB_ICMP_EX = MIB_ICMP_EX_XPSP1
	PMIB_ICMP_EX = PMIB_ICMP_EX_XPSP1
