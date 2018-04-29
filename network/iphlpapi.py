# iphlpapi.py
# Copyright (c) 2012 Maxim Kolosov

NET_ADDRESS_FORMAT_ = 0
NET_ADDRESS_FORMAT = 0
NET_ADDRESS_FORMAT_UNSPECIFIED = 0
NET_ADDRESS_DNS_NAME = 1
NET_ADDRESS_IPV4 = 2
NET_ADDRESS_IPV6 = 3

NET_STRING_IPV4_ADDRESS = 0x00000001
# The string identifies an IPv4 Host/router using literal address.
# (port or prefix not allowed) 
NET_STRING_IPV4_SERVICE = 0x00000002
# The string identifies an IPv4 service using literal address.
# (port required; prefix not allowed) 
NET_STRING_IPV4_NETWORK = 0x00000004
# The string identifies an IPv4 network.
# (prefix required; port not allowed) 
NET_STRING_IPV6_ADDRESS = 0x00000008
# The string identifies an IPv6 Host/router using literal address.
# (port or prefix not allowed; scope-id allowed) 
NET_STRING_IPV6_ADDRESS_NO_SCOPE = 0x00000010
# The string identifies an IPv6 Host/router using literal address
# where the interface context is already known.
# (port or prefix not allowed; scope-id not allowed) 
NET_STRING_IPV6_SERVICE = 0x00000020
# The string identifies an IPv6 service using literal address.
# (port required; prefix not allowed; scope-id allowed) 
NET_STRING_IPV6_SERVICE_NO_SCOPE = 0x00000040
# The string identifies an IPv6 service using literal address
# where the interface context is already known.
# (port required; prefix not allowed; scope-id not allowed) 
NET_STRING_IPV6_NETWORK = 0x00000080
# The string identifies an IPv6 network.
# (prefix required; port or scope-id not allowed) 
NET_STRING_NAMED_ADDRESS = 0x00000100
# The string identifies an Internet Host using DNS.
# (port or prefix or scope-id not allowed) 
NET_STRING_NAMED_SERVICE = 0x00000200
# The string identifies an Internet service using DNS.
# (port required; prefix or scope-id not allowed)

NET_STRING_IP_ADDRESS = NET_STRING_IPV4_ADDRESS | NET_STRING_IPV6_ADDRESS
NET_STRING_IP_ADDRESS_NO_SCOPE = NET_STRING_IPV4_ADDRESS | NET_STRING_IPV6_ADDRESS_NO_SCOPE
NET_STRING_IP_SERVICE = NET_STRING_IPV4_SERVICE | NET_STRING_IPV6_SERVICE
NET_STRING_IP_SERVICE_NO_SCOPE = NET_STRING_IPV4_SERVICE | NET_STRING_IPV6_SERVICE_NO_SCOPE
NET_STRING_IP_NETWORK = NET_STRING_IPV4_NETWORK | NET_STRING_IPV6_NETWORK
NET_STRING_ANY_ADDRESS = NET_STRING_NAMED_ADDRESS | NET_STRING_IP_ADDRESS
NET_STRING_ANY_ADDRESS_NO_SCOPE = NET_STRING_NAMED_ADDRESS | NET_STRING_IP_ADDRESS_NO_SCOPE
NET_STRING_ANY_SERVICE = NET_STRING_NAMED_SERVICE | NET_STRING_IP_SERVICE
NET_STRING_ANY_SERVICE_NO_SCOPE = NET_STRING_NAMED_SERVICE | NET_STRING_IP_SERVICE_NO_SCOPE

#from socket import AF_INET
AF_UNSPEC = 0
AF_INET = 2

from ctypes import *

from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WIN2KSP1, NTDDI_WINXPSP1, NTDDI_LONGHORN
from ipexport import *
from ipifcons import *
from iptypes import *
from ifmib import *
from ipmib import *
from tcpmib import *
from udpmib import *

_GetNumberOfInterfaces = WINFUNCTYPE(c_ulong, c_void_p)(('GetNumberOfInterfaces', windll.iphlpapi))
def GetNumberOfInterfaces():
	'Retrieves the number of interfaces in the system. These include LAN and WAN interfaces'
	result2 = c_ulong()
	result1 = _GetNumberOfInterfaces(byref(result2))
	return result1, result2

_GetIfEntry = WINFUNCTYPE(c_ulong, c_void_p)(('GetIfEntry', windll.iphlpapi))
def GetIfEntry(pIfRow = None):
	'Gets the MIB-II ifEntry. The dwIndex field of the MIB_IFROW should be set to the index of the interface being queried'
	if not pIfRow:
		pIfRow = PMIB_IFROW()
	return _GetIfEntry(pIfRow)

