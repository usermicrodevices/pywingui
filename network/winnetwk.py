# winnetwk.py
# Copyright (c) 2012 Maxim Kolosov


from ctypes import *
from pywingui.error import *
from pywingui.version_microsoft import WINVER, UNICODE
from pywingui.sdkddkver import _WIN32_WINNT, _WIN32_WINNT_LONGHORN

# Network types
WNNC_NET_MSNET = 0x00010000
WNNC_NET_LANMAN = 0x00020000
WNNC_NET_NETWARE = 0x00030000
WNNC_NET_VINES = 0x00040000
WNNC_NET_10NET = 0x00050000
WNNC_NET_LOCUS = 0x00060000
WNNC_NET_SUN_PC_NFS = 0x00070000
WNNC_NET_LANSTEP = 0x00080000
WNNC_NET_9TILES = 0x00090000
WNNC_NET_LANTASTIC = 0x000A0000
WNNC_NET_AS400 = 0x000B0000
WNNC_NET_FTP_NFS = 0x000C0000
WNNC_NET_PATHWORKS = 0x000D0000
WNNC_NET_LIFENET = 0x000E0000
WNNC_NET_POWERLAN = 0x000F0000
WNNC_NET_BWNFS = 0x00100000
WNNC_NET_COGENT = 0x00110000
WNNC_NET_FARALLON = 0x00120000
WNNC_NET_APPLETALK = 0x00130000
WNNC_NET_INTERGRAPH = 0x00140000
WNNC_NET_SYMFONET = 0x00150000
WNNC_NET_CLEARCASE = 0x00160000
WNNC_NET_FRONTIER = 0x00170000
WNNC_NET_BMC = 0x00180000
WNNC_NET_DCE = 0x00190000
WNNC_NET_AVID = 0x001A0000
WNNC_NET_DOCUSPACE = 0x001B0000
WNNC_NET_MANGOSOFT = 0x001C0000
WNNC_NET_SERNET = 0x001D0000
WNNC_NET_RIVERFRONT1 = 0X001E0000
WNNC_NET_RIVERFRONT2 = 0x001F0000
WNNC_NET_DECORB = 0x00200000
WNNC_NET_PROTSTOR = 0x00210000
WNNC_NET_FJ_REDIR = 0x00220000
WNNC_NET_DISTINCT = 0x00230000
WNNC_NET_TWINS = 0x00240000
WNNC_NET_RDR2SAMPLE = 0x00250000
WNNC_NET_CSC = 0x00260000
WNNC_NET_3IN1 = 0x00270000
WNNC_NET_EXTENDNET = 0x00290000
WNNC_NET_STAC = 0x002A0000
WNNC_NET_FOXBAT = 0x002B0000
WNNC_NET_YAHOO = 0x002C0000
WNNC_NET_EXIFS = 0x002D0000
WNNC_NET_DAV = 0x002E0000
WNNC_NET_KNOWARE = 0x002F0000
WNNC_NET_OBJECT_DIRE = 0x00300000
WNNC_NET_MASFAX = 0x00310000
WNNC_NET_HOB_NFS = 0x00320000
WNNC_NET_SHIVA = 0x00330000
WNNC_NET_IBMAL = 0x00340000
WNNC_NET_LOCK = 0x00350000
WNNC_NET_TERMSRV = 0x00360000
WNNC_NET_SRT = 0x00370000
WNNC_NET_QUINCY = 0x00380000
WNNC_NET_OPENAFS = 0x00390000
WNNC_NET_AVID1 = 0X003A0000
WNNC_NET_DFS = 0x003B0000
WNNC_NET_KWNP = 0x003C0000
WNNC_NET_ZENWORKS = 0x003D0000
WNNC_NET_DRIVEONWEB = 0x003E0000
WNNC_NET_VMWARE = 0x003F0000
WNNC_NET_RSFX = 0x00400000
WNNC_NET_MFILES = 0x00410000
WNNC_NET_MS_NFS = 0x00420000
WNNC_NET_GOOGLE = 0x00430000
WNNC_CRED_MANAGER = 0xFFFF0000


#  Network Resources.

RESOURCE_CONNECTED = 0x00000001
RESOURCE_GLOBALNET = 0x00000002
RESOURCE_REMEMBERED = 0x00000003
if WINVER >= 0x0400:
	RESOURCE_RECENT = 0x00000004
	RESOURCE_CONTEXT = 0x00000005

