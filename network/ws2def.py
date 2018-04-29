# ws2def.py
# Copyright (c) 2012 Maxim Kolosov

AF_UNSPEC = 0
AF_UNIX = 1
AF_INET = 2
AF_IMPLINK = 3
AF_PUP = 4
AF_CHAOS = 5
AF_NS = 6
AF_IPX = AF_NS
AF_ISO = 7
AF_OSI = AF_ISO
AF_ECMA = 8
AF_DATAKIT = 9
AF_CCITT = 10
AF_SNA = 11
AF_DECnet = 12
AF_DLI = 13
AF_LAT = 14
AF_HYLINK = 15
AF_APPLETALK = 16
AF_NETBIOS = 17
AF_VOICEVIEW = 18
AF_FIREFOX = 19
AF_UNKNOWN1 = 20
AF_BAN = 21
AF_ATM = 22
AF_INET6 = 23
AF_CLUSTER = 24
AF_12844 = 25
AF_IRDA = 26
AF_NETDES = 28
AF_MAX = 29
AF_TCNPROCESS = 29
AF_TCNMESSAGE = 30
AF_ICLFXBM = 31
AF_MAX = 32
AF_BTH = 32
AF_MAX = 33
SOCK_STREAM = 1
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOL_SOCKET = 0xffff
SO_DEBUG = 0x0001
SO_ACCEPTCONN = 0x0002
SO_REUSEADDR = 0x0004
SO_KEEPALIVE = 0x0008
SO_DONTROUTE = 0x0010
SO_BROADCAST = 0x0020
SO_USELOOPBACK = 0x0040
SO_LINGER = 0x0080
SO_OOBINLINE = 0x0100
SO_DONTLINGER = SO_LINGER
SO_EXCLUSIVEADDRUSE = SO_REUSEADDR
SO_SNDBUF = 0x1001
SO_RCVBUF = 0x1002
SO_SNDLOWAT = 0x1003
SO_RCVLOWAT = 0x1004
SO_SNDTIMEO = 0x1005
SO_RCVTIMEO = 0x1006
SO_ERROR = 0x1007
SO_TYPE = 0x1008
SO_BSP_STATE = 0x1009
SO_GROUP_ID = 0x2001
SO_GROUP_PRIORITY = 0x2002
SO_MAX_MSG_SIZE = 0x2003
SO_CONDITIONAL_ACCEPT = 0x3002
SO_PAUSE_ACCEPT = 0x3003
SO_COMPARTMENT_ID = 0x3004
SO_RANDOMIZE_PORT = 0x3005
WSK_SO_BASE = 0x4000
TCP_NODELAY = 0x0001

_SS_MAXSIZE = 128

from ctypes import *
from pywingui.version_microsoft import WINVER as _WIN32_WINNT

_SS_ALIGNSIZE = sizeof(c_int64)

if _WIN32_WINNT >= 0x0600:
	_SS_PAD1SIZE = _SS_ALIGNSIZE - sizeof(c_ushort)
	_SS_PAD2SIZE = _SS_MAXSIZE - (sizeof(c_ushort) + _SS_PAD1SIZE + _SS_ALIGNSIZE)
else:
	_SS_PAD1SIZE = _SS_ALIGNSIZE - sizeof(c_short)
	_SS_PAD2SIZE = _SS_MAXSIZE - (sizeof(c_short) + _SS_PAD1SIZE + _SS_ALIGNSIZE)

IOC_UNIX = 0x00000000
IOC_WS2 = 0x08000000
IOC_PROTOCOL = 0x10000000
IOC_VENDOR = 0x18000000
if _WIN32_WINNT >= 0x0600:
	IOC_WSK = IOC_WS2|0x07000000