_GetIfTable = WINFUNCTYPE(c_ulong, PMIB_IFTABLE, c_void_p, c_bool)(('GetIfTable', windll.iphlpapi))
def GetIfTable(pdwSize = None, bOrder = True):
	'Gets the MIB-II IfTable'
	pIfTable = PMIB_IFTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetIfTable(pIfTable, byref(pdwSize), bOrder)
	return result, pIfTable

_GetIpAddrTable = WINFUNCTYPE(c_ulong, PMIB_IPADDRTABLE, c_void_p, c_bool)(('GetIpAddrTable', windll.iphlpapi))
def GetIpAddrTable(pdwSize = None, bOrder = True):
	'Gets the Interface to IP Address mapping'
	pIpAddrTable = PMIB_IPADDRTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetIpAddrTable(pIpAddrTable, byref(pdwSize), bOrder)
	return result, pIpAddrTable

_GetIpNetTable = WINFUNCTYPE(c_ulong, PMIB_IPNETTABLE, c_void_p, c_bool)(('GetIpNetTable', windll.iphlpapi))
def GetIpNetTable(pdwSize = None, bOrder = True):
	'Gets the current IP Address to Physical Address (ARP) mapping'
	IpNetTable = PMIB_IPNETTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetIpNetTable(IpNetTable, byref(pdwSize), bOrder)
	return result, IpNetTable

_GetIpForwardTable = WINFUNCTYPE(c_ulong, PMIB_IPFORWARDTABLE, c_void_p, c_bool)(('GetIpForwardTable', windll.iphlpapi))
def GetIpForwardTable(pdwSize = None, bOrder = True):
	'Gets the IP Routing Table  (RFX XXXX)'
	pIpForwardTable = PMIB_IPFORWARDTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetIpForwardTable(pIpForwardTable, byref(pdwSize), bOrder)
	return result, pIpForwardTable


# Gets TCP Connection/UDP Listener Table

_GetTcpTable = WINFUNCTYPE(c_ulong, PMIB_TCPTABLE, c_void_p, c_bool)(('GetTcpTable', windll.iphlpapi))
def GetTcpTable(pdwSize = None, bOrder = True):
	'Gets the TCP Connection Table'
	TcpTable = PMIB_TCPTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetTcpTable(TcpTable, byref(pdwSize), bOrder)
	return result, TcpTable

_GetExtendedTcpTable = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, c_bool, c_ulong, c_int, c_ulong)(('GetExtendedTcpTable', windll.iphlpapi))
def GetExtendedTcpTable(pTcpTable = None, pdwSize = None, bOrder = True, ulAf = 0, TableClass = 0, Reserved = 0):
	if not pTcpTable:
		pTcpTable = c_void_p()
	if not pdwSize:
		pdwSize = c_ulong()
	return _GetExtendedTcpTable(byref(pTcpTable), byref(pdwSize), bOrder, ulAf, TableClass, Reserved)

_GetOwnerModuleFromTcpEntry = WINFUNCTYPE(c_ulong, PMIB_TCPROW_OWNER_MODULE, c_int, c_void_p, c_void_p)(('GetOwnerModuleFromTcpEntry', windll.iphlpapi))
def GetOwnerModuleFromTcpEntry(pTcpEntry = PMIB_TCPROW_OWNER_MODULE(), Class = 0, pBuffer = None, pdwSize = None):
	if not pBuffer:
		pBuffer = c_void_p()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetOwnerModuleFromTcpEntry(pTcpEntry, Class, byref(pBuffer), byref(pdwSize))
	return result, pBuffer

_GetUdpTable = WINFUNCTYPE(c_ulong, PMIB_UDPTABLE, c_void_p, c_bool)(('GetUdpTable', windll.iphlpapi))
def GetUdpTable(pdwSize = None, bOrder = True):
	'Gets the UDP Listener Table'
	UdpTable = PMIB_UDPTABLE()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetUdpTable(UdpTable, byref(pdwSize), bOrder)
	return result, UdpTable

_GetExtendedUdpTable = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, c_bool, c_ulong, c_int, c_ulong)(('GetExtendedUdpTable', windll.iphlpapi))
def GetExtendedUdpTable(pUdpTable = None, pdwSize = None, bOrder = True, ulAf = 0, TableClass = 0, Reserved = 0):
	if not pUdpTable:
		pUdpTable = c_void_p()
	if not pdwSize:
		pdwSize = c_ulong()
	return _GetExtendedUdpTable(byref(pUdpTable), byref(pdwSize), bOrder, ulAf, TableClass, Reserved)