RESOURCETYPE_ANY = 0x00000000
RESOURCETYPE_DISK = 0x00000001
RESOURCETYPE_PRINT = 0x00000002
if WINVER >= 0x0400:
	RESOURCETYPE_RESERVED = 0x00000008
RESOURCETYPE_UNKNOWN = 0xFFFFFFFF

RESOURCEUSAGE_CONNECTABLE = 0x00000001
RESOURCEUSAGE_CONTAINER = 0x00000002
if WINVER >= 0x0400:
	RESOURCEUSAGE_NOLOCALDEVICE = 0x00000004
	RESOURCEUSAGE_SIBLING = 0x00000008
	RESOURCEUSAGE_ATTACHED = 0x00000010
	RESOURCEUSAGE_ALL = RESOURCEUSAGE_CONNECTABLE | RESOURCEUSAGE_CONTAINER | RESOURCEUSAGE_ATTACHED
RESOURCEUSAGE_RESERVED = 0x80000000

RESOURCEDISPLAYTYPE_GENERIC = 0x00000000
RESOURCEDISPLAYTYPE_DOMAIN = 0x00000001
RESOURCEDISPLAYTYPE_SERVER = 0x00000002
RESOURCEDISPLAYTYPE_SHARE = 0x00000003
RESOURCEDISPLAYTYPE_FILE = 0x00000004
RESOURCEDISPLAYTYPE_GROUP = 0x00000005
if WINVER >= 0x0400:
	RESOURCEDISPLAYTYPE_NETWORK = 0x00000006
	RESOURCEDISPLAYTYPE_ROOT = 0x00000007
	RESOURCEDISPLAYTYPE_SHAREADMIN = 0x00000008
	RESOURCEDISPLAYTYPE_DIRECTORY = 0x00000009
RESOURCEDISPLAYTYPE_TREE = 0x0000000A
if WINVER >= 0x0400:
	RESOURCEDISPLAYTYPE_NDSCONTAINER = 0x0000000B

class NETRESOURCE(Structure):
	_fields_ = [('dwScope', c_ulong),
	('dwType', c_ulong),
	('dwDisplayType', c_ulong),
	('dwUsage', c_ulong)]
	if UNICODE:
		_fields_ += [('lpLocalName', c_wchar_p),
		('lpRemoteName', c_wchar_p),
		('lpComment', c_wchar_p),
		('lpProvider', c_wchar_p),]
	else:
		_fields_ += [('lpLocalName', c_char_p),
		('lpRemoteName', c_char_p),
		('lpComment', c_char_p),
		('lpProvider', c_char_p),]
LPNETRESOURCE = POINTER(NETRESOURCE)


#  Network Connections.

NETPROPERTY_PERSISTENT = 1

CONNECT_UPDATE_PROFILE = 0x00000001
CONNECT_UPDATE_RECENT = 0x00000002
CONNECT_TEMPORARY = 0x00000004
CONNECT_INTERACTIVE = 0x00000008
CONNECT_PROMPT = 0x00000010
CONNECT_NEED_DRIVE = 0x00000020
if WINVER >= 0x0400:
	CONNECT_REFCOUNT = 0x00000040
	CONNECT_REDIRECT = 0x00000080
	CONNECT_LOCALDRIVE = 0x00000100
	CONNECT_CURRENT_MEDIA = 0x00000200
	CONNECT_DEFERRED = 0x00000400
	CONNECT_RESERVED = 0xFF000000
elif WINVER >= 0x0500:
	CONNECT_COMMANDLINE = 0x00000800
	CONNECT_CMD_SAVECRED = 0x00001000
elif WINVER >= 0x0600:
	CONNECT_CRED_RESET = 0x00002000