IOC_VOID = 0x20000000
IOC_OUT = 0x40000000
IOC_IN = (-2147483648)
IOC_INOUT = (IOC_IN|IOC_OUT)
def _WSAIO(x,y): return (IOC_VOID|(x)|(y))
def _WSAIOR(x,y): return (IOC_OUT|(x)|(y))
def _WSAIOW(x,y): return (IOC_IN|(x)|(y))
def _WSAIORW(x,y): return (IOC_INOUT|(x)|(y))
SIO_ASSOCIATE_HANDLE         = _WSAIOW(IOC_WS2,1)
SIO_ENABLE_CIRCULAR_QUEUEING = _WSAIO(IOC_WS2,2)
SIO_FIND_ROUTE               = _WSAIOR(IOC_WS2,3)
SIO_FLUSH                    = _WSAIO(IOC_WS2,4)
SIO_GET_BROADCAST_ADDRESS    = _WSAIOR(IOC_WS2,5)
SIO_GET_EXTENSION_FUNCTION_POINTER = _WSAIORW(IOC_WS2,6)
SIO_GET_QOS                  = _WSAIORW(IOC_WS2,7)
SIO_GET_GROUP_QOS            = _WSAIORW(IOC_WS2,8)
SIO_MULTIPOINT_LOOPBACK      = _WSAIOW(IOC_WS2,9)
SIO_MULTICAST_SCOPE          = _WSAIOW(IOC_WS2,10)
SIO_SET_QOS                  = _WSAIOW(IOC_WS2,11)
SIO_SET_GROUP_QOS            = _WSAIOW(IOC_WS2,12)
SIO_TRANSLATE_HANDLE         = _WSAIORW(IOC_WS2,13)
SIO_ROUTING_INTERFACE_QUERY  = _WSAIORW(IOC_WS2,20)
SIO_ROUTING_INTERFACE_CHANGE = _WSAIOW(IOC_WS2,21)
SIO_ADDRESS_LIST_QUERY       = _WSAIOR(IOC_WS2,22)
SIO_ADDRESS_LIST_CHANGE      = _WSAIO(IOC_WS2,23)
SIO_QUERY_TARGET_PNP_HANDLE  = _WSAIOR(IOC_WS2,24)
if _WIN32_WINNT >= 0x0501:
	SIO_ADDRESS_LIST_SORT = _WSAIORW(IOC_WS2,25)
if _WIN32_WINNT >= 0x0600:
	SIO_RESERVED_1 = _WSAIOW(IOC_WS2,26)
	SIO_RESERVED_2 = _WSAIOW(IOC_WS2,33)

IPPROTO_IP = 0

IPPROTO = 0
if _WIN32_WINNT >= 0x0501:
	IPPROTO_HOPOPTS = 0# IPv6 Hop-by-Hop options
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
if _WIN32_WINNT >= 0x0501:
	IPPROTO_IPV4 = 4
if _WIN32_WINNT >= 0x0600:
	IPPROTO_ST = 5
IPPROTO_TCP = 6
if _WIN32_WINNT >= 0x0600:
	IPPROTO_CBT = 7
	IPPROTO_EGP = 8
	IPPROTO_IGP = 9
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
if _WIN32_WINNT >= 0x0600:
	IPPROTO_RDP = 27
if _WIN32_WINNT >= 0x0501:
	IPPROTO_IPV6     = 41# IPv6 header
	IPPROTO_ROUTING  = 43# IPv6 Routing header
	IPPROTO_FRAGMENT = 44# IPv6 fragmentation header
	IPPROTO_ESP      = 50# encapsulating security payload
	IPPROTO_AH       = 51# authentication header
	IPPROTO_ICMPV6   = 58# ICMPv6
	IPPROTO_NONE     = 59# IPv6 no next header
	IPPROTO_DSTOPTS  = 60# IPv6 Destination options
IPPROTO_ND = 77
if _WIN32_WINNT >= 0x0501:
	IPPROTO_ICLFXBM = 78