_GetOwnerModuleFromUdpEntry = WINFUNCTYPE(c_ulong, PMIB_UDPROW_OWNER_MODULE, c_int, c_void_p, c_void_p)(('GetOwnerModuleFromUdpEntry', windll.iphlpapi))
def GetOwnerModuleFromUdpEntry(pUdpEntry = PMIB_UDPROW_OWNER_MODULE(), Class = 0, pBuffer = None, pdwSize = None):
	if not pBuffer:
		pBuffer = c_void_p()
	if not pdwSize:
		pdwSize = c_ulong()
	result = _GetOwnerModuleFromUdpEntry(pUdpEntry, Class, byref(pBuffer), byref(pdwSize))
	return result, pBuffer

if NTDDI_VERSION >= NTDDI_LONGHORN:
	_GetTcpTable2 = WINFUNCTYPE(c_ulong, PMIB_TCPTABLE2, c_void_p, c_bool)(('GetTcpTable2', windll.iphlpapi))
	def GetTcpTable2(pdwSize = None, bOrder = True):
		TcpTable = PMIB_TCPTABLE2()
		if not pdwSize:
			pdwSize = c_ulong()
		result = _GetTcpTable2(TcpTable, byref(pdwSize), bOrder)
		return result, TcpTable


# Deprecated APIs, Added for documentation.
if NTDDI_VERSION < NTDDI_LONGHORN:
	_AllocateAndGetTcpExTableFromStack = WINFUNCTYPE(c_ulong, POINTER(c_void_p), c_bool, c_ulong, c_ulong, c_ulong)(('AllocateAndGetTcpExTableFromStack', windll.iphlpapi))
	def AllocateAndGetTcpExTableFromStack(ppTcpTable = None, bOrder = True, hHeap = 0, dwFlags = 0, dwFamily = 0):
		if not ppTcpTable:
			ppTcpTable = pointer(c_void_p())
		return _AllocateAndGetTcpExTableFromStack(ppTcpTable, bOrder, hHeap, dwFlags, dwFamily)
	_AllocateAndGetUdpExTableFromStack = WINFUNCTYPE(c_ulong, POINTER(c_void_p), c_bool, c_ulong, c_ulong, c_ulong)(('AllocateAndGetUdpExTableFromStack', windll.iphlpapi))
	def AllocateAndGetUdpExTableFromStack(ppUdpTable = None, bOrder = True, hHeap = 0, dwFlags = 0, dwFamily = 0):
		if not ppUdpTable:
			ppUdpTable = pointer(c_void_p())
		return _AllocateAndGetUdpExTableFromStack(ppUdpTable, bOrder, hHeap, dwFlags, dwFamily)