if UNICODE:
	_WNetAddConnection = WINFUNCTYPE(c_ulong, c_wchar_p, c_wchar_p, c_wchar_p)(('WNetAddConnectionW', windll.mpr))
	_WNetAddConnection2 = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_wchar_p, c_wchar_p, c_ulong)(('WNetAddConnection2W', windll.mpr))
	_WNetAddConnection3 = WINFUNCTYPE(c_ulong, c_void_p, LPNETRESOURCE, c_wchar_p, c_wchar_p, c_ulong)(('WNetAddConnection3W', windll.mpr))
	_WNetCancelConnection = WINFUNCTYPE(c_ulong, c_wchar_p, c_bool)(('WNetCancelConnectionW', windll.mpr))
	_WNetCancelConnection2 = WINFUNCTYPE(c_ulong, c_wchar_p, c_ulong, c_bool)(('WNetCancelConnection2W', windll.mpr))
	_WNetGetConnection = WINFUNCTYPE(c_ulong, c_wchar_p, c_void_p, c_void_p)(('WNetGetConnectionW', windll.mpr))
	if WINVER >= 0x0400:
		_WNetUseConnection = WINFUNCTYPE(c_ulong, c_void_p, LPNETRESOURCE, c_wchar_p, c_wchar_p, c_ulong, c_void_p, c_void_p, c_void_p)(('WNetUseConnectionW', windll.mpr))
else:
	_WNetAddConnection = WINFUNCTYPE(c_ulong, c_char_p, c_char_p, c_char_p)(('WNetAddConnectionA', windll.mpr))
	_WNetAddConnection2 = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_char_p, c_char_p, c_ulong)(('WNetAddConnection2A', windll.mpr))
	_WNetAddConnection3 = WINFUNCTYPE(c_ulong, c_void_p, LPNETRESOURCE, c_char_p, c_char_p, c_ulong)(('WNetAddConnection3A', windll.mpr))
	_WNetCancelConnection = WINFUNCTYPE(c_ulong, c_char_p, c_bool)(('WNetCancelConnectionA', windll.mpr))
	_WNetCancelConnection2 = WINFUNCTYPE(c_ulong, c_char_p, c_ulong, c_bool)(('WNetCancelConnection2A', windll.mpr))
	_WNetGetConnection = WINFUNCTYPE(c_ulong, c_char_p, c_void_p, c_void_p)(('WNetGetConnectionA', windll.mpr))
	if WINVER >= 0x0400:
		_WNetUseConnection = WINFUNCTYPE(c_ulong, c_void_p, LPNETRESOURCE, c_char_p, c_char_p, c_ulong, c_void_p, c_void_p, c_void_p)(('WNetUseConnectionA', windll.mpr))

def WNetAddConnection(lpRemoteName, lpPassword = None, lpLocalName = None):
	return _WNetAddConnection(lpRemoteName, lpPassword, lpLocalName)

def WNetAddConnection2(lpNetResource, lpPassword = None, lpUserName = None, dwFlags = 0):
	return _WNetAddConnection2(lpNetResource, lpPassword, lpUserName, dwFlags)

def WNetAddConnection3(hwndOwner, lpNetResource, lpPassword = None, lpUserName = None, dwFlags = 0):
	return _WNetAddConnection3(hwndOwner, lpNetResource, lpPassword, lpUserName, dwFlags)

def WNetCancelConnection(lpName, fForce = True):
	return _WNetCancelConnection(lpName, fForce)

def WNetCancelConnection2(lpName, dwFlags = 0, fForce = True):
	return _WNetCancelConnection2(lpName, dwFlags, fForce)

def WNetGetConnection(lpLocalName, lpnLength = c_ulong()):
	lpRemoteName = c_wchar_p()
	if not UNICODE:
		lpRemoteName = c_char_p()
	result = _WNetGetConnection(lpLocalName, byref(lpRemoteName), byref(lpnLength))
	return result, lpRemoteName.value, lpnLength.value

if _WIN32_WINNT >= _WIN32_WINNT_LONGHORN:
	WNetRestoreSingleConnection = WNetRestoreSingleConnectionW = WINFUNCTYPE(c_ulong, c_void_p, c_wchar_p, c_bool)(('WNetRestoreSingleConnectionW', windll.mpr))
else:
	WNetRestoreConnection = WNetRestoreConnectionW = WINFUNCTYPE(c_ulong, c_void_p, c_wchar_p)(('WNetRestoreConnectionW', windll.mpr))

