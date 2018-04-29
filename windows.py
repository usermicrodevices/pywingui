## 	   Copyright (c) 2003 Henk Punt

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the
## "Software"), to deal in the Software without restriction, including
## without limitation the rights to use, copy, modify, merge, publish,
## distribute, sublicense, and/or sell copies of the Software, and to
## permit persons to whom the Software is furnished to do so, subject to
## the following conditions:

## The above copyright notice and this permission notice shall be
## included in all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
## NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
## LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
## OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
## WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

from version_microsoft import WINVER, UNICODE

from ctypes import *

from sys import hexversion
if hexversion < 0x02060000:
	c_bool = c_byte

#TODO auto ie/comctl detection
WIN32_IE = 0x0550

#TODO: auto unicode selection,
#if unicode:
#  CreateWindowEx = windll.user32.CreateWindowExW
#else:
#  CreateWindowEx = windll.user32.CreateWindowExA
#etc, etc


DWORD = c_ulong
HANDLE = c_void_p
UINT = c_uint
BOOL = c_int
HWND = HANDLE
HINSTANCE = HANDLE
HICON = HANDLE
HDC = HANDLE
HCURSOR = HANDLE
HBRUSH = HANDLE
HMENU = HANDLE
HBITMAP = HANDLE
HIMAGELIST = HANDLE
HGDIOBJ = HANDLE
HMETAFILE = HANDLE
HRGN = HANDLE

ULONG = DWORD
ULONG_PTR = DWORD
UINT_PTR = DWORD
LONG_PTR = c_long
INT = c_int
LPCTSTR = c_char_p
LPTSTR = c_char_p
PSTR = c_char_p
LPCSTR = c_char_p
LPCWSTR = c_wchar_p
LPSTR = c_char_p
LPWSTR = c_wchar_p
PVOID = c_void_p
USHORT = c_ushort
WORD = c_ushort
ATOM = WORD
SHORT = c_short
LPARAM = c_ulong
WPARAM = c_uint
LPVOID = c_void_p
LONG = c_long
BYTE = c_byte
TCHAR = c_char #TODO depends on unicode/wide conventions
DWORD_PTR = c_ulong #TODO what is this exactly?
INT_PTR = c_ulong  #TODO what is this exactly?
COLORREF = c_ulong
CLIPFORMAT = WORD
FLOAT = c_float
CHAR = c_char
WCHAR = c_wchar

FXPT16DOT16 = c_long
FXPT2DOT30 = c_long
LCSCSTYPE = c_long
LCSGAMUTMATCH = c_long
COLOR16 = USHORT

LRESULT = LONG_PTR

#### Windows version detection ##############################
class OSVERSIONINFO(Structure):
	_fields_ = [("dwOSVersionInfoSize", DWORD),
	("dwMajorVersion", DWORD),
	("dwMinorVersion", DWORD),
	("dwBuildNumber", DWORD),
	("dwPlatformId", DWORD),
	("szCSDVersion", TCHAR * 128)]

	def isMajorMinor(self, major, minor):
		return (self.dwMajorVersion, self.dwMinorVersion) == (major, minor)

GetVersion = windll.kernel32.GetVersionExA
versionInfo = OSVERSIONINFO()
versionInfo.dwOSVersionInfoSize = sizeof(versionInfo)
GetVersion(byref(versionInfo))

def MAKELONG(w1, w2):
	return w1 | (w2 << 16)

MAKELPARAM = MAKELONG

##### Windows Callback functions ################################
WNDPROC = WINFUNCTYPE(c_int, HWND, UINT, WPARAM, LPARAM)
DialogProc = WINFUNCTYPE(c_int, HWND, UINT, WPARAM, LPARAM)

CBTProc = WINFUNCTYPE(c_int, c_int, c_int, c_int)
MessageProc = CBTProc

EnumChildProc = WINFUNCTYPE(c_int, HWND, LPARAM)

MSGBOXCALLBACK = WINFUNCTYPE(c_int, HWND, LPARAM) #TODO look up real def

class WNDCLASSEX(Structure):
	_fields_ = [("cbSize", UINT),
	("style",  UINT),
	("lpfnWndProc", WNDPROC),
	("cbClsExtra", INT),
	("cbWndExtra", INT),
	("hInstance", HINSTANCE),
	("hIcon", c_void_p),#HICON
	("hCursor", HCURSOR),
	("hbrBackground", HBRUSH)]
	if UNICODE:
		_fields_ += [("lpszMenuName", c_wchar_p), ("lpszClassName", c_wchar_p)]
	else:
		_fields_ += [("lpszMenuName", c_char_p), ("lpszClassName", c_char_p)]
	_fields_.append(("hIconSm", c_void_p))#HICON

class POINT(Structure):
	_fields_ = [("x", LONG), ("y", LONG)]
	def __str__(self):
		return "POINT {x: %d, y: %d}" % (self.x, self.y)
POINTL = POINT
LPPOINT = POINTER(POINT)

class POINTS(Structure):
	_fields_ = [("x", SHORT), ("y", SHORT)]


PtInRect = windll.user32.PtInRect

class RECT(Structure):
	_fields_ = [("left", LONG),
		("top", LONG),
		("right", LONG),
		("bottom", LONG)]

	def __str__(self):
		return "RECT {left: %d, top: %d, right: %d, bottom: %d}" % (self.left, self.top, self.right, self.bottom)

	def __add__(self, value):
		left, top, right, bottom = 0, 0, 0, 0
		if self.left > value.left:
			left = value.left
		else:
			left = self.left
		if self.top > value.top:
			top = value.top
		else:
			top = self.top
		if self.right < value.right:
			right = value.right
		else:
			right = self.right
		if self.bottom < value.bottom:
			bottom = value.bottom
		else:
			bottom = self.bottom
		return RECT(left, top, right, bottom)

	def __iadd__(self, value):
		if self.left > value.left:
			self.left = value.left
		if self.top > value.top:
			self.top = value.top
		if self.right < value.right:
			self.right = value.right
		if self.bottom < value.bottom:
			self.bottom = value.bottom

	def getHeight(self):
		return self.bottom - self.top

	height = property(getHeight, None, None, "")

	def getWidth(self):
		return self.right - self.left

	width = property(getWidth, None, None, "")

	def getSize(self):
		return self.width, self.height

	size = property(getSize, None, None, "")

	def ContainsPoint(self, pt):
		"""determines if this RECT contains the given POINT pt
		returns True if pt is in this rect
		"""
		return bool(PtInRect(byref(self), pt))

