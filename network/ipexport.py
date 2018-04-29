# ipexport.py
# Copyright (c) 2012 Maxim Kolosov

MAX_ADAPTER_NAME = 128
IP_STATUS_BASE = 11000
IP_SUCCESS = 0
IP_BUF_TOO_SMALL = (IP_STATUS_BASE + 1)
IP_DEST_NET_UNREACHABLE = (IP_STATUS_BASE + 2)
IP_DEST_HOST_UNREACHABLE = (IP_STATUS_BASE + 3)
IP_DEST_PROT_UNREACHABLE = (IP_STATUS_BASE + 4)
IP_DEST_PORT_UNREACHABLE = (IP_STATUS_BASE + 5)
IP_NO_RESOURCES = (IP_STATUS_BASE + 6)
IP_BAD_OPTION = (IP_STATUS_BASE + 7)
IP_HW_ERROR = (IP_STATUS_BASE + 8)
IP_PACKET_TOO_BIG = (IP_STATUS_BASE + 9)
IP_REQ_TIMED_OUT = (IP_STATUS_BASE + 10)
IP_BAD_REQ = (IP_STATUS_BASE + 11)
IP_BAD_ROUTE = (IP_STATUS_BASE + 12)
IP_TTL_EXPIRED_TRANSIT = (IP_STATUS_BASE + 13)
IP_TTL_EXPIRED_REASSEM = (IP_STATUS_BASE + 14)
IP_PARAM_PROBLEM = (IP_STATUS_BASE + 15)
IP_SOURCE_QUENCH = (IP_STATUS_BASE + 16)
IP_OPTION_TOO_BIG = (IP_STATUS_BASE + 17)
IP_BAD_DESTINATION = (IP_STATUS_BASE + 18)
IP_DEST_NO_ROUTE = (IP_STATUS_BASE + 2)
IP_DEST_ADDR_UNREACHABLE = (IP_STATUS_BASE + 3)
IP_DEST_PROHIBITED = (IP_STATUS_BASE + 4)
IP_DEST_PORT_UNREACHABLE = (IP_STATUS_BASE + 5)
IP_HOP_LIMIT_EXCEEDED = (IP_STATUS_BASE + 13)
IP_REASSEMBLY_TIME_EXCEEDED = (IP_STATUS_BASE + 14)
IP_PARAMETER_PROBLEM = (IP_STATUS_BASE + 15)
IP_DEST_UNREACHABLE = (IP_STATUS_BASE + 40)
IP_TIME_EXCEEDED = (IP_STATUS_BASE + 41)
IP_BAD_HEADER = (IP_STATUS_BASE + 42)
IP_UNRECOGNIZED_NEXT_HEADER = (IP_STATUS_BASE + 43)
IP_ICMP_ERROR = (IP_STATUS_BASE + 44)
IP_DEST_SCOPE_MISMATCH = (IP_STATUS_BASE + 45)
IP_ADDR_DELETED = (IP_STATUS_BASE + 19)
IP_SPEC_MTU_CHANGE = (IP_STATUS_BASE + 20)
IP_MTU_CHANGE = (IP_STATUS_BASE + 21)
IP_UNLOAD = (IP_STATUS_BASE + 22)
IP_ADDR_ADDED = (IP_STATUS_BASE + 23)
IP_MEDIA_CONNECT = (IP_STATUS_BASE + 24)
IP_MEDIA_DISCONNECT = (IP_STATUS_BASE + 25)
IP_BIND_ADAPTER = (IP_STATUS_BASE + 26)
IP_UNBIND_ADAPTER = (IP_STATUS_BASE + 27)
IP_DEVICE_DOES_NOT_EXIST = (IP_STATUS_BASE + 28)
IP_DUPLICATE_ADDRESS = (IP_STATUS_BASE + 29)
IP_INTERFACE_METRIC_CHANGE = (IP_STATUS_BASE + 30)
IP_RECONFIG_SECFLTR = (IP_STATUS_BASE + 31)
IP_NEGOTIATING_IPSEC = (IP_STATUS_BASE + 32)
IP_INTERFACE_WOL_CAPABILITY_CHANGE = (IP_STATUS_BASE + 33)
IP_DUPLICATE_IPADD = (IP_STATUS_BASE + 34)
IP_GENERAL_FAILURE = (IP_STATUS_BASE + 50)
MAX_IP_STATUS = IP_GENERAL_FAILURE
IP_PENDING = (IP_STATUS_BASE + 255)
IP_FLAG_REVERSE = 0x1
IP_FLAG_DF = 0x2
IP_OPT_EOL = 0
IP_OPT_NOP = 1
IP_OPT_SECURITY = 0x82
IP_OPT_LSRR = 0x83
IP_OPT_SSRR = 0x89
IP_OPT_RR = 0x7
IP_OPT_TS = 0x44
IP_OPT_SID = 0x88
IP_OPT_ROUTER_ALERT = 0x94
MAX_OPT_SIZE = 40
IOCTL_IP_RTCHANGE_NOTIFY_REQUEST = 101
IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST = 102
IOCTL_ARP_SEND_REQUEST = 103
IOCTL_IP_INTERFACE_INFO = 104
IOCTL_IP_GET_BEST_INTERFACE = 105
IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS = 106

POINTER_32 = 4

from ctypes import *

#~ from in6addr import IN6_ADDR
from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WINXP, NTDDI_WINXPSP1, NTDDI_LONGHORN