# The following definitions require Winsock2.
# Minimum supported client Windows Vista 
# Minimum supported server Windows Server 2008 
if NTDDI_VERSION >= NTDDI_LONGHORN:

	_GetTcp6Table = WINFUNCTYPE(c_ulong, PMIB_TCP6TABLE, c_void_p, c_bool)(('GetTcp6Table', windll.iphlpapi))
	def GetTcp6Table(pdwSize = None, bOrder = True):
		Tcp6Table = PMIB_TCP6TABLE()
		if not pdwSize:
			pdwSize = c_ulong()
		result = _GetTcp6Table(Tcp6Table, byref(pdwSize), bOrder)
		return result, Tcp6Table

	_GetTcp6Table2 = WINFUNCTYPE(c_ulong, PMIB_TCP6TABLE2, c_void_p, c_bool)(('GetTcp6Table2', windll.iphlpapi))
	def GetTcp6Table2(pdwSize = None, bOrder = True):
		Tcp6Table2 = PMIB_TCP6TABLE2()
		if not pdwSize:
			pdwSize = c_ulong()
		result = _GetTcp6Table2(Tcp6Table2, byref(pdwSize), bOrder)
		return result, Tcp6Table2

	GetPerTcpConnectionEStats = WINFUNCTYPE(c_ulong, PMIB_TCPROW, c_int, c_void_p, c_ulong, c_ulong, c_void_p, c_ulong, c_ulong, c_void_p, c_ulong, c_ulong)(('GetPerTcpConnectionEStats', windll.iphlpapi))
	SetPerTcpConnectionEStats = WINFUNCTYPE(c_ulong, PMIB_TCPROW, c_int, c_void_p, c_ulong, c_ulong, c_ulong)(('SetPerTcpConnectionEStats', windll.iphlpapi))

	#if _WS2IPDEF_:
	GetPerTcp6ConnectionEStats = WINFUNCTYPE(c_ulong, PMIB_TCP6ROW, c_int, c_void_p, c_ulong, c_ulong, c_void_p, c_ulong, c_ulong, c_void_p, c_ulong, c_ulong)(('GetPerTcp6ConnectionEStats', windll.iphlpapi))
	SetPerTcp6ConnectionEStats = WINFUNCTYPE(c_ulong, PMIB_TCP6ROW, c_int, c_void_p, c_ulong, c_ulong, c_ulong)(('SetPerTcp6ConnectionEStats', windll.iphlpapi))

	GetOwnerModuleFromTcp6Entry = WINFUNCTYPE(c_ulong, PMIB_TCP6ROW_OWNER_MODULE, c_int, c_void_p, c_void_p)(('GetOwnerModuleFromTcp6Entry', windll.iphlpapi))

	_GetUdp6Table = WINFUNCTYPE(c_ulong, PMIB_UDP6TABLE, c_void_p, c_bool)(('GetUdp6Table', windll.iphlpapi))
	def GetUdp6Table(pdwSize = None, bOrder = True):
		Udp6Table = PMIB_UDP6TABLE()
		if not pdwSize:
			pdwSize = c_ulong()
		result = _GetUdp6Table(Udp6Table, byref(pdwSize), bOrder)
		return result, Udp6Table

	GetOwnerModuleFromUdp6Entry = WINFUNCTYPE(c_ulong, PMIB_UDP6ROW_OWNER_MODULE, c_int, c_void_p, c_void_p)(('GetOwnerModuleFromUdp6Entry', windll.iphlpapi))
	#end if _WS2IPDEF_

	GetOwnerModuleFromPidAndInfo = WINFUNCTYPE(c_ulong, c_ulong, c_void_p, c_int, c_void_p, c_void_p)(('GetOwnerModuleFromPidAndInfo', windll.iphlpapi))


# Gets IP/ICMP/TCP/UDP Statistics

if NTDDI_VERSION >= NTDDI_WIN2K:

	_GetIpStatistics = WINFUNCTYPE(c_ulong, PMIB_IPSTATS)(('GetIpStatistics', windll.iphlpapi))
	def GetIpStatistics():
		'retrieves the IP statistics for the current computer'
		Statistics = MIB_IPSTATS()
		#~ Statistics = cast(cdll.msvcrt.malloc(sizeof(MIB_IPSTATS)), PMIB_IPSTATS)
		result = _GetIpStatistics(Statistics)
		return result, Statistics

	_GetIpStatisticsEx = WINFUNCTYPE(c_ulong, PMIB_IPSTATS, c_ulong)(('GetIpStatisticsEx', windll.iphlpapi))
	def GetIpStatisticsEx(Family = AF_INET):
		'retrieves the IP statistics for the current computer, also supports the Internet Protocol version 6 (IPv6) protocol family'
		Statistics = MIB_IPSTATS()
		result = _GetIpStatisticsEx(Statistics, Family)
		return result, Statistics

if NTDDI_VERSION >= NTDDI_LONGHORN:
	_SetIpStatisticsEx = WINFUNCTYPE(c_ulong, PMIB_IPSTATS, c_ulong)(('SetIpStatisticsEx', windll.iphlpapi))
	def SetIpStatisticsEx(Statistics = MIB_IPSTATS(), Family = AF_INET):
		'set the IP statistics for the current computer, also supports the Internet Protocol version 6 (IPv6) protocol family'
		return _SetIpStatisticsEx(Statistics, Family)

_GetIcmpStatistics = WINFUNCTYPE(c_ulong, PMIB_ICMP)(('GetIcmpStatistics', windll.iphlpapi))
def GetIcmpStatistics():
	'retrieves the Internet Control Message Protocol (ICMP) for IPv4 statistics for the local computer'
	Statistics = MIB_ICMP()
	result = _GetIcmpStatistics(Statistics)
	return result, Statistics

