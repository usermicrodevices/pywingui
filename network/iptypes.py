# iptypes.py
# Copyright (c) 2012 Maxim Kolosov

MAX_ADAPTER_DESCRIPTION_LENGTH = 128 # arb.
MAX_ADAPTER_NAME_LENGTH        = 256 # arb.
MAX_ADAPTER_ADDRESS_LENGTH     = 8   # arb.
DEFAULT_MINIMUM_ENTITIES       = 32  # arb.
MAX_HOSTNAME_LEN               = 128 # arb.
MAX_DOMAIN_NAME_LEN            = 128 # arb.
MAX_SCOPE_ID_LEN               = 256 # arb.
MAX_DHCPV6_DUID_LENGTH         = 130 # RFC 3315.

# Node Type
BROADCAST_NODETYPE             = 1
PEER_TO_PEER_NODETYPE          = 2
MIXED_NODETYPE                 = 4
HYBRID_NODETYPE                = 8

# Bit values of IP_ADAPTER_UNICAST_ADDRESS Flags field.
IP_ADAPTER_ADDRESS_DNS_ELIGIBLE = 0x01
IP_ADAPTER_ADDRESS_TRANSIENT    = 0x02

# Bit values of IP_ADAPTER_ADDRESSES Flags field.
IP_ADAPTER_DDNS_ENABLED               = 0x00000001
IP_ADAPTER_REGISTER_ADAPTER_SUFFIX    = 0x00000002
IP_ADAPTER_DHCP_ENABLED               = 0x00000004
IP_ADAPTER_RECEIVE_ONLY               = 0x00000008
IP_ADAPTER_NO_MULTICAST               = 0x00000010
IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG = 0x00000020
IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED = 0x00000040
IP_ADAPTER_IPV4_ENABLED               = 0x00000080
IP_ADAPTER_IPV6_ENABLED               = 0x00000100

# Flags used as argument to GetAdaptersAddresses().
# "SKIP" flags are added when the default is to include the information.
# "INCLUDE" flags are added when the default is to skip the information.
GAA_FLAG_SKIP_UNICAST                = 0x0001
GAA_FLAG_SKIP_ANYCAST                = 0x0002
GAA_FLAG_SKIP_MULTICAST              = 0x0004
GAA_FLAG_SKIP_DNS_SERVER             = 0x0008
GAA_FLAG_INCLUDE_PREFIX              = 0x0010
GAA_FLAG_SKIP_FRIENDLY_NAME          = 0x0020
GAA_FLAG_INCLUDE_WINS_INFO           = 0x0040
GAA_FLAG_INCLUDE_GATEWAYS            = 0x0080
GAA_FLAG_INCLUDE_ALL_INTERFACES      = 0x0100
GAA_FLAG_INCLUDE_ALL_COMPARTMENTS    = 0x0200
GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER = 0x0400

from ctypes import *
from ifdef import IF_LUID
from ws2def import SOCKET_ADDRESS
from pywingui.shell import GUID
from pywingui.sdkddkver import NTDDI_VERSION, NTDDI_WIN2K, NTDDI_WIN2KSP1, NTDDI_WINXP, NTDDI_WINXPSP1, NTDDI_LONGHORN

class IP_ADDRESS_STRING(Structure):
	_fields_ = [('String', c_char * 16)]
PIP_ADDRESS_STRING = POINTER(IP_ADDRESS_STRING)
IP_MASK_STRING = IP_ADDRESS_STRING
PIP_MASK_STRING = POINTER(IP_MASK_STRING)

class IP_ADDR_STRING(Structure):
	pass
PIP_ADDR_STRING = POINTER(IP_ADDR_STRING)
IP_ADDR_STRING._fields_ = [('Next', PIP_ADDR_STRING),
	('IpAddress', IP_ADDRESS_STRING),
	('IpMask', IP_MASK_STRING),
	('Context', c_ulong)]