# The ip_option_information structure describes the options to be
# included in the header of an IP packet. The TTL, TOS, and Flags
# values are carried in specific fields in the header. The OptionsData
# bytes are carried in the options area following the standard IP header.
# With the exception of source route options, this data must be in the
# format to be transmitted on the wire as specified in RFC 791. A source
# route option should contain the full route - first hop thru final
# destination - in the route data. The first hop will be pulled out of the
# data and the option will be reformatted accordingly. Otherwise, the route
# option should be formatted as specified in RFC 791.
class IP_OPTION_INFORMATION(Structure):
	_fields_ = [('Ttl', c_ubyte),# Time To Live
	('Tos', c_ubyte),# Type Of Service
	('Flags', c_ubyte),# IP header flags
	('OptionsSize', c_ubyte),# Size in bytes of options data
	('OptionsData', POINTER(c_ubyte))]# Pointer to options data
PIP_OPTION_INFORMATION = POINTER(IP_OPTION_INFORMATION)
if '_WIN64' in globals():
	class IP_OPTION_INFORMATION32(Structure):
		_fields_ = [('Ttl', c_ubyte),
		('Tos', c_ubyte),
		('Flags', c_ubyte),
		('OptionsSize', c_ubyte),
		('OptionsData', POINTER(c_ubyte * POINTER_32))]
	PIP_OPTION_INFORMATION32 = POINTER(IP_OPTION_INFORMATION32)

class ICMP_ECHO_REPLY(Structure):
	'The icmp_echo_reply structure describes the data returned in response to an echo request.'
	_fields_ = [('Address', c_ulong),# Replying address
	('Status', c_ulong),# Reply IP_STATUS
	('RoundTripTime', c_ulong),# RTT in milliseconds
	('DataSize', c_ushort),# Reply data size in bytes
	('Reserved', c_ushort),# Reserved for system use
	('Data', c_void_p),# Pointer to the reply data
	('Options', IP_OPTION_INFORMATION)]# Reply options
PICMP_ECHO_REPLY = POINTER(ICMP_ECHO_REPLY)
if '_WIN64' in globals():
	class ICMP_ECHO_REPLY32(Structure):
		_fields_ = [('Address', c_ulong),
		('Status', c_ulong),
		('RoundTripTime', c_ulong),
		('DataSize', c_ushort),
		('Reserved', c_ushort),
		('Data', POINTER(c_void * POINTER_32)),
		('Options', IP_OPTION_INFORMATION32)]
	PICMP_ECHO_REPLY32 = POINTER(ICMP_ECHO_REPLY32)

class IPV6_ADDRESS_EX_LH(Structure):
	_fields_ = [('sin6_port', c_ushort),
	('sin6_flowinfo', c_ulong),
	('sin6_addr', c_ushort * 8),
	('sin6_scope_id', c_ulong)]
PIPV6_ADDRESS_EX_LH = POINTER(IPV6_ADDRESS_EX_LH)
if NTDDI_VERSION >= NTDDI_LONGHORN:
	IPV6_ADDRESS_EX = IPV6_ADDRESS_EX_LH
	PIPV6_ADDRESS_EX = PIPV6_ADDRESS_EX_LH

class ICMPV6_ECHO_REPLY_LH(Structure):
	_fields_ = [('Address', IPV6_ADDRESS_EX_LH),# Replying address.
	('Status', c_ulong),# Reply IP_STATUS.
	('RoundTripTime', c_uint)]# RTT in milliseconds.
# Reply data follows this structure in memory.
PICMPV6_ECHO_REPLY_LH = POINTER(ICMPV6_ECHO_REPLY_LH)
if NTDDI_VERSION >= NTDDI_LONGHORN:
	ICMPV6_ECHO_REPLY = ICMPV6_ECHO_REPLY_LH
	PICMPV6_ECHO_REPLY = PICMPV6_ECHO_REPLY_LH

class ARP_SEND_REPLY(Structure):
	_fields_ = [('DestAddress', c_ulong), ('SrcAddress', c_ulong)]
PARP_SEND_REPLY = POINTER(ARP_SEND_REPLY)

class TCP_RESERVE_PORT_RANGE(Structure):
	_fields_ = [('UpperRange', c_ushort), ('LowerRange', c_ushort)]
PTCP_RESERVE_PORT_RANGE = POINTER(TCP_RESERVE_PORT_RANGE)

class IP_ADAPTER_INDEX_MAP(Structure):
	_fields_ = [('Index', c_ulong), ('Name', c_wchar * MAX_ADAPTER_NAME)]
PIP_ADAPTER_INDEX_MAP = POINTER(IP_ADAPTER_INDEX_MAP)

class IP_INTERFACE_INFO(Structure):
	_fields_ = [('NumAdapters', c_long), ('Adapter', IP_ADAPTER_INDEX_MAP)]
PIP_INTERFACE_INFO = POINTER(IP_INTERFACE_INFO)

class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(Structure):
	_fields_ = [('NumAdapters', c_ulong), ('Address', c_ulong)]
PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS = POINTER(IP_UNIDIRECTIONAL_ADAPTER_ADDRESS)

class IP_ADAPTER_ORDER_MAP(Structure):
	_fields_ = [('NumAdapters', c_ulong), ('AdapterOrder', c_ulong)]
PIP_ADAPTER_ORDER_MAP = POINTER(IP_ADAPTER_ORDER_MAP)

class IP_MCAST_COUNTER_INFO(Structure):
	_fields_ = [('InMcastOctets', c_ulonglong),
	('OutMcastOctets', c_ulonglong),
	('InMcastPkts', c_ulonglong),
	('OutMcastPkts', c_ulonglong)]
PIP_MCAST_COUNTER_INFO = POINTER(IP_MCAST_COUNTER_INFO)