if NTDDI_VERSION >= NTDDI_WINXPSP1:
	_GetIcmpStatisticsEx = WINFUNCTYPE(c_ulong, PMIB_ICMP_EX, c_ulong)(('GetIcmpStatisticsEx', windll.iphlpapi))
	def GetIcmpStatisticsEx(Family = AF_INET):
		'retrieves the Internet Control Message Protocol (ICMP) for IPv4 statistics for the local computer, also supports the version 6 (IPv6) protocol family'
		Statistics = MIB_ICMP_EX()
		result = _GetIcmpStatisticsEx(Statistics, Family)
		return result, Statistics

if NTDDI_VERSION >= NTDDI_WIN2K:

	_GetTcpStatistics = WINFUNCTYPE(c_ulong, PMIB_TCPSTATS)(('GetTcpStatistics', windll.iphlpapi))
	def GetTcpStatistics():
		'retrieves the TCP statistics for IPv4 on the current computer'
		Statistics = MIB_TCPSTATS()
		result = _GetTcpStatistics(Statistics)
		return result, Statistics

	_GetTcpStatisticsEx = WINFUNCTYPE(c_ulong, PMIB_TCPSTATS, c_ulong)(('GetTcpStatisticsEx', windll.iphlpapi))
	def GetTcpStatisticsEx(Family = AF_INET):
		'retrieves the Transmission Control Protocol (TCP) statistics for the current computer, also supports the Internet Protocol version 6 (IPv6) protocol family'
		Statistics = MIB_TCPSTATS()
		result = _GetTcpStatisticsEx(Statistics, Family)
		return result, Statistics

_GetUdpStatistics = WINFUNCTYPE(c_ulong, PMIB_UDPSTATS)(('GetUdpStatistics', windll.iphlpapi))
def GetUdpStatistics():
	'retrieves the User Datagram Protocol (UDP) statistics for IPv4 on the current computer'
	Statistics = MIB_UDPSTATS()
	result = _GetUdpStatistics(Statistics)
	return result, Statistics

_GetUdpStatisticsEx = WINFUNCTYPE(c_ulong, PMIB_UDPSTATS, c_ulong)(('GetUdpStatisticsEx', windll.iphlpapi))
def GetUdpStatisticsEx(Family = AF_INET):
	'retrieves the User Datagram Protocol (UDP) statistics for the current computer, also supports the Internet Protocol version 6 (IPv6) protocol family'
	Statistics = MIB_UDPSTATS()
	result = _GetUdpStatisticsEx(Statistics, Family)
	return result, Statistics

SetIfEntry = WINFUNCTYPE(c_ulong, PMIB_IFROW)(('SetIfEntry', windll.iphlpapi))
SetIfEntry.__doc__ = 'Used to set the ifAdminStatus on an interface.  The only fields of the MIB_IFROW that are relevant are the dwIndex (index of the interface whose status needs to be set) and the dwAdminStatus which can be either MIB_IF_ADMIN_STATUS_UP or MIB_IF_ADMIN_STATUS_DOWN'

# Used to create, modify or delete a route.  In all cases the
# dwForwardIfIndex, dwForwardDest, dwForwardMask, dwForwardNextHop and
# dwForwardPolicy MUST BE SPECIFIED. Currently dwForwardPolicy is unused
# and MUST BE 0.
# For a set, the complete MIB_IPFORWARDROW structure must be specified
CreateIpForwardEntry = WINFUNCTYPE(c_ulong, PMIB_IPFORWARDROW)(('CreateIpForwardEntry', windll.iphlpapi))
SetIpForwardEntry = WINFUNCTYPE(c_ulong, PMIB_IPFORWARDROW)(('SetIpForwardEntry', windll.iphlpapi))
DeleteIpForwardEntry = WINFUNCTYPE(c_ulong, PMIB_IPFORWARDROW)(('DeleteIpForwardEntry', windll.iphlpapi))

if NTDDI_VERSION >= NTDDI_WIN2K:
	SetIpStatistics = WINFUNCTYPE(c_ulong, PMIB_IPSTATS)(('SetIpStatistics', windll.iphlpapi))
	SetIpStatistics.__doc__ = 'Used to set the ipForwarding to ON or OFF (currently only ON->OFF is allowed) and to set the defaultTTL.  If only one of the fields needs to be modified and the other needs to be the same as before the other field needs to be set to MIB_USE_CURRENT_TTL or MIB_USE_CURRENT_FORWARDING as the case may be'

SetIpTTL = WINFUNCTYPE(c_ulong, c_uint)(('SetIpTTL', windll.iphlpapi))
SetIpTTL.__doc__ = 'Used to set the defaultTTL'