# ADAPTER_INFO - per-adapter information. All IP addresses are stored as strings
class IP_ADAPTER_INFO(Structure):
	pass
PIP_ADAPTER_INFO = POINTER(IP_ADAPTER_INFO)
IP_ADAPTER_INFO._fields_ = [('Next', PIP_ADAPTER_INFO),
	('ComboIndex', c_ulong),
	('AdapterName', c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
	('Description', c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
	('AddressLength', c_uint),
	('Address', c_byte * MAX_ADAPTER_ADDRESS_LENGTH),
	('Index', c_ulong),
	('Type', c_uint),
	('DhcpEnabled', c_uint),
	('CurrentIpAddress', PIP_ADDR_STRING),
	('IpAddressList', IP_ADDR_STRING),
	('GatewayList', IP_ADDR_STRING),
	('DhcpServer', IP_ADDR_STRING),
	('HaveWins', c_bool),
	('PrimaryWinsServer', IP_ADDR_STRING),
	('SecondaryWinsServer', IP_ADDR_STRING),
	('LeaseObtained', c_int64),
	('LeaseExpires', c_int64)]

class _STRUCTURE(Structure):
	_fields_ = [('Length', c_ulong), ('Flags', c_ulong)]
class _UNION(Union):
	_fields_ = [('Alignment', c_ulonglong), ('s', _STRUCTURE)]
	_anonymous_ = ('s',)
class IP_ADAPTER_UNICAST_ADDRESS_LH(Structure): pass
PIP_ADAPTER_UNICAST_ADDRESS_LH = POINTER(IP_ADAPTER_UNICAST_ADDRESS_LH)
IP_ADAPTER_UNICAST_ADDRESS_LH._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_UNICAST_ADDRESS_LH),
('Address', SOCKET_ADDRESS),
('PrefixOrigin', c_int),
('SuffixOrigin', c_int),
('DadState', c_int),
('ValidLifetime', c_ulong),
('PreferredLifetime', c_ulong),
('LeaseLifetime', c_ulong),
('OnLinkPrefixLength', c_ubyte)]
IP_ADAPTER_UNICAST_ADDRESS_LH._anonymous_ = ('u',)

class IP_ADAPTER_UNICAST_ADDRESS_XP(Structure): pass
PIP_ADAPTER_UNICAST_ADDRESS_XP = POINTER(IP_ADAPTER_UNICAST_ADDRESS_XP)
IP_ADAPTER_UNICAST_ADDRESS_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_UNICAST_ADDRESS_XP),
('Address', SOCKET_ADDRESS),
('PrefixOrigin', c_int),
('SuffixOrigin', c_int),
('DadState', c_int),
('ValidLifetime', c_ulong),
('PreferredLifetime', c_ulong),
('LeaseLifetime', c_ulong)]
IP_ADAPTER_UNICAST_ADDRESS_XP._anonymous_ = ('u',)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	IP_ADAPTER_UNICAST_ADDRESS = IP_ADAPTER_UNICAST_ADDRESS_LH
	PIP_ADAPTER_UNICAST_ADDRESS = PIP_ADAPTER_UNICAST_ADDRESS_LH
elif NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_UNICAST_ADDRESS = IP_ADAPTER_UNICAST_ADDRESS_XP
	PIP_ADAPTER_UNICAST_ADDRESS = PIP_ADAPTER_UNICAST_ADDRESS_XP

class IP_ADAPTER_ANYCAST_ADDRESS_XP(Structure): pass
PIP_ADAPTER_ANYCAST_ADDRESS_XP = POINTER(IP_ADAPTER_ANYCAST_ADDRESS_XP)
IP_ADAPTER_ANYCAST_ADDRESS_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_ANYCAST_ADDRESS_XP),
('Address', SOCKET_ADDRESS)]
IP_ADAPTER_ANYCAST_ADDRESS_XP._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_ANYCAST_ADDRESS = IP_ADAPTER_ANYCAST_ADDRESS_XP
	PIP_ADAPTER_ANYCAST_ADDRESS = PIP_ADAPTER_ANYCAST_ADDRESS_XP