if WINVER >= 0x0400:
	def WNetUseConnection(hwndOwner = None, lpNetResource = NETRESOURCE(), lpPassword = None, lpUserId = None, dwFlags = 0, lpBufferSize = c_ulong()):
		'Makes a connection to a network resource. The function can redirect a local device to a network resource. The main difference from WNetAddConnection3 is that WNetUseConnection can automatically select an unused local device to redirect to the network resource.'
		lpAccessName = c_wchar_p()
		if not UNICODE:
			lpAccessName = c_char_p()
		lpResult = c_ulong()
		result = _WNetUseConnection(hwndOwner, lpNetResource, lpPassword, lpUserId, dwFlags, byref(lpAccessName), byref(lpBufferSize), byref(lpResult))
		return result, lpAccessName.value, lpBufferSize.value, lpResult.value


#  Network Connection Dialogs.

WNetConnectionDialog = WINFUNCTYPE(c_ulong, c_void_p, c_ulong)(('WNetConnectionDialog', windll.mpr))
WNetDisconnectDialog = WINFUNCTYPE(c_ulong, c_void_p, c_ulong)(('WNetDisconnectDialog', windll.mpr))

class CONNECTDLGSTRUCT(Structure):
	_fields_ = [('cbStructure', c_ulong),#size of this structure in bytes
	('hwndOwner', c_void_p),#owner window for the dialog
	('lpConnRes', LPNETRESOURCE),#Requested Resource info
	('dwFlags', c_ulong),#flags (see below)
	('dwDevNum', c_ulong)]#number of devices connected to
LPCONNECTDLGSTRUCT = POINTER(CONNECTDLGSTRUCT)

CONNDLG_RO_PATH = 0x00000001#Resource path should be read-only
CONNDLG_CONN_POINT = 0x00000002#Netware -style movable connection point enabled
CONNDLG_USE_MRU = 0x00000004#Use MRU combobox
CONNDLG_HIDE_BOX = 0x00000008#Hide persistent connect checkbox

#Set at most ONE of the below flags.  If neither flag is set, then the persistence is set to whatever the user chose during  a previous connection
CONNDLG_PERSIST = 0x00000010#Force persistent connection
CONNDLG_NOT_PERSIST = 0x00000020#Force connection NOT persistent

if UNICODE:
	WNetConnectionDialog1 = WINFUNCTYPE(c_ulong, LPCONNECTDLGSTRUCT)(('WNetConnectionDialog1W', windll.mpr))
else:
	WNetConnectionDialog1 = WINFUNCTYPE(c_ulong, LPCONNECTDLGSTRUCT)(('WNetConnectionDialog1A', windll.mpr))

class DISCDLGSTRUCT(Structure):
	_fields_ = [('cbStructure', c_ulong),# size of this structure in bytes
	('hwndOwner', c_void_p)]# owner window for the dialog
	if UNICODE:
		_fields_ += [('lpLocalName', c_wchar_p),# local device name
		('lpRemoteName', c_wchar_p)]# network resource name
	else:
		_fields_ += [('lpLocalName', c_char_p),
		('lpRemoteName', c_char_p)]
	_fields_ += [('dwFlags', c_ulong)]# flags
LPDISCDLGSTRUCT = POINTER(DISCDLGSTRUCT)

DISC_UPDATE_PROFILE = 0x00000001
DISC_NO_FORCE = 0x00000040

if UNICODE:
	WNetDisconnectDialog1 = WINFUNCTYPE(c_ulong, LPDISCDLGSTRUCT)(('WNetDisconnectDialog1W', windll.mpr))
else:
	WNetDisconnectDialog1 = WINFUNCTYPE(c_ulong, LPDISCDLGSTRUCT)(('WNetDisconnectDialog1A', windll.mpr))


#  Network Browsing.

WNetCloseEnum = WINFUNCTYPE(c_ulong, c_void_p)(('WNetCloseEnum', windll.mpr))

if UNICODE:
	_WNetOpenEnum = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_ulong, LPNETRESOURCE, c_void_p)(('WNetOpenEnumW', windll.mpr))
	_WNetEnumResource = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, LPNETRESOURCE, c_void_p)(('WNetEnumResourceW', windll.mpr))
	_WNetGetResourceParent = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_void_p, c_void_p)(('WNetGetResourceParentW', windll.mpr))
	_WNetGetResourceInformation = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_void_p, c_void_p, c_void_p)(('WNetGetResourceInformationW', windll.mpr))