RECTL = RECT        

class SIZE(Structure):
	_fields_ = [('cx', LONG), ('cy', LONG)]

SIZEL = SIZE        

##class MSG(Structure):
##    _fields_ = [("hWnd", HWND),
##                ("message", UINT),
##                ("wParam", WPARAM),
##                ("lParam", LPARAM),
##                ("time", DWORD),
##                ("pt", POINT)]

##    def __str__(self):
##        return "MSG {%d %d %d %d %d %s}" % (self.hWnd, self.message, self.wParam, self.lParam,
##                                            self.time, str(self.pt))

#Hack: we need to use the same MSG type as comtypes.ole uses!
from ctypes.wintypes import MSG

class ACCEL(Structure):
	_fields_ = [("fVirt", BYTE),
	("key", WORD),
	("cmd", WORD)]

class CREATESTRUCT(Structure):
	_fields_ = [("lpCreateParams", LPVOID),
	("hInstance", HINSTANCE),
	("hMenu", HMENU),
	("hwndParent", HWND),
	("cx", INT),
	("cy", INT),
	("x", INT),
	("y", INT),
	("style", LONG)]
	if UNICODE:
		_fields_ += [("lpszName", c_wchar_p), ("lpszClass", c_wchar_p)]
	else:
		_fields_ += [("lpszName", c_char_p), ("lpszClass", c_char_p)]
	_fields_.append(("dwExStyle", DWORD))

class NMHDR(Structure):
	_fields_ = [("hwndFrom", HWND),
	("idFrom", UINT),
	("code", UINT)]

class PAINTSTRUCT(Structure):
	_fields_ = [("hdc", HDC),
	("fErase", BOOL),
	("rcPaint", RECT),
	("fRestore", BOOL),
	("fIncUpdate", BOOL),
	("rgbReserved", c_byte * 32)]

    
class MENUITEMINFO(Structure):
	_fields_ = [("cbSize", UINT),
	("fMask", UINT),
	("fType", UINT),
	("fState", UINT),
	("wID", UINT),
	("hSubMenu", HMENU),
	("hbmpChecked", HBITMAP),
	("hbmpUnchecked", HBITMAP),
	("dwItemData", ULONG_PTR)]
	if UNICODE:
		_fields_.append(("dwTypeData", c_wchar_p))
	else:
		_fields_.append(("dwTypeData", c_char_p))
	_fields_.append(("cch", UINT))
	if WINVER >= 0x0500:
		_fields_.append(("hbmpItem", HBITMAP))

class DLGTEMPLATE(Structure):
	_pack_ = 2
	_fields_ = [
		("style", DWORD),
		("exStyle", DWORD),
		("cDlgItems", WORD),
		("x", c_short),
		("y", c_short),
		("cx", c_short),
		("cy", c_short)
	]

class DLGITEMTEMPLATE(Structure):
	_pack_ = 2
	_fields_ = [
		("style", DWORD),
		("exStyle", DWORD),
		("x", c_short),
		("y", c_short),
		("cx", c_short),
		("cy", c_short),
		("id", WORD)
	]

class COPYDATASTRUCT(Structure):
	_fields_ = [
		("dwData", ULONG_PTR),
		("cbData", DWORD),
		("lpData", PVOID)]

def LOWORD(dword):
	return dword & 0x0000ffff

def HIWORD(dword):
	return dword >> 16

TRUE = 1
FALSE = 0
NULL = 0

IDI_APPLICATION = 32512

SW_HIDE            = 0
SW_SHOWNORMAL      = 1
SW_NORMAL          = 1
SW_SHOWMINIMIZED   = 2
SW_SHOWMAXIMIZED   = 3
SW_MAXIMIZE        = 3
SW_SHOWNOACTIVATE  = 4
SW_SHOW            = 5
SW_MINIMIZE        = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA          = 8
SW_RESTORE         = 9
SW_SHOWDEFAULT     = 10
SW_FORCEMINIMIZE   = 11
SW_MAX             = 11

EN_CHANGE = 768