# Used to create, modify or delete an ARP entry.  In all cases the dwIndex
# dwAddr field MUST BE SPECIFIED.
# For a set, the complete MIB_IPNETROW structure must be specified
CreateIpNetEntry = WINFUNCTYPE(c_ulong, PMIB_IPNETROW)(('CreateIpNetEntry', windll.iphlpapi))
SetIpNetEntry = WINFUNCTYPE(c_ulong, PMIB_IPNETROW)(('SetIpNetEntry', windll.iphlpapi))
DeleteIpNetEntry = WINFUNCTYPE(c_ulong, PMIB_IPNETROW)(('DeleteIpNetEntry', windll.iphlpapi))
FlushIpNetTable = WINFUNCTYPE(c_ulong, c_ulong)(('FlushIpNetTable', windll.iphlpapi))

# Used to create or delete a Proxy ARP entry. The dwIndex is the index of
# the interface on which to PARP for the dwAddress.  If the interface is
# of a type that doesnt support ARP, e.g. PPP, then the call will fail
CreateProxyArpEntry = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_ulong)(('CreateProxyArpEntry', windll.iphlpapi))
CreateProxyArpEntry.__doc__ = 'params : dwAddress, dwMask, dwIfIndex'
DeleteProxyArpEntry = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_ulong)(('DeleteProxyArpEntry', windll.iphlpapi))
DeleteProxyArpEntry.__doc__ = 'params : dwAddress, dwMask, dwIfIndex'

# Used to set the state of a TCP Connection.
# The only state that it can be set to is MIB_TCP_STATE_DELETE_TCB.
# The complete MIB_TCPROW structure MUST BE SPECIFIED
SetTcpEntry = WINFUNCTYPE(c_ulong, PMIB_TCPROW)(('SetTcpEntry', windll.iphlpapi))
_GetInterfaceInfo = WINFUNCTYPE(c_ulong, PIP_INTERFACE_INFO, c_void_p)(('GetInterfaceInfo', windll.iphlpapi))
def GetInterfaceInfo(pIfTable = IP_INTERFACE_INFO()):
	dwOutBufLen = c_ulong()
	result = _GetInterfaceInfo(pIfTable, byref(dwOutBufLen))
	return result, dwOutBufLen
_GetUniDirectionalAdapterInfo = WINFUNCTYPE(c_ulong, PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS, c_void_p)(('GetUniDirectionalAdapterInfo', windll.iphlpapi))
def GetUniDirectionalAdapterInfo(pIPIfInfo = IP_UNIDIRECTIONAL_ADAPTER_ADDRESS()):
	dwOutBufLen = c_ulong()
	result = _GetUniDirectionalAdapterInfo(pIPIfInfo, byref(dwOutBufLen))
	return result, dwOutBufLen

if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	_NhpAllocateAndGetInterfaceInfoFromStack = WINFUNCTYPE(c_ulong, POINTER(PIP_INTERFACE_NAME_INFO), c_void_p, c_bool, c_ulong, c_ulong)(('NhpAllocateAndGetInterfaceInfoFromStack', windll.iphlpapi))
	def NhpAllocateAndGetInterfaceInfoFromStack(bOrder = True, hHeap = None, dwFlags = 0):
		ppTable = POINTER(IP_INTERFACE_NAME_INFO())
		pdwCount = c_ulong()
		result = _NhpAllocateAndGetInterfaceInfoFromStack(ppTable, byref(pdwCount), bOrder, hHeap, dwFlags)
		return result, pdwCount, ppTable

_GetBestInterface = WINFUNCTYPE(c_ulong, c_ulong, c_void_p)(('GetBestInterface', windll.iphlpapi))
def GetBestInterface(dwDestAddr = 0):
	pdwBestIfIndex = c_ulong()
	result = _GetBestInterface(dwDestAddr, byref(pdwBestIfIndex))
	return result, pdwBestIfIndex

class sockaddr(Structure):
	_fields_ = [('sa_family', c_ushort), ('sa_data', c_char * 14)]
_GetBestInterfaceEx = WINFUNCTYPE(c_ulong, POINTER(sockaddr), c_void_p)(('GetBestInterfaceEx', windll.iphlpapi))
def GetBestInterfaceEx(pDestAddr = sockaddr()):
	pdwBestIfIndex = c_ulong()
	result = _GetBestInterfaceEx(pDestAddr, byref(pdwBestIfIndex))
	return result, pdwBestIfIndex