if _WIN32_WINNT >= 0x0600:
	IPPROTO_PIM = 103
	IPPROTO_PGM = 113
	IPPROTO_L2TP = 115
	IPPROTO_SCTP = 132
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPROTO_RESERVED_RAW = 257
IPPROTO_RESERVED_IPSEC = 258
IPPROTO_RESERVED_IPSECOFFLOAD = 259
IPPROTO_RESERVED_MAX = 260

IPPORT_TCPMUX = 1
IPPORT_ECHO = 7
IPPORT_DISCARD = 9
IPPORT_SYSTAT = 11
IPPORT_DAYTIME = 13
IPPORT_NETSTAT = 15
IPPORT_QOTD = 17
IPPORT_MSP = 18
IPPORT_CHARGEN = 19
IPPORT_FTP_DATA = 20
IPPORT_FTP = 21
IPPORT_TELNET = 23
IPPORT_SMTP = 25
IPPORT_TIMESERVER = 37
IPPORT_NAMESERVER = 42
IPPORT_WHOIS = 43
IPPORT_MTP = 57
IPPORT_TFTP = 69
IPPORT_RJE = 77
IPPORT_FINGER = 79
IPPORT_TTYLINK = 87
IPPORT_SUPDUP = 95
IPPORT_POP3 = 110
IPPORT_NTP = 123
IPPORT_EPMAP = 135
IPPORT_NETBIOS_NS = 137
IPPORT_NETBIOS_DGM = 138
IPPORT_NETBIOS_SSN = 139
IPPORT_IMAP = 143
IPPORT_SNMP = 161
IPPORT_SNMP_TRAP = 162
IPPORT_IMAP3 = 220
IPPORT_LDAP = 389
IPPORT_HTTPS = 443
IPPORT_MICROSOFT_DS = 445
IPPORT_EXECSERVER = 512
IPPORT_LOGINSERVER = 513
IPPORT_CMDSERVER = 514
IPPORT_EFSSERVER = 520
IPPORT_BIFFUDP = 512
IPPORT_WHOSERVER = 513
IPPORT_ROUTESERVER = 520
IPPORT_RESERVED = 1024
if _WIN32_WINNT >= 0x0600:
	IPPORT_REGISTERED_MIN = IPPORT_RESERVED
	IPPORT_REGISTERED_MAX = 0xbfff
	IPPORT_DYNAMIC_MIN = 0xc000
	IPPORT_DYNAMIC_MAX = 0xffff

IN_CLASSA_NET = 0xff000000
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 0x00ffffff
IN_CLASSA_MAX = 128

IN_CLASSB_NET = 0xffff0000
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 0x0000ffff
IN_CLASSB_MAX = 65536

IN_CLASSC_NET = 0xffffff00
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 0x000000ff

IN_CLASSD_NET = 0xf0000000
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 0x0fffffff

INADDR_ANY = 0x00000000
INADDR_LOOPBACK = 0x7f000001
INADDR_BROADCAST = 0xffffffff
INADDR_NONE = 0xffffffff

SCOPE_LEVEL = 0
ScopeLevelInterface    = 1
ScopeLevelLink         = 2
ScopeLevelSubnet       = 3
ScopeLevelAdmin        = 4
ScopeLevelSite         = 5
ScopeLevelOrganization = 8
ScopeLevelGlobal       = 14
ScopeLevelCount        = 16

SCOPEID_UNSPECIFIED_INIT = 0
IOCPARM_MASK = 0x7f

MSG_TRUNC = 0x0100
MSG_CTRUNC = 0x0200
MSG_BCAST = 0x0400
MSG_MCAST = 0x0800

class SOCKADDR(Structure):
	'Structure used to store most addresses'
	_fields_ = [('sa_family', c_ushort),# Address family.
	('sa_data', c_char * 14)]# Up to 14 bytes of direct address.
LPSOCKADDR = PSOCKADDR = POINTER(SOCKADDR)

class SOCKET_ADDRESS(Structure):
	_fields_ = [('lpSockaddr', PSOCKADDR),
	('iSockaddrLength', c_int)]