MSGS = [('WM_NULL', 0),
        ('WM_CREATE', 1),
        ('WM_CANCELMODE', 31),
        ('WM_CAPTURECHANGED', 533),
        ('WM_CLOSE', 16),
        ('WM_COMMAND', 273),
        ('WM_DESTROY', 2),
        ('WM_ERASEBKGND', 20),
        ('WM_GETFONT', 49),
        ('WM_INITDIALOG', 272),
        ('WM_INITMENUPOPUP', 279),
        ('WM_KEYDOWN', 256),
        ('WM_KEYFIRST', 256),
        ('WM_KEYLAST', 264),
        ('WM_KEYUP', 257),
        ('WM_LBUTTONDBLCLK', 515),
        ('WM_LBUTTONDOWN', 513),
        ('WM_LBUTTONUP', 514),
        ('WM_MBUTTONDBLCLK', 521),
        ('WM_MBUTTONDOWN', 519),
        ('WM_MBUTTONUP', 520),
        ('WM_MENUSELECT', 287),
        ('WM_MOUSEFIRST', 512),
        ('WM_MOUSEHOVER', 673),
        ('WM_MOUSELEAVE', 675),
        ('WM_MOUSEMOVE', 512),
        ('WM_MOVE', 3),
        ('WM_NCCREATE', 129),
        ('WM_NCDESTROY', 130),
        ('WM_NOTIFY', 78),
        ('WM_PAINT', 15),
        ('WM_RBUTTONDBLCLK', 518),
        ('WM_RBUTTONDOWN', 516),
        ('WM_RBUTTONUP', 517),
        ('WM_SETCURSOR', 32),
        ('WM_SETFONT', 48),
        ('WM_SETREDRAW', 11),
        ('WM_SIZE', 5),
        ('WM_SYSKEYDOWN', 260),
        ('WM_SYSKEYUP', 261),
        ('WM_USER', 1024),
        ('WM_WINDOWPOSCHANGED', 71),
        ('WM_WINDOWPOSCHANGING', 70),
        ('WM_SETTEXT', 12),
        ('WM_GETTEXT', 13),
        ('WM_GETTEXTLENGTH', 14),
        ('WM_ACTIVATE', 6),
        ('WM_HSCROLL', 276),
        ('WM_VSCROLL', 277),
        ('WM_CTLCOLORBTN', 309),
        ('WM_CTLCOLORDLG', 310),
        ('WM_CTLCOLOREDIT', 307),
        ('WM_CTLCOLORLISTBOX', 308),
        ('WM_CTLCOLORMSGBOX', 306),
        ('WM_CTLCOLORSCROLLBAR', 311),
        ('WM_CTLCOLORSTATIC', 312),
        ('WM_TIMER', 0x0113),
        ('WM_CONTEXTMENU', 0x007B),
        ('WM_COPYDATA', 0x004A),
        ('WM_ACTIVATEAPP', 0x001C),
        ('WM_NCACTIVATE', 0x0086)
        ]

#insert wm_* msgs as constants in this module:
for key, val in MSGS:
    exec('%s = %d' % (key, val)) #TODO without using 'exec'?

BN_CLICKED    =     0

VK_DOWN = 40
VK_LEFT = 37
VK_RIGHT = 39
VK_DELETE  = 0x2E

CS_HREDRAW = 2
CS_VREDRAW = 1
#~ WHITE_BRUSH = 0

MIIM_STATE= 1
MIIM_ID= 2
MIIM_SUBMENU =4
MIIM_CHECKMARKS= 8
MIIM_TYPE= 16
MIIM_DATA= 32
MIIM_STRING= 64
MIIM_BITMAP= 128
MIIM_FTYPE =256

MFT_BITMAP= 4
MFT_MENUBARBREAK =32
MFT_MENUBREAK= 64
MFT_OWNERDRAW= 256
MFT_RADIOCHECK= 512
MFT_RIGHTJUSTIFY= 0x4000
MFT_SEPARATOR =0x800
MFT_RIGHTORDER= 0x2000L
MFT_STRING = 0

# Menu flags for Add/Check/EnableMenuItem()
MF_INSERT          = 0x00000000L
MF_CHANGE          = 0x00000080L
MF_APPEND          = 0x00000100L
MF_DELETE          = 0x00000200L
MF_REMOVE          = 0x00001000L
MF_BYCOMMAND       = 0x00000000L
MF_BYPOSITION      = 0x00000400L
MF_SEPARATOR       = 0x00000800L
MF_ENABLED         = 0x00000000L
MF_GRAYED          = 0x00000001L
MF_DISABLED        = 0x00000002L
MF_UNCHECKED       = 0x00000000L
MF_CHECKED         = 0x00000008L
MF_USECHECKBITMAPS = 0x00000200L
MF_STRING          = 0x00000000L
MF_BITMAP          = 0x00000004L
MF_OWNERDRAW       = 0x00000100L
MF_POPUP           = 0x00000010L
MF_MENUBARBREAK    = 0x00000020L
MF_MENUBREAK       = 0x00000040L
MF_UNHILITE        = 0x00000000L
MF_HILITE          = 0x00000080L
if WINVER >= 0x0400:
	MF_DEFAULT = 0x00001000L
MF_SYSMENU = 0x00002000L
MF_HELP    = 0x00004000L
if WINVER >= 0x0400:
	MF_RIGHTJUSTIFY = 0x00004000L
MF_MOUSESELECT = 0x00008000L
if WINVER >= 0x0400:
	MF_END = 0x00000080L  # Obsolete -- only used by old RES files

if WINVER >= 0x0400:
	MFT_STRING         = MF_STRING
	MFT_BITMAP         = MF_BITMAP
	MFT_MENUBARBREAK   = MF_MENUBARBREAK
	MFT_MENUBREAK      = MF_MENUBREAK
	MFT_OWNERDRAW      = MF_OWNERDRAW
	MFT_RADIOCHECK     = 0x00000200L
	MFT_SEPARATOR      = MF_SEPARATOR
	MFT_RIGHTORDER     = 0x00002000L
	MFT_RIGHTJUSTIFY   = MF_RIGHTJUSTIFY

	# Menu flags for Add/Check/EnableMenuItem()
	MFS_GRAYED         = 0x00000003L
	MFS_DISABLED       = MFS_GRAYED
	MFS_CHECKED        = MF_CHECKED
	MFS_HILITE         = MF_HILITE
	MFS_ENABLED        = MF_ENABLED
	MFS_UNCHECKED      = MF_UNCHECKED
	MFS_UNHILITE       = MF_UNHILITE
	MFS_DEFAULT        = MF_DEFAULT

LOCALE_SYSTEM_DEFAULT =  0x800