# Gets the best (longest matching prefix) route for the given destination
# If the source address is also specified (i.e. is not 0x00000000), and
# there are multiple "best" routes to the given destination, the returned
# route will be one that goes out over the interface which has an address
# that matches the source address
_GetBestRoute = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, PMIB_IPFORWARDROW)(('GetBestRoute', windll.iphlpapi))
def GetBestRoute(dwDestAddr = 0, dwSourceAddr = 0):
	pBestRoute = MIB_IPFORWARDROW()
	result = _GetBestRoute(dwDestAddr, dwSourceAddr, pBestRoute)
	return result, pBestRoute

class _STRUCTURE(Structure):
	_fields_ = [('Offset', c_ulong), ('OffsetHigh', c_ulong)]
class _UNION(Union):
	_fields_ = [('s', _STRUCTURE), ('Pointer', c_void_p)]
	_anonymous_ = ('s',)
class OVERLAPPED(Structure):
	_fields_ = [('Internal', POINTER(c_ulong)),
	('InternalHigh', POINTER(c_ulong)),
	('u', _UNION),
	('hEvent', c_ushort)]
	_anonymous_ = ('u',)
LPOVERLAPPED = POINTER(OVERLAPPED)
_NotifyAddrChange = WINFUNCTYPE(c_ulong, LPOVERLAPPED, c_void_p)(('NotifyAddrChange', windll.iphlpapi))
def NotifyAddrChange(overlapped = OVERLAPPED()):
	Handle = c_ulong()
	result = _NotifyAddrChange(byref(Handle), overlapped)
	return result, Handle
_NotifyRouteChange = WINFUNCTYPE(c_ulong, LPOVERLAPPED, c_void_p)(('NotifyRouteChange', windll.iphlpapi))
def NotifyRouteChange(overlapped = OVERLAPPED()):
	Handle = c_ulong()
	result = _NotifyRouteChange(byref(Handle), overlapped)
	return result, Handle
CancelIPChangeNotify = WINFUNCTYPE(c_bool, LPOVERLAPPED)(('CancelIPChangeNotify', windll.iphlpapi))
_GetAdapterIndex = WINFUNCTYPE(c_ulong, c_wchar_p, c_void_p)(('GetAdapterIndex', windll.iphlpapi))
def GetAdapterIndex(AdapterName = '', IfIndex = None):
	if IfIndex is None:
		IfIndex = c_ulong()
	result = _GetAdapterIndex(AdapterName, byref(IfIndex))
	return result, IfIndex.value
_AddIPAddress = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_ulong, c_void_p, c_void_p)(('AddIPAddress', windll.iphlpapi))
def AddIPAddress(Address, IpMask = 0, IfIndex = 0):
	NTEContext = c_ulong()
	NTEInstance = c_ulong()
	result = _AddIPAddress(Address, IpMask, IfIndex, byref(NTEContext), byref(NTEInstance))
	return result, NTEContext, NTEInstance
DeleteIPAddress = WINFUNCTYPE(c_ulong, c_ulong)(('DeleteIPAddress', windll.iphlpapi))

if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	_GetNetworkParams = WINFUNCTYPE(c_ulong, PFIXED_INFO, c_void_p)(('GetNetworkParams', windll.iphlpapi))
	def GetNetworkParams():
		pFixedInfo = FIXED_INFO()
		pOutBufLen = c_ulong()
		result = _GetNetworkParams(pFixedInfo, byref(pOutBufLen))
		if result == 111:#ERROR_BUFFER_OVERFLOW
			from pywingui.windows import GlobalAlloc
			pFixedInfo = cast(GlobalAlloc(0, pOutBufLen), PFIXED_INFO)[0]
			result = _GetNetworkParams(pFixedInfo, byref(pOutBufLen))
		return result, pFixedInfo, pOutBufLen.value

_GetAdaptersInfo = WINFUNCTYPE(c_ulong, PIP_ADAPTER_INFO, c_void_p)(('GetAdaptersInfo', windll.iphlpapi))
def GetAdaptersInfo():
	#~ AdapterInfo = IP_ADAPTER_INFO()
	ulOutBufLen = c_ulong(sizeof(IP_ADAPTER_INFO))
	AdapterInfo = cast(windll.kernel32.HeapAlloc(windll.kernel32.GetProcessHeap(), 0, ulOutBufLen), PIP_ADAPTER_INFO)[0]
	result = _GetAdaptersInfo(AdapterInfo, byref(ulOutBufLen))
	if result == 111:#ERROR_BUFFER_OVERFLOW
		windll.kernel32.HeapFree(windll.kernel32.GetProcessHeap(), 0, pointer(AdapterInfo))
		AdapterInfo = cast(windll.kernel32.HeapAlloc(windll.kernel32.GetProcessHeap(), 0, ulOutBufLen), PIP_ADAPTER_INFO)[0]
		result = _GetAdaptersInfo(AdapterInfo, byref(ulOutBufLen))
	return result, AdapterInfo, ulOutBufLen.value