class IP_ADAPTER_MULTICAST_ADDRESS_XP(Structure): pass
PIP_ADAPTER_MULTICAST_ADDRESS_XP = POINTER(IP_ADAPTER_MULTICAST_ADDRESS_XP)
IP_ADAPTER_MULTICAST_ADDRESS_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_MULTICAST_ADDRESS_XP),
('Address', SOCKET_ADDRESS)]
IP_ADAPTER_MULTICAST_ADDRESS_XP._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_MULTICAST_ADDRESS = IP_ADAPTER_MULTICAST_ADDRESS_XP
	PIP_ADAPTER_MULTICAST_ADDRESS = PIP_ADAPTER_MULTICAST_ADDRESS_XP

class IP_ADAPTER_DNS_SERVER_ADDRESS_XP(Structure): pass
PIP_ADAPTER_DNS_SERVER_ADDRESS_XP = POINTER(IP_ADAPTER_DNS_SERVER_ADDRESS_XP)
IP_ADAPTER_DNS_SERVER_ADDRESS_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
('Address', SOCKET_ADDRESS)]
IP_ADAPTER_DNS_SERVER_ADDRESS_XP._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_DNS_SERVER_ADDRESS = IP_ADAPTER_DNS_SERVER_ADDRESS_XP
	PIP_ADAPTER_DNS_SERVER_ADDRESS = PIP_ADAPTER_DNS_SERVER_ADDRESS_XP

class IP_ADAPTER_WINS_SERVER_ADDRESS_LH(Structure): pass
PIP_ADAPTER_WINS_SERVER_ADDRESS_LH = POINTER(IP_ADAPTER_WINS_SERVER_ADDRESS_LH)
IP_ADAPTER_WINS_SERVER_ADDRESS_LH._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_WINS_SERVER_ADDRESS_LH),
('Address', SOCKET_ADDRESS)]
IP_ADAPTER_WINS_SERVER_ADDRESS_LH._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_LONGHORN:
	IP_ADAPTER_WINS_SERVER_ADDRESS = IP_ADAPTER_WINS_SERVER_ADDRESS_LH
	PIP_ADAPTER_WINS_SERVER_ADDRESS = PIP_ADAPTER_WINS_SERVER_ADDRESS_LH

class IP_ADAPTER_GATEWAY_ADDRESS_LH(Structure): pass
PIP_ADAPTER_GATEWAY_ADDRESS_LH = POINTER(IP_ADAPTER_GATEWAY_ADDRESS_LH)
IP_ADAPTER_GATEWAY_ADDRESS_LH._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_GATEWAY_ADDRESS_LH),
('Address', SOCKET_ADDRESS)]
IP_ADAPTER_GATEWAY_ADDRESS_LH._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_LONGHORN:
	IP_ADAPTER_GATEWAY_ADDRESS = IP_ADAPTER_GATEWAY_ADDRESS_LH
	PIP_ADAPTER_GATEWAY_ADDRESS = PIP_ADAPTER_GATEWAY_ADDRESS_LH

class IP_ADAPTER_PREFIX_XP(Structure): pass
PIP_ADAPTER_PREFIX_XP = POINTER(IP_ADAPTER_PREFIX_XP)
IP_ADAPTER_PREFIX_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_PREFIX_XP),
('Address', SOCKET_ADDRESS),
('PrefixLength', c_ulong)]
IP_ADAPTER_PREFIX_XP._anonymous_ = ('u',)
if NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_PREFIX = IP_ADAPTER_PREFIX_XP
	PIP_ADAPTER_PREFIX = PIP_ADAPTER_PREFIX_XP