WS_BORDER	= 0x800000
WS_CAPTION	= 0xc00000
WS_CHILD	= 0x40000000
WS_CHILDWINDOW	= 0x40000000
WS_CLIPCHILDREN = 0x2000000
WS_CLIPSIBLINGS = 0x4000000
WS_DISABLED	= 0x8000000
WS_DLGFRAME	= 0x400000
WS_GROUP	= 0x20000
WS_HSCROLL	= 0x100000
WS_ICONIC	= 0x20000000
WS_MAXIMIZE	= 0x1000000
WS_MAXIMIZEBOX	= 0x10000
WS_MINIMIZE	= 0x20000000
WS_MINIMIZEBOX	= 0x20000
WS_OVERLAPPED	= 0
WS_OVERLAPPEDWINDOW = 0xcf0000
WS_POPUP	= 0x80000000l
WS_POPUPWINDOW	= 0x80880000
WS_SIZEBOX	= 0x40000
WS_SYSMENU	= 0x80000
WS_TABSTOP	= 0x10000
WS_THICKFRAME	= 0x40000
WS_TILED	= 0
WS_TILEDWINDOW	= 0xcf0000
WS_VISIBLE	= 0x10000000
WS_VSCROLL	= 0x200000

# Extended Window Styles
WS_EX_DLGMODALFRAME    = 0x00000001L
WS_EX_NOPARENTNOTIFY   = 0x00000004L
WS_EX_TOPMOST          = 0x00000008L
WS_EX_ACCEPTFILES      = 0x00000010L
WS_EX_TRANSPARENT      = 0x00000020L
if WINVER >= 0x0400:
	WS_EX_MDICHILD         = 0x00000040L
	WS_EX_TOOLWINDOW       = 0x00000080L
	WS_EX_WINDOWEDGE       = 0x00000100L
	WS_EX_CLIENTEDGE       = 0x00000200L
	WS_EX_CONTEXTHELP      = 0x00000400L

	WS_EX_RIGHT            = 0x00001000L
	WS_EX_LEFT             = 0x00000000L
	WS_EX_RTLREADING       = 0x00002000L
	WS_EX_LTRREADING       = 0x00000000L
	WS_EX_LEFTSCROLLBAR    = 0x00004000L
	WS_EX_RIGHTSCROLLBAR   = 0x00000000L

	WS_EX_CONTROLPARENT    = 0x00010000L
	WS_EX_STATICEDGE       = 0x00020000L
	WS_EX_APPWINDOW        = 0x00040000L

	WS_EX_OVERLAPPEDWINDOW = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
	WS_EX_PALETTEWINDOW    = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)

if WINVER >= 0x0500:
	WS_EX_LAYERED          = 0x00080000
	WS_EX_NOINHERITLAYOUT  = 0x00100000L # Disable inheritence of mirroring by children
	WS_EX_LAYOUTRTL        = 0x00400000L # Right to left mirroring

if WINVER >= 0x0501:
	WS_EX_COMPOSITED       = 0x02000000L
if WINVER >= 0x0500:
	WS_EX_NOACTIVATE       = 0x08000000L

WA_INACTIVE = 0
WA_ACTIVE = 1
WA_CLICKACTIVE = 2

RB_SETBARINFO = WM_USER + 4
RB_GETBANDCOUNT = WM_USER +  12
RB_INSERTBANDA = WM_USER + 1
RB_INSERTBANDW = WM_USER + 10

RB_INSERTBAND = RB_INSERTBANDA

RBBIM_STYLE = 1
RBBIM_COLORS = 2
RBBIM_TEXT = 4
RBBIM_IMAGE = 8
RBBIM_CHILD = 16
RBBIM_CHILDSIZE = 32
RBBIM_SIZE = 64
RBBIM_BACKGROUND = 128
RBBIM_ID = 256
RBBIM_IDEALSIZE = 0x00000200

TPM_CENTERALIGN =4
TPM_LEFTALIGN =0
TPM_RIGHTALIGN= 8
TPM_LEFTBUTTON= 0
TPM_RIGHTBUTTON= 2
TPM_HORIZONTAL= 0
TPM_VERTICAL= 64
TPM_TOPALIGN= 0
TPM_VCENTERALIGN= 16
TPM_BOTTOMALIGN= 32
TPM_NONOTIFY= 128
TPM_RETURNCMD= 256

TBIF_TEXT = 0x00000002

DT_NOPREFIX   =      0x00000800
DT_HIDEPREFIX =      1048576

WH_CBT       =  5
WH_MSGFILTER =  (-1)

I_IMAGENONE = -2
TBSTATE_ENABLED = 4

BTNS_SHOWTEXT = 0x00000040
CW_USEDEFAULT = 0x80000000

COLOR_3DFACE = 15

BF_LEFT      = 1
BF_TOP       = 2
BF_RIGHT     = 4
BF_BOTTOM    = 8

BDR_RAISEDOUTER =      1
BDR_SUNKENOUTER =      2
BDR_RAISEDINNER =      4
BDR_SUNKENINNER =      8
BDR_OUTER    = 3
BDR_INNER    = 0xc
BDR_RAISED   = 5
BDR_SUNKEN   = 10

EDGE_RAISED  = (BDR_RAISEDOUTER|BDR_RAISEDINNER)
EDGE_SUNKEN  = (BDR_SUNKENOUTER|BDR_SUNKENINNER)
EDGE_ETCHED  = (BDR_SUNKENOUTER|BDR_RAISEDINNER)
EDGE_BUMP    = (BDR_RAISEDOUTER|BDR_SUNKENINNER)

IDC_SIZENWSE = 32642
IDC_SIZENESW = 32643
IDC_SIZEWE = 32644
IDC_SIZENS = 32645
IDC_SIZEALL = 32646
IDC_SIZE = 32640
IDC_ARROW = 32512

TCIF_TEXT    =1
TCIF_IMAGE   =2
TCIF_RTLREADING=      4
TCIF_PARAM  = 8


TCS_MULTILINE = 512

MK_LBUTTON    = 1
MK_RBUTTON    = 2
MK_SHIFT      = 4
MK_CONTROL    = 8
MK_MBUTTON    = 16