GetAdapterOrderMap = WINFUNCTYPE(PIP_ADAPTER_ORDER_MAP)(('GetAdapterOrderMap', windll.iphlpapi))

#===============================
# The following functions require Winsock2.

#ULONG WINAPI GetAdaptersAddresses(IN ULONG Family, IN ULONG Flags, IN PVOID Reserved, __out_bcount_opt(*SizePointer) PIP_ADAPTER_ADDRESSES AdapterAddresses, IN OUT PULONG SizePointer);
_GetAdaptersAddresses = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_void_p, PIP_ADAPTER_ADDRESSES, c_void_p)(('GetAdaptersAddresses', windll.iphlpapi))
from iptypes import GAA_FLAG_INCLUDE_PREFIX
def GetAdaptersAddresses(family = GAA_FLAG_INCLUDE_PREFIX, flags = AF_UNSPEC, reserved = None):
	#~ AdapterAddresses = IP_ADAPTER_ADDRESSES()
	WORKING_BUFFER_SIZE = 15000
	AdapterAddresses = cast(windll.kernel32.HeapAlloc(windll.kernel32.GetProcessHeap(), 0, WORKING_BUFFER_SIZE), PIP_ADAPTER_ADDRESSES)[0]
	ulOutBufLen = c_ulong(sizeof(IP_ADAPTER_INFO))
	result = _GetAdaptersAddresses(family, flags, reserved, AdapterAddresses, byref(ulOutBufLen))
	if result == 111:#ERROR_BUFFER_OVERFLOW
		windll.kernel32.HeapFree(windll.kernel32.GetProcessHeap(), 0, pointer(AdapterAddresses))
		AdapterAddresses = cast(windll.kernel32.HeapAlloc(windll.kernel32.GetProcessHeap(), 0, WORKING_BUFFER_SIZE), PIP_ADAPTER_ADDRESSES)[0]
		result = _GetAdaptersAddresses(family, flags, reserved, AdapterAddresses, byref(ulOutBufLen))
	return result, AdapterAddresses, ulOutBufLen.value

if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	#DWORD WINAPI GetPerAdapterInfo(ULONG IfIndex, PIP_PER_ADAPTER_INFO pPerAdapterInfo, PULONG pOutBufLen);
	GetPerAdapterInfo = WINFUNCTYPE(c_ulong, c_ulong, PIP_PER_ADAPTER_INFO, c_void_p)(('GetPerAdapterInfo', windll.iphlpapi))

#DWORD WINAPI IpReleaseAddress(PIP_ADAPTER_INDEX_MAP  AdapterInfo);
IpReleaseAddress = WINFUNCTYPE(c_ulong, PIP_ADAPTER_INDEX_MAP)(('IpReleaseAddress', windll.iphlpapi))

#DWORD WINAPI IpRenewAddress(PIP_ADAPTER_INDEX_MAP  AdapterInfo);
IpRenewAddress = WINFUNCTYPE(c_ulong, PIP_ADAPTER_INDEX_MAP)(('IpRenewAddress', windll.iphlpapi))

#DWORD WINAPI SendARP(IPAddr DestIP, IPAddr SrcIP, PVOID pMacAddr, PULONG  PhyAddrLen);
_SendARP = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_void_p, c_void_p)(('SendARP', windll.iphlpapi))
def SendARP(SrcIP = 0):
	DestIP = 0
	pMacAddr = (c_ulong*2)()#default for src ip
	PhyAddrLen = c_ulong(6)#for 6-byte hardware addresses
	result = _SendARP(DestIP, SrcIP, byref(pMacAddr), byref(PhyAddrLen))
	return result, DestIP, SrcIP, pMacAddr, PhyAddrLen.value


if __name__ == '__main__':
	if NTDDI_VERSION >= NTDDI_WIN2K:
		from pywingui.error import NO_ERROR
		dwRetval, pStats = GetIpStatistics()
		if dwRetval != NO_ERROR:
			print('GetIpStatistics call failed with %d' % dwRetval)
		else:
			print(repr(pStats))
		#~ cdll.msvcrt.free(pStats)
	else:
		print('OS version is not enough for GetIpStatistics function')