else:
	_WNetOpenEnum = WINFUNCTYPE(c_ulong, c_ulong, c_ulong, c_ulong, LPNETRESOURCE, c_void_p)(('WNetOpenEnumA', windll.mpr))
	_WNetEnumResource = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, LPNETRESOURCE, c_void_p)(('WNetEnumResourceA', windll.mpr))
	_WNetGetResourceParent = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_void_p, c_void_p)(('WNetGetResourceParentA', windll.mpr))
	_WNetGetResourceInformation = WINFUNCTYPE(c_ulong, LPNETRESOURCE, c_void_p, c_void_p, c_void_p)(('WNetGetResourceInformationA', windll.mpr))

def WNetOpenEnum(dwScope, dwType, dwUsage, lpNetResource = None):
	lphEnum = c_void_p()
	result = _WNetOpenEnum(dwScope, dwType, dwUsage, lpNetResource, byref(lphEnum))
	return result, lphEnum.value

def WNetEnumResource(hEnum, lpcCount = c_ulong(-1), lpBufferSize = c_ulong(16384)):
	from pywingui.windows import GlobalAlloc#, ZeroMemory
	lpBuffer = cast(GlobalAlloc(0, lpBufferSize.value), LPNETRESOURCE)
	#~ ZeroMemory(lpBuffer, lpBufferSize.value)
	result = _WNetEnumResource(hEnum, byref(lpcCount), lpBuffer, byref(lpBufferSize))
	return result, lpcCount.value, lpBuffer, lpBufferSize.value

def WNetGetResourceParent(lpNetResource, lpcbBuffer = c_ulong()):
	lpBuffer = c_void_p()
	result = _WNetGetResourceParent(lpNetResource, byref(lpBuffer), byref(lpcbBuffer))
	return result, lpBuffer, lpcbBuffer.value

def WNetGetResourceInformation(lpNetResource, lpcbBuffer = c_ulong()):
	lpBuffer = c_void_p()
	lplpSystem = c_void_p()
	result = _WNetGetResourceInformation(lpNetResource, byref(lpBuffer), byref(lpcbBuffer), byref(lplpSystem))
	system = wstring_at(lplpSystem)
	if not UNICODE:
		system = string_at(lplpSystem)
	return result, lpBuffer, lpcbBuffer.value, system


#  Universal Naming.

UNIVERSAL_NAME_INFO_LEVEL = 0x00000001
REMOTE_NAME_INFO_LEVEL = 0x00000002

class UNIVERSAL_NAME_INFO(Structure):
	_fields_ = [('lpUniversalName', c_wchar_p)]
	if not UNICODE:
		_fields_ = [('lpUniversalName', c_char_p)]
LPUNIVERSAL_NAME_INFO = POINTER(UNIVERSAL_NAME_INFO)

class REMOTE_NAME_INFO(Structure):
	_fields_ = [('lpUniversalName', c_wchar_p),
	('lpConnectionName', c_wchar_p),
	('lpRemainingPath', c_wchar_p)]
	if not UNICODE:
		_fields_ = [('lpUniversalName', c_char_p),
		('lpConnectionName', c_char_p),
		('lpRemainingPath', c_char_p)]
LPREMOTE_NAME_INFO = POINTER(REMOTE_NAME_INFO)

if UNICODE:
	_WNetGetUniversalName = WINFUNCTYPE(c_ulong, c_wchar_p, c_ulong, c_void_p, c_void_p)(('WNetGetUniversalNameW', windll.mpr))
	_WNetGetUser = WINFUNCTYPE(c_ulong, c_ulong, c_wchar_p, c_void_p, c_void_p)(('WNetGetUserW', windll.mpr))
else:
	_WNetGetUniversalName = WINFUNCTYPE(c_ulong, c_char_p, c_ulong, c_void_p, c_void_p)(('WNetGetUniversalNameA', windll.mpr))
	_WNetGetUser = WINFUNCTYPE(c_ulong, c_ulong, c_char_p, c_void_p, c_void_p)(('WNetGetUserA', windll.mpr))

def WNetGetUniversalName(lpLocalPath, dwInfoLevel, lpBufferSize = c_ulong()):
	lpBuffer = c_void_p()
	result = _WNetGetUniversalName(lpLocalPath, dwInfoLevel, byref(lpBuffer), byref(lpBufferSize))
	return result, lpBuffer, lpBufferSize.value