ILC_COLOR = 0
ILC_COLOR4 = 4
ILC_COLOR8 = 8
ILC_COLOR16 = 16
ILC_COLOR24 = 24
ILC_COLOR32 = 32
ILC_COLORDDB = 254
ILC_MASK = 1
ILC_PALETTE = 2048

IMAGE_BITMAP = 0
IMAGE_ICON = 1

LR_LOADFROMFILE = 16
LR_VGACOLOR = 0x0080
LR_LOADMAP3DCOLORS = 4096
LR_LOADTRANSPARENT = 32

LVSIL_NORMAL = 0
LVSIL_SMALL  = 1
LVSIL_STATE  = 2

TVSIL_NORMAL = 0
TVSIL_STATE  = 2

SRCCOPY = 0xCC0020

GWL_WNDPROC = -4

HWND_BOTTOM = 1
HWND_TOP=0
HWND_TOPMOST=-1

SWP_DRAWFRAME= 32
SWP_FRAMECHANGED= 32
SWP_HIDEWINDOW= 128
SWP_NOACTIVATE= 16
SWP_NOCOPYBITS= 256
SWP_NOMOVE= 2
SWP_NOSIZE= 1
SWP_NOREDRAW= 8
SWP_NOZORDER= 4
SWP_SHOWWINDOW= 64
SWP_NOOWNERZORDER =512
SWP_NOREPOSITION= 512
SWP_NOSENDCHANGING= 1024
SWP_DEFERERASE= 8192
SWP_ASYNCWINDOWPOS=  16384

DCX_WINDOW = 1
DCX_CACHE = 2
DCX_PARENTCLIP = 32
DCX_CLIPSIBLINGS= 16
DCX_CLIPCHILDREN= 8
DCX_NORESETATTRS= 4
DCX_LOCKWINDOWUPDATE= 0x400
DCX_EXCLUDERGN= 64
DCX_INTERSECTRGN =128
DCX_VALIDATE= 0x200000

GCL_STYLE = -26

SB_HORZ       =      0
SB_VERT       =      1
SB_CTL        =      2
SB_BOTH       =      3

SB_LINEUP           =0
SB_LINELEFT         =0
SB_LINEDOWN         =1
SB_LINERIGHT        =1
SB_PAGEUP           =2
SB_PAGELEFT         =2
SB_PAGEDOWN         =3
SB_PAGERIGHT        =3
SB_THUMBPOSITION    =4
SB_THUMBTRACK       =5
SB_TOP              =6
SB_LEFT             =6
SB_BOTTOM           =7
SB_RIGHT            =7
SB_ENDSCROLL        =8

MB_OK                    =   0x00000000
MB_OKCANCEL              =   0x00000001
MB_ABORTRETRYIGNORE      =   0x00000002
MB_YESNOCANCEL           =   0x00000003
MB_YESNO                 =   0x00000004
MB_RETRYCANCEL           =   0x00000005


MB_ICONASTERISK = 64
MB_ICONEXCLAMATION = 0x30
MB_ICONWARNING = 0x30
MB_ICONERROR = 16
MB_ICONHAND = 16
MB_ICONQUESTION = 32
MB_ICONINFORMATION = 64
MB_ICONSTOP = 16
MB_ICONMASK = 240

IDOK          =      1
IDCANCEL      =      2
IDABORT       =      3
IDRETRY       =      4
IDIGNORE      =      5
IDYES         =      6
IDNO          =      7
IDCLOSE       =  8
IDHELP        =  9

COLOR_3DDKSHADOW = 21
COLOR_3DFACE  = 15
COLOR_3DHILIGHT = 20
COLOR_3DHIGHLIGHT= 20
COLOR_3DLIGHT= 22
COLOR_BTNHILIGHT= 20
COLOR_3DSHADOW= 16
COLOR_ACTIVEBORDER =10
COLOR_ACTIVECAPTION= 2
COLOR_APPWORKSPACE= 12
COLOR_BACKGROUND= 1
COLOR_DESKTOP= 1
COLOR_BTNFACE= 15
COLOR_BTNHIGHLIGHT= 20
COLOR_BTNSHADOW= 16
COLOR_BTNTEXT= 18
COLOR_CAPTIONTEXT= 9
COLOR_GRAYTEXT= 17
COLOR_HIGHLIGHT= 13
COLOR_HIGHLIGHTTEXT= 14
COLOR_INACTIVEBORDER= 11
COLOR_INACTIVECAPTION= 3
COLOR_INACTIVECAPTIONTEXT= 19
COLOR_INFOBK= 24
COLOR_INFOTEXT= 23
COLOR_MENU= 4
COLOR_MENUTEXT= 7
COLOR_SCROLLBAR= 0
COLOR_WINDOW= 5
COLOR_WINDOWFRAME= 6
COLOR_WINDOWTEXT= 8
CTLCOLOR_MSGBOX= 0
CTLCOLOR_EDIT= 1
CTLCOLOR_LISTBOX= 2
CTLCOLOR_BTN= 3
CTLCOLOR_DLG= 4
CTLCOLOR_SCROLLBAR= 5
CTLCOLOR_STATIC= 6
CTLCOLOR_MAX= 7


GMEM_FIXED         = 0x0000
GMEM_MOVEABLE      = 0x0002
GMEM_NOCOMPACT     = 0x0010
GMEM_NODISCARD     = 0x0020
GMEM_ZEROINIT      = 0x0040
GMEM_MODIFY        = 0x0080
GMEM_DISCARDABLE   = 0x0100
GMEM_NOT_BANKED    = 0x1000
GMEM_SHARE         = 0x2000
GMEM_DDESHARE      = 0x2000
GMEM_NOTIFY        = 0x4000
GMEM_LOWER         = GMEM_NOT_BANKED
GMEM_VALID_FLAGS   = 0x7F72
GMEM_INVALID_HANDLE= 0x8000