PSOCKET_ADDRESS = POINTER(SOCKET_ADDRESS)

class SOCKET_ADDRESS_LIST(Structure):
	'Address list returned via SIO_ADDRESS_LIST_QUERY'
	_fields_ = [('iAddressCount', c_int),
	('Address', SOCKET_ADDRESS)]
PSOCKET_ADDRESS_LIST = POINTER(SOCKET_ADDRESS_LIST)

class CSADDR_INFO(Structure):
	'CSAddr Information'
	_fields_ = [('LocalAddr', SOCKET_ADDRESS),
	('RemoteAddr', SOCKET_ADDRESS),
	('iSocketType', c_int),
	('iProtocol', c_int)]
PCSADDR_INFO = POINTER(CSADDR_INFO)

class SOCKADDR_STORAGE_LH(Structure):
	_fields_ = [('ss_family', c_ushort),# address family
	('__ss_pad1', c_char * _SS_PAD1SIZE),# 6 byte pad, this is to make implementation specific pad up to alignment field that follows explicit in the data structure
	('__ss_align', c_int64),# Field to force desired structure
	('__ss_pad2', c_char * _SS_PAD2SIZE)]# 112 byte pad to achieve desired size; _SS_MAXSIZE value minus size of ss_family, __ss_pad1, and __ss_align fields is 112
PSOCKADDR_STORAGE_LH = POINTER(SOCKADDR_STORAGE_LH)

class SOCKADDR_STORAGE_XP(Structure):
	_fields_ = [('ss_family', c_short),# address family
	('__ss_pad1', c_char * _SS_PAD1SIZE),# 6 byte pad, this is to make implementation specific pad up to alignment field that follows explicit in the data structure
	('__ss_align', c_int64),# Field to force desired structure
	('__ss_pad2', c_char * _SS_PAD2SIZE)]# 112 byte pad to achieve desired size; _SS_MAXSIZE value minus size of ss_family, __ss_pad1, and __ss_align fields is 112
PSOCKADDR_STORAGE_XP = POINTER(SOCKADDR_STORAGE_XP)

if _WIN32_WINNT >= 0x0600:
	SOCKADDR_STORAGE = SOCKADDR_STORAGE_LH
	LPSOCKADDR_STORAGE = PSOCKADDR_STORAGE = PSOCKADDR_STORAGE_LH
elif _WIN32_WINNT >= 0x0501:
	SOCKADDR_STORAGE = SOCKADDR_STORAGE_XP
	LPSOCKADDR_STORAGE = PSOCKADDR_STORAGE = PSOCKADDR_STORAGE_XP

class _S(Structure):
	_fields_ = [('Zone', c_ulong),# default value 28
	('Level', c_ulong)]# default value 4
class _U(Union):
	_fields_ = [('s', _S), ('Value', c_ulong)]
	_anonymous_ = ('s',)
class SCOPE_ID(Structure):
	_fields_ = [('u', _U)]
	_anonymous_ = ('u',)
PSCOPE_ID = POINTER(SCOPE_ID)

from inaddr import IN_ADDR

class SOCKADDR_IN(Structure):
	_fields_ = []
	if _WIN32_WINNT < 0x0600:
		_fields_.append(('sin_family', c_short))
	else:
		_fields_.append(('sin_family', c_ushort))
	_fields_.append(('sin_port', c_ushort))
	_fields_.append(('sin_addr', IN_ADDR))
	_fields_.append(('sin_zero', c_char * 8))
PSOCKADDR_IN = POINTER(SOCKADDR_IN)

class WSABUF(Structure):
	_fields_ = [('len', c_ulong),# the length of the buffer
	('buf', c_char_p)]# the pointer to the buffer
LPWSABUF = POINTER(WSABUF)

class WSAMSG(Structure):
	_fields_ = [('name', LPSOCKADDR),# Remote address
	('namelen', c_int),# Remote address length
	('lpBuffers', LPWSABUF),# Data buffer array
	('dwBufferCount', c_ulong),# Number of elements in the array
	('Control', WSABUF),# Control buffer
	('dwFlags', c_ulong)]# Flags