class _STRUCTURE1(Structure):
	_fields_ = [('DdnsEnabled', c_ulong, 1),
	('RegisterAdapterSuffix', c_ulong, 1),
	('Dhcpv4Enabled', c_ulong, 1),
	('ReceiveOnly', c_ulong, 1),
	('NoMulticast', c_ulong, 1),
	('Ipv6OtherStatefulConfig', c_ulong, 1),
	('NetbiosOverTcpipEnabled', c_ulong, 1),
	('Ipv4Enabled', c_ulong, 1),
	('Ipv6Enabled', c_ulong, 1),
	('Ipv6ManagedAddressConfigurationSupported', c_ulong, 1)]
class _UNION1(Union):
	_fields_ = [('Flags', c_ulong), ('s', _STRUCTURE1)]
	_anonymous_ = ('s',)
class IP_ADAPTER_ADDRESSES_LH(Structure): pass
PIP_ADAPTER_ADDRESSES_LH = POINTER(IP_ADAPTER_ADDRESSES_LH)
IP_ADAPTER_ADDRESSES_LH._fields_ = [('u0', _UNION),
('Next', PIP_ADAPTER_ADDRESSES_LH),
('AdapterName', c_char_p),
('FirstUnicastAddress', PIP_ADAPTER_UNICAST_ADDRESS_LH),
('FirstAnycastAddress', PIP_ADAPTER_ANYCAST_ADDRESS_XP),
('FirstMulticastAddress', PIP_ADAPTER_MULTICAST_ADDRESS_XP),
('FirstDnsServerAddress', PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
('DnsSuffix', c_wchar_p),
('Description', c_wchar_p),
('FriendlyName', c_wchar_p),
('PhysicalAddress', c_byte * MAX_ADAPTER_ADDRESS_LENGTH),
('PhysicalAddressLength', c_ulong),
('u1', _UNION1),
('Mtu', c_ulong),
('IfType', c_ulong),
('OperStatus', c_int),# enum IF_OPER_STATUS
('Ipv6IfIndex', c_ulong),
('ZoneIndices', c_ulong * 16),
('FirstPrefix', PIP_ADAPTER_PREFIX_XP),
('TransmitLinkSpeed', c_ulonglong),# ULONG64
('ReceiveLinkSpeed', c_ulonglong),# ULONG64
('FirstWinsServerAddress', PIP_ADAPTER_WINS_SERVER_ADDRESS_LH),
('FirstGatewayAddress', PIP_ADAPTER_GATEWAY_ADDRESS_LH),
('Ipv4Metric', c_ulong),
('Ipv6Metric', c_ulong),
('Luid', IF_LUID),
('Dhcpv4Server', SOCKET_ADDRESS),
('CompartmentId', c_uint),
('NetworkGuid', GUID),
('ConnectionType', c_int),# enum NET_IF_CONNECTION_TYPE
('TunnelType', c_int),# enum TUNNEL_TYPE
('Dhcpv6Server', SOCKET_ADDRESS),
('Dhcpv6ClientDuid', c_byte * MAX_DHCPV6_DUID_LENGTH),
('Dhcpv6ClientDuidLength', c_ulong),
('Dhcpv6Iaid', c_ulong)]
IP_ADAPTER_ADDRESSES_LH._anonymous_ = ('u0', 'u1')

class IP_ADAPTER_ADDRESSES_XP(Structure): pass
PIP_ADAPTER_ADDRESSES_XP = POINTER(IP_ADAPTER_ADDRESSES_XP)
IP_ADAPTER_ADDRESSES_XP._fields_ = [('u', _UNION),
('Next', PIP_ADAPTER_ADDRESSES_XP),
('AdapterName', c_char_p),
('FirstUnicastAddress', PIP_ADAPTER_UNICAST_ADDRESS_XP),
('FirstAnycastAddress', PIP_ADAPTER_ANYCAST_ADDRESS_XP),
('FirstMulticastAddress', PIP_ADAPTER_MULTICAST_ADDRESS_XP),
('FirstDnsServerAddress', PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
('DnsSuffix', c_wchar_p),
('Description', c_wchar_p),
('FriendlyName', c_wchar_p),
('PhysicalAddress', c_byte * MAX_ADAPTER_ADDRESS_LENGTH),
('PhysicalAddressLength', c_ulong),
('Flags', c_ulong),
('Mtu', c_ulong),
('IfType', c_ulong),
('OperStatus', c_int),# enum IF_OPER_STATUS
('Ipv6IfIndex', c_ulong),
('ZoneIndices', c_ulong * 16),
('FirstPrefix', PIP_ADAPTER_PREFIX_XP)]
IP_ADAPTER_ADDRESSES_XP._anonymous_ = ('u',)

if NTDDI_VERSION >= NTDDI_LONGHORN:
	IP_ADAPTER_ADDRESSES = IP_ADAPTER_ADDRESSES_LH
	PIP_ADAPTER_ADDRESSES = PIP_ADAPTER_ADDRESSES_LH
elif NTDDI_VERSION >= NTDDI_WINXP:
	IP_ADAPTER_ADDRESSES = IP_ADAPTER_ADDRESSES_XP
	PIP_ADAPTER_ADDRESSES = PIP_ADAPTER_ADDRESSES_XP
else:# For platforms other platforms that are including the file but not using the types.
	IP_ADAPTER_ADDRESSES = IP_ADAPTER_ADDRESSES_XP
	PIP_ADAPTER_ADDRESSES = PIP_ADAPTER_ADDRESSES_XP

class IP_PER_ADAPTER_INFO_W2KSP1(Structure):
	_fields_ = [('AutoconfigEnabled', c_uint),
	('AutoconfigActive', c_uint),
	('CurrentDnsServer', PIP_ADDR_STRING),
	('DnsServerList', IP_ADDR_STRING)]
PIP_PER_ADAPTER_INFO_W2KSP1 = POINTER(IP_PER_ADAPTER_INFO_W2KSP1)
if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	IP_PER_ADAPTER_INFO = IP_PER_ADAPTER_INFO_W2KSP1
	PIP_PER_ADAPTER_INFO = PIP_PER_ADAPTER_INFO_W2KSP1

class FIXED_INFO_W2KSP1(Structure):
	_fields_ = [('HostName', c_char * (MAX_HOSTNAME_LEN + 4)),
	('DomainName', c_char * (MAX_DOMAIN_NAME_LEN + 4)),
	('CurrentDnsServer', PIP_ADDR_STRING),
	('DnsServerList', IP_ADDR_STRING),
	('NodeType', c_int),
	('ScopeId', c_char * (MAX_SCOPE_ID_LEN + 4)),
	('EnableRouting', c_uint),
	('EnableProxy', c_uint),
	('EnableDns', c_uint)]
PFIXED_INFO_W2KSP1 = POINTER(FIXED_INFO_W2KSP1)
if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	FIXED_INFO = FIXED_INFO_W2KSP1
	PFIXED_INFO = PFIXED_INFO_W2KSP1

class IP_INTERFACE_NAME_INFO_W2KSP1(Structure):
	_fields_ = [('Index', c_ulong),# Interface Index
	('MediaType', c_ulong),# Interface Types - see ipifcons.h
	('ConnectionType', c_ubyte),
	('AccessType', c_ubyte),
	('DeviceGuid', GUID),# Device GUID is the guid of the device that IP exposes
	('InterfaceGuid', GUID)]# Interface GUID, if not GUID_NULL is the GUID for the interface mapped to the device.
PIP_INTERFACE_NAME_INFO_W2KSP1 = POINTER(IP_INTERFACE_NAME_INFO_W2KSP1)

if NTDDI_VERSION >= NTDDI_WIN2KSP1:
	IP_INTERFACE_NAME_INFO = IP_INTERFACE_NAME_INFO_W2KSP1
	PIP_INTERFACE_NAME_INFO = PIP_INTERFACE_NAME_INFO_W2KSP1