RT_DIALOG        = "5"

CF_TEXT = 1


# Button Control Styles
#BS_DEFPUSHBUTTON = 0x01L
#BS_GROUPBOX = 0x7
BS_PUSHBUTTON       = 0x00000000L
BS_DEFPUSHBUTTON    = 0x00000001L
BS_CHECKBOX         = 0x00000002L
BS_AUTOCHECKBOX     = 0x00000003L
BS_RADIOBUTTON      = 0x00000004L
BS_3STATE           = 0x00000005L
BS_AUTO3STATE       = 0x00000006L
BS_GROUPBOX         = 0x00000007L
BS_USERBUTTON       = 0x00000008L
BS_AUTORADIOBUTTON  = 0x00000009L
BS_PUSHBOX          = 0x0000000AL
BS_OWNERDRAW        = 0x0000000BL
BS_TYPEMASK         = 0x0000000FL
BS_LEFTTEXT         = 0x00000020L
if WINVER >= 0x0400:
	BS_TEXT             = 0x00000000L
	BS_ICON             = 0x00000040L
	BS_BITMAP           = 0x00000080L
	BS_LEFT             = 0x00000100L
	BS_RIGHT            = 0x00000200L
	BS_CENTER           = 0x00000300L
	BS_TOP              = 0x00000400L
	BS_BOTTOM           = 0x00000800L
	BS_VCENTER          = 0x00000C00L
	BS_PUSHLIKE         = 0x00001000L
	BS_MULTILINE        = 0x00002000L
	BS_NOTIFY           = 0x00004000L
	BS_FLAT             = 0x00008000L
	BS_RIGHTBUTTON      = BS_LEFTTEXT

# Listbox Styles
LBS_NOTIFY            = 0x0001L
LBS_SORT              = 0x0002L
LBS_NOREDRAW          = 0x0004L
LBS_MULTIPLESEL       = 0x0008L
LBS_OWNERDRAWFIXED    = 0x0010L
LBS_OWNERDRAWVARIABLE = 0x0020L
LBS_HASSTRINGS        = 0x0040L
LBS_USETABSTOPS       = 0x0080L
LBS_NOINTEGRALHEIGHT  = 0x0100L
LBS_MULTICOLUMN       = 0x0200L
LBS_WANTKEYBOARDINPUT = 0x0400L
LBS_EXTENDEDSEL       = 0x0800L
LBS_DISABLENOSCROLL   = 0x1000L
LBS_NODATA            = 0x2000L
if WINVER >= 0x0400:
	LBS_NOSEL             = 0x4000L
LBS_COMBOBOX          = 0x8000L
LBS_STANDARD          = LBS_NOTIFY | LBS_SORT | WS_VSCROLL | WS_BORDER

# Scroll Bar Styles
SBS_HORZ                    = 0x0000L
SBS_VERT                    = 0x0001L
SBS_TOPALIGN                = 0x0002L
SBS_LEFTALIGN               = 0x0002L
SBS_BOTTOMALIGN             = 0x0004L
SBS_RIGHTALIGN              = 0x0004L
SBS_SIZEBOXTOPLEFTALIGN     = 0x0002L
SBS_SIZEBOXBOTTOMRIGHTALIGN = 0x0004L
SBS_SIZEBOX                 = 0x0008L
if WINVER >= 0x0400:
	SBS_SIZEGRIP                = 0x0010L

ES_MULTILINE = 4
ES_AUTOVSCROLL = 0x40L
ES_AUTOHSCROLL = 0x80L
ES_READONLY    = 0x800
CP_ACP = 0
DS_SETFONT = 0x40
DS_MODALFRAME = 0x80

# User Button Notification Codes
BN_CLICKED          = 0
BN_PAINT            = 1
BN_HILITE           = 2
BN_UNHILITE         = 3
BN_DISABLE          = 4
BN_DOUBLECLICKED    = 5
if WINVER >= 0x0400:
	BN_PUSHED           = BN_HILITE
	BN_UNPUSHED         = BN_UNHILITE
	BN_DBLCLK           = BN_DOUBLECLICKED
	BN_SETFOCUS         = 6
	BN_KILLFOCUS        = 7

# Button Control Messages
BM_GETCHECK        = 0x00F0
BM_SETCHECK        = 0x00F1
BM_GETSTATE        = 0x00F2
BM_SETSTATE        = 0x00F3
BM_SETSTYLE        = 0x00F4
if WINVER >= 0x0400:
	BM_CLICK           = 0x00F5
	BM_GETIMAGE        = 0x00F6
	BM_SETIMAGE        = 0x00F7
if WINVER >= 0x0600:
	BM_SETDONTCLICK    = 0x00F8

BST_UNCHECKED      = 0x0000
BST_CHECKED        = 0x0001
BST_INDETERMINATE  = 0x0002
BST_PUSHED         = 0x0004
BST_FOCUS          = 0x0008

SYNCHRONIZE  = (0x00100000L)
STANDARD_RIGHTS_REQUIRED = (0x000F0000L)
EVENT_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED|SYNCHRONIZE|0x3)
MAX_PATH = 260

def GET_XY_LPARAM(lParam):
    x = LOWORD(lParam)
    if x > 32768:
        x = x - 65536
    y = HIWORD(lParam)
    if y > 32768:
        y = y - 65536
        
    return x, y 

def GET_POINT_LPARAM(lParam):
    x, y = GET_XY_LPARAM(lParam)
    return POINT(x, y)

FVIRTKEY  = 0x01
FNOINVERT = 0x02
FSHIFT    = 0x04
FCONTROL  = 0x08
FALT      = 0x10

def ValidHandle(value):
    if value == 0:
        raise WinError()
    else:
        return value