LPWSAMSG = PWSAMSG = POINTER(WSAMSG)

class WSACMSGHDR(Structure):
	_fields_ = [('cmsg_len', c_size_t),
	('cmsg_level', c_int),
	('cmsg_type', c_int)]
LPWSACMSGHDR = PWSACMSGHDR = POINTER(WSACMSGHDR)
if _WIN32_WINNT >= 0x0600:
	CMSGHDR = WSACMSGHDR
	PCMSGHDR = PWSACMSGHDR


def FIELD_OFFSET(type_field): return type_field.offset
if _WIN32_WINNT >= 0x0600:
	def SIZEOF_SOCKET_ADDRESS_LIST(AddressCount): return FIELD_OFFSET(SOCKET_ADDRESS_LIST.Address) + AddressCount * sizeof(SOCKET_ADDRESS)

def IN_CLASSA(i): return (i & -2147483648) == 0
def IN_CLASSB(i): return (i & -1073741824) == -2147483648
def IN_CLASSC(i): return (i & -536870912) == -1073741824
def IN_CLASSD(i): return (i & -268435456) == -536870912
def IN_MULTICAST(i): return IN_CLASSD(i)

def _IO(x,y): return (IOC_VOID|((x)<<8)|(y))
def _IOR(x,y,t): return (IOC_OUT|((sizeof(t)&IOCPARM_MASK)<<16)|((x)<<8)|(y))
def _IOW(x,y,t): return (IOC_IN|((sizeof(t)&IOCPARM_MASK)<<16)|((x)<<8)|(y))

def WSA_CMSGHDR_ALIGN(length): return (length + alignment(WSACMSGHDR)-1) & (~(alignment(WSACMSGHDR)-1))
def WSA_CMSGDATA_ALIGN(length): return ((length) + MAX_NATURAL_ALIGNMENT-1) & (~(MAX_NATURAL_ALIGNMENT-1))
if _WIN32_WINNT >= 0x0600:
	CMSGHDR_ALIGN = WSA_CMSGHDR_ALIGN
	CMSGDATA_ALIGN = WSA_CMSGDATA_ALIGN
def WSA_CMSG_FIRSTHDR(msg):
	if msg.Control.len >= sizeof(WSACMSGHDR):
		return msg.Control.buf
	else:
		return None
if _WIN32_WINNT >= 0x0600:
	CMSG_FIRSTHDR = WSA_CMSG_FIRSTHDR
def WSA_CMSG_DATA(cmsg): return cmsg + WSA_CMSGDATA_ALIGN(sizeof(WSACMSGHDR))

def WSA_CMSG_NXTHDR(msg, cmsg):
	if not cmsg:
		return WSA_CMSG_FIRSTHDR(msg)
	else:
		if (cmsg + WSA_CMSGHDR_ALIGN(cmsg.cmsg_len) + sizeof(WSACMSGHDR)) > (msg.Control.buf + msg.Control.len):
			return None
		else:
			return cast(c_void_p(cmsg + WSA_CMSGHDR_ALIGN(cmsg.cmsg_len)), LPWSACMSGHDR)
if _WIN32_WINNT >= 0x0600:
	CMSG_NXTHDR = WSA_CMSG_NXTHDR

def WSA_CMSG_SPACE(length): return WSA_CMSGDATA_ALIGN(sizeof(WSACMSGHDR) + WSA_CMSGHDR_ALIGN(length))
if _WIN32_WINNT >= 0x0600:
	CMSG_SPACE = WSA_CMSG_SPACE
def WSA_CMSG_LEN(length): return WSA_CMSGDATA_ALIGN(sizeof(WSACMSGHDR)) + length
if _WIN32_WINNT >= 0x0600:
	CMSG_LEN = WSA_CMSG_LEN