def WNetGetUser(lpName, lpnLength = c_ulong()):
	lpUserName = c_void_p()
	result = _WNetGetUser(lpName, byref(lpUserName), byref(lpnLength))
	UserName = wstring_at(lpUserName)
	if not UNICODE:
		UserName = string_at(lpUserName)
	return result, UserName, lpnLength.value


# Other.

if WINVER >= 0x0400:
	WNFMT_MULTILINE = 0x01
	WNFMT_ABBREVIATED = 0x02
	WNFMT_INENUM = 0x10
	WNFMT_CONNECTION = 0x20

	if UNICODE:
		_WNetGetProviderName = WINFUNCTYPE(c_ulong, c_ulong, c_void_p, c_void_p)(('WNetGetProviderNameW', windll.mpr))
	else:
		_WNetGetProviderName = WINFUNCTYPE(c_ulong, c_ulong, c_void_p, c_void_p)(('WNetGetProviderNameA', windll.mpr))

	def WNetGetProviderName(dwNetType, lpBufferSize = c_ulong()):
		lpProviderName = c_void_p()
		result = _WNetGetProviderName(dwNetType, byref(lpProviderName), byref(lpBufferSize))
		ProviderName = wstring_at(lpProviderName)
		if not UNICODE:
			ProviderName = string_at(lpProviderName)
		return result, ProviderName, lpBufferSize.value

	class NETINFOSTRUCT(Structure):
		_fields_ = [('cbStructure', c_ulong),
		('dwProviderVersion', c_ulong),
		('dwStatus', c_ulong),
		('dwCharacteristics', c_ulong),
		('dwHandle', c_ulong),# ULONG_PTR = c_void_p, or ...
		('wNetType', c_ushort),
		('dwPrinters', c_ulong),
		('dwDrives', c_ulong)]
	LPNETINFOSTRUCT = POINTER(NETINFOSTRUCT)

	NETINFO_DLL16 = 0x00000001# Provider running as 16 bit Winnet Driver
	NETINFO_DISKRED = 0x00000004# Provider requires disk redirections to connect
	NETINFO_PRINTERRED = 0x00000008# Provider requires printer redirections to connect

	if UNICODE:
		_WNetGetNetworkInformation = WINFUNCTYPE(c_ulong, c_wchar_p, LPNETINFOSTRUCT)(('WNetGetNetworkInformationW', windll.mpr))
	else:
		_WNetGetNetworkInformation = WINFUNCTYPE(c_ulong, c_wchar_p, LPNETINFOSTRUCT)(('WNetGetNetworkInformationA', windll.mpr))

	def WNetGetProviderName(lpProvider = ''):
		lpNetInfoStruct = NETINFOSTRUCT()
		result = _WNetGetNetworkInformation(lpProvider, lpNetInfoStruct)
		return result, lpNetInfoStruct


#  Error handling.

if UNICODE:
	_WNetGetLastError = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, c_ulong, c_void_p, c_ulong)(('WNetGetLastErrorW', windll.mpr))
else:
	_WNetGetLastError = WINFUNCTYPE(c_ulong, c_void_p, c_void_p, c_ulong, c_void_p, c_ulong)(('WNetGetLastErrorA', windll.mpr))

def WNetGetLastError(nErrorBufSize = 0, nNameBufSize = 0):
	lpError = c_ulong()
	lpErrorBuf = c_wchar_p()
	lpNameBuf = c_wchar_p()
	if not UNICODE:
		lpErrorBuf = c_char_p()
		lpNameBuf = c_char_p()
	result = _WNetGetLastError(byref(lpError), byref(lpErrorBuf), nErrorBufSize, byref(lpNameBuf), nNameBufSize)
	return result, lpError.value, lpErrorBuf.value, lpNameBuf.value


#  STATUS CODES