def Fail(value):
    if value == -1:
        raise WinError()
    else:
        return value

COLORREF = DWORD
LPCOLORREF = POINTER(COLORREF)

# The ZeroMemory function fills a block of memory with zeros
SIZE_T = c_ulong
def ZeroMemory(Destination, Length):
	memset(addressof(Destination), 0, Length)

PostQuitMessage= windll.user32.PostQuitMessage
GetDCEx = windll.user32.GetDCEx
GetDC = windll.user32.GetDC
ReleaseDC = windll.user32.ReleaseDC
DestroyIcon = windll.user32.DestroyIcon

RegisterClassEx = WINFUNCTYPE(c_void_p, POINTER(WNDCLASSEX))(('RegisterClassExW', windll.user32))
GetModuleHandle = WINFUNCTYPE(c_void_p, c_wchar_p)(('GetModuleHandleW', windll.kernel32))
DefWindowProc = WINFUNCTYPE(c_long, c_void_p, c_uint, c_uint, c_long)(('DefWindowProcW', windll.user32))
CallWindowProc = WINFUNCTYPE(c_long, c_void_p, c_void_p, c_uint, c_uint, c_long)(('CallWindowProcW', windll.user32))
CreateWindowEx = WINFUNCTYPE(ValidHandle, c_ulong, c_wchar_p, c_wchar_p, c_ulong, c_int, c_int, c_int, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(('CreateWindowExW', windll.user32))
CreateWindowEx_atom = WINFUNCTYPE(ValidHandle, c_ulong, c_void_p, c_wchar_p, c_ulong, c_int, c_int, c_int, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(('CreateWindowExW', windll.user32))
AppendMenu = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_uint, c_wchar_p)(('AppendMenuW', windll.user32))
GetMessage = WINFUNCTYPE(c_bool, c_void_p, c_void_p, c_uint, c_uint)(('GetMessageW', windll.user32))
SendMessage = WINFUNCTYPE(c_long, c_void_p, c_uint, c_uint, c_void_p)(('SendMessageW', windll.user32))
PostMessage = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_uint, c_long)(('PostMessageW', windll.user32))
DispatchMessage = WINFUNCTYPE(c_long, c_void_p)(('DispatchMessageW', windll.user32))
RegisterWindowMessage = windll.user32.RegisterWindowMessageW
SetWindowLong = windll.user32.SetWindowLongW
SetClassLong = windll.user32.SetClassLongW
GetClassLong = windll.user32.GetClassLongW
CreateAcceleratorTable = windll.user32.CreateAcceleratorTableW
ExpandEnvironmentStrings = windll.kernel32.ExpandEnvironmentStringsW
LoadLibrary = WINFUNCTYPE(c_void_p, c_wchar_p)(('LoadLibraryW', windll.kernel32))
FindResource = windll.kernel32.FindResourceW
FindWindow = windll.user32.FindWindowW
SetMenuItemInfo = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_bool, POINTER(MENUITEMINFO))(('SetMenuItemInfoW', windll.user32))
GetMenuItemInfo = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_bool, POINTER(MENUITEMINFO))(('GetMenuItemInfoW', windll.user32))
SetWindowsHookEx = windll.user32.SetWindowsHookExW
MessageBox = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_wchar_p, c_uint)(('MessageBoxW', windll.user32))
RegisterClipboardFormat = windll.user32.RegisterClipboardFormatW
DialogBoxParam = windll.user32.DialogBoxParamW
CreateDialogIndirectParam = windll.user32.CreateDialogIndirectParamW
DialogBoxIndirectParam = windll.user32.DialogBoxIndirectParamW
GetClassName = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_int)(('GetClassNameW', windll.user32))
GetClassInfo = WINFUNCTYPE(c_bool, c_void_p, c_wchar_p, c_void_p)(('GetClassInfoW', windll.user32))
CreateEvent = WINFUNCTYPE(c_void_p, c_void_p, c_bool, c_bool, c_wchar_p)(('CreateEventW', windll.kernel32))
OpenEvent = WINFUNCTYPE(c_void_p, c_ulong, c_bool, c_wchar_p)(('OpenEventW', windll.kernel32))
if not UNICODE:
	RegisterClassEx = WINFUNCTYPE(c_void_p, POINTER(WNDCLASSEX))(('RegisterClassExA', windll.user32))
	GetModuleHandle = WINFUNCTYPE(c_void_p, c_char_p)(('GetModuleHandleA', windll.kernel32))
	DefWindowProc = WINFUNCTYPE(c_long, c_void_p, c_uint, c_uint, c_long)(('DefWindowProcA', windll.user32))
	CallWindowProc = WINFUNCTYPE(c_long, c_void_p, c_void_p, c_uint, c_uint, c_long)(('CallWindowProcA', windll.user32))
	CreateWindowEx = CreateWindowEx_atom = windll.user32.CreateWindowExA
	AppendMenu = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_uint, c_char_p)(('AppendMenuA', windll.user32))
	GetMessage = WINFUNCTYPE(c_bool, c_void_p, c_void_p, c_uint, c_uint)(('GetMessageA', windll.user32))
	SendMessage = WINFUNCTYPE(c_long, c_void_p, c_uint, c_uint, c_void_p)(('SendMessageA', windll.user32))
	PostMessage = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_uint, c_long)(('PostMessageA', windll.user32))
	DispatchMessage = WINFUNCTYPE(c_long, c_void_p)(('DispatchMessageA', windll.user32))
	RegisterWindowMessage = windll.user32.RegisterWindowMessageA
	SetWindowLong = windll.user32.SetWindowLongA
	SetClassLong = windll.user32.SetClassLongA
	GetClassLong = windll.user32.GetClassLongA
	CreateAcceleratorTable = windll.user32.CreateAcceleratorTableA
	ExpandEnvironmentStrings = windll.kernel32.ExpandEnvironmentStringsA
	LoadLibrary = WINFUNCTYPE(c_void_p, c_char_p)(('LoadLibraryA', windll.kernel32))
	FindResource = windll.kernel32.FindResourceA
	FindWindow = windll.user32.FindWindowA
	SetMenuItemInfo = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_bool, POINTER(MENUITEMINFO))(('SetMenuItemInfoA', windll.user32))
	GetMenuItemInfo = WINFUNCTYPE(c_bool, c_void_p, c_uint, c_bool, POINTER(MENUITEMINFO))(('GetMenuItemInfoA', windll.user32))
	SetWindowsHookEx = windll.user32.SetWindowsHookExA
	MessageBox = WINFUNCTYPE(c_int, c_void_p, c_char_p, c_char_p, c_uint)(('MessageBoxA', windll.user32))
	RegisterClipboardFormat = windll.user32.RegisterClipboardFormatA
	DialogBoxParam = windll.user32.DialogBoxParamA
	CreateDialogIndirectParam = windll.user32.CreateDialogIndirectParamA
	DialogBoxIndirectParam = windll.user32.DialogBoxIndirectParamA
	GetClassName = WINFUNCTYPE(c_int, c_void_p, c_char_p, c_int)(('GetClassNameA', windll.user32))
	GetClassInfo = WINFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(('GetClassInfoA', windll.user32))
	CreateEvent = WINFUNCTYPE(c_void_p, c_void_p, c_bool, c_bool, c_char_p)(('CreateEventA', windll.kernel32))
	OpenEvent = WINFUNCTYPE(c_void_p, c_ulong, c_bool, c_char_p)(('OpenEventA', windll.kernel32))