# General
WN_SUCCESS        = NO_ERROR
WN_NO_ERROR       = NO_ERROR
WN_NOT_SUPPORTED  = ERROR_NOT_SUPPORTED
WN_CANCEL         = ERROR_CANCELLED
WN_RETRY          = ERROR_RETRY
WN_NET_ERROR      = ERROR_UNEXP_NET_ERR
WN_MORE_DATA      = ERROR_MORE_DATA
WN_BAD_POINTER    = ERROR_INVALID_ADDRESS
WN_BAD_VALUE      = ERROR_INVALID_PARAMETER
WN_BAD_USER       = ERROR_BAD_USERNAME
WN_BAD_PASSWORD   = ERROR_INVALID_PASSWORD
WN_ACCESS_DENIED  = ERROR_ACCESS_DENIED
WN_FUNCTION_BUSY  = ERROR_BUSY
WN_WINDOWS_ERROR  = ERROR_UNEXP_NET_ERR
WN_OUT_OF_MEMORY  = ERROR_NOT_ENOUGH_MEMORY
WN_NO_NETWORK     = ERROR_NO_NETWORK
WN_EXTENDED_ERROR = ERROR_EXTENDED_ERROR
WN_BAD_LEVEL      = ERROR_INVALID_LEVEL
WN_BAD_HANDLE     = ERROR_INVALID_HANDLE
if WINVER >= 0x0400:
	WN_NOT_INITIALIZING = ERROR_ALREADY_INITIALIZED
	WN_NO_MORE_DEVICES  = ERROR_NO_MORE_DEVICES

# Connection
WN_NOT_CONNECTED             = ERROR_NOT_CONNECTED
WN_OPEN_FILES                = ERROR_OPEN_FILES
WN_DEVICE_IN_USE             = ERROR_DEVICE_IN_USE
WN_BAD_NETNAME               = ERROR_BAD_NET_NAME
WN_BAD_LOCALNAME             = ERROR_BAD_DEVICE
WN_ALREADY_CONNECTED         = ERROR_ALREADY_ASSIGNED
WN_DEVICE_ERROR              = ERROR_GEN_FAILURE
WN_CONNECTION_CLOSED         = ERROR_CONNECTION_UNAVAIL
WN_NO_NET_OR_BAD_PATH        = ERROR_NO_NET_OR_BAD_PATH
WN_BAD_PROVIDER              = ERROR_BAD_PROVIDER
WN_CANNOT_OPEN_PROFILE       = ERROR_CANNOT_OPEN_PROFILE
WN_BAD_PROFILE               = ERROR_BAD_PROFILE
WN_BAD_DEV_TYPE              = ERROR_BAD_DEV_TYPE
WN_DEVICE_ALREADY_REMEMBERED = ERROR_DEVICE_ALREADY_REMEMBERED
WN_CONNECTED_OTHER_PASSWORD  = ERROR_CONNECTED_OTHER_PASSWORD
if WINVER >= 0x0501:
	WN_CONNECTED_OTHER_PASSWORD_DEFAULT = ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT

# Enumeration
WN_NO_MORE_ENTRIES = ERROR_NO_MORE_ITEMS
WN_NOT_CONTAINER   = ERROR_NOT_CONTAINER

# Authentication
if WINVER >= 0x0400:
	WN_NOT_AUTHENTICATED = ERROR_NOT_AUTHENTICATED
	WN_NOT_LOGGED_ON     = ERROR_NOT_LOGGED_ON
	WN_NOT_VALIDATED     = ERROR_NO_LOGON_SERVERS


#  For Shell

if WINVER >= 0x0400:

	class NETCONNECTINFOSTRUCT(Structure):
		_fields_ = [('cbStructure', c_ulong),
		('dwFlags', c_ulong),
		('dwSpeed', c_ulong),
		('dwDelay', c_ulong),
		('dwOptDataSize', c_ulong)]
	LPNETCONNECTINFOSTRUCT = POINTER(NETCONNECTINFOSTRUCT)


	WNCON_FORNETCARD = 0x00000001
	WNCON_NOTROUTED = 0x00000002
	WNCON_SLOWLINK = 0x00000004
	WNCON_DYNAMIC = 0x00000008

	if UNICODE:
		_MultinetGetConnectionPerformance = WINFUNCTYPE(c_ulong, LPNETRESOURCE, LPNETCONNECTINFOSTRUCT)(('MultinetGetConnectionPerformanceW', windll.mpr))
	else:
		_MultinetGetConnectionPerformance = WINFUNCTYPE(c_ulong, LPNETRESOURCE, LPNETCONNECTINFOSTRUCT)(('MultinetGetConnectionPerformanceA', windll.mpr))

	def MultinetGetConnectionPerformance(lpNetResource):
		lpNetConnectInfoStruct = NETCONNECTINFOSTRUCT()
		result = _MultinetGetConnectionPerformance(lpNetResource, lpNetInfoStruct, lpNetConnectInfoStruct)
		return result, lpNetConnectInfoStruct