GetMessagePos = windll.user32.GetMessagePos
BeginDeferWindowPos = windll.user32.BeginDeferWindowPos
DeferWindowPos = windll.user32.DeferWindowPos
EndDeferWindowPos = windll.user32.EndDeferWindowPos
DestroyAcceleratorTable = windll.user32.DestroyAcceleratorTable
TranslateAccelerator = windll.user32.TranslateAccelerator

GetForegroundWindow = windll.user32.GetForegroundWindow
ChildWindowFromPoint = windll.user32.ChildWindowFromPoint

TrackPopupMenuEx = windll.user32.TrackPopupMenuEx

GetMenuItemCount = windll.user32.GetMenuItemCount
GetMenuItemCount.restype = Fail
GetSubMenu = windll.user32.GetSubMenu

CallNextHookEx = windll.user32.CallNextHookEx
UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx

GetCurrentThreadId = windll.kernel32.GetCurrentThreadId

GetFocus = windll.user32.GetFocus

GlobalAlloc = windll.kernel32.GlobalAlloc
GlobalReAlloc = windll.kernel32.GlobalReAlloc
GlobalLock = windll.kernel32.GlobalLock
GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalFree = windll.kernel32.GlobalFree
#~ GlobalDiscard = windll.kernel32.GlobalDiscard
GlobalFlags = windll.kernel32.GlobalFlags
GlobalHandle = windll.kernel32.GlobalHandle
GlobalSize = windll.kernel32.GlobalSize

GetCurrentThreadId = WINFUNCTYPE(DWORD)(('GetCurrentThreadId', windll.kernel32))

LocalAlloc = windll.kernel32.LocalAlloc
LocalReAlloc = windll.kernel32.LocalReAlloc
LocalLock = windll.kernel32.LocalLock
LocalUnlock = windll.kernel32.LocalUnlock
LocalFree = windll.kernel32.LocalFree
#~ LocalDiscard = windll.kernel32.LocalDiscard
LocalFlags = windll.kernel32.LocalFlags
LocalHandle = windll.kernel32.LocalHandle
LocalSize = windll.kernel32.LocalSize

OpenClipboard = windll.user32.OpenClipboard
EmptyClipboard = windll.user32.EmptyClipboard
SetClipboardData = windll.user32.SetClipboardData
GetClipboardData = windll.user32.GetClipboardData
CloseClipboard = windll.user32.CloseClipboard
EnumClipboardFormats = windll.user32.EnumClipboardFormats
IsClipboardFormatAvailable = windll.user32.IsClipboardFormatAvailable
GetDlgItem = windll.user32.GetDlgItem
EndDialog = windll.user32.EndDialog
ShowScrollBar = windll.user32.ShowScrollBar
GetDesktopWindow = windll.user32.GetDesktopWindow
SetFocus = windll.user32.SetFocus
MultiByteToWideChar = windll.kernel32.MultiByteToWideChar
EnumChildWindows = windll.user32.EnumChildWindows
GetMenu = windll.user32.GetMenu

SetTimer = windll.user32.SetTimer
KillTimer = windll.user32.KillTimer

IsWindowVisible = windll.user32.IsWindowVisible
IsIconic = windll.user32.IsIconic
GetCursorPos = windll.user32.GetCursorPos
SetForegroundWindow = windll.user32.SetForegroundWindow
SetMenuDefaultItem = windll.user32.SetMenuDefaultItem

LockWindowUpdate = windll.user32.LockWindowUpdate

# RedrawWindow() flags
RDW_INVALIDATE         = 0x0001
RDW_INTERNALPAINT      = 0x0002
RDW_ERASE              = 0x0004
RDW_VALIDATE           = 0x0008
RDW_NOINTERNALPAINT    = 0x0010
RDW_NOERASE            = 0x0020
RDW_NOCHILDREN         = 0x0040
RDW_ALLCHILDREN        = 0x0080
RDW_UPDATENOW          = 0x0100
RDW_ERASENOW           = 0x0200
RDW_FRAME              = 0x0400
RDW_NOFRAME            = 0x0800
RedrawWindow = WINFUNCTYPE(c_byte, HWND, POINTER(RECT), HRGN, c_uint)(('RedrawWindow', windll.user32))
