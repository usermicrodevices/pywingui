'WinUser.h implementation'

RC_INVOKED = True

from windows import *
try:
	WINVER = _WIN32_WINNT
except:
	_WIN32_WINNT = WINVER

# IS_INTRESOURCE and MAKEINTRESOURCE code from pyWinLite project, author Vincent Povirk (2008)
def IS_INTRESOURCE(i):
	try:
		return i.value|0xFFFF == 0xFFFF
	except AttributeError:
		return i|0xFFFF == 0xFFFF
if UNICODE:
	def MAKEINTRESOURCE(i):#MAKEINTRESOURCEW
		return cast(c_void_p(i&0xFFFF), c_wchar_p)
else:
	def MAKEINTRESOURCE(i):#MAKEINTRESOURCEA
		return cast(c_void_p(i&0xFFFF), c_char_p)

# ========================
# some constants from WinUser.h

#Special HWND value for use with PostMessage() and SendMessage()
HWND_BROADCAST = 0xffff
if WINVER >= 0x0500:
	HWND_MESSAGE = -3

#Virtual Keys, Standard Set
VK_LBUTTON = 0x01
VK_RBUTTON = 0x02
VK_CANCEL = 0x03
VK_MBUTTON = 0x04# NOT contiguous with L & RBUTTON
if WINVER >= 0x0500:
	VK_XBUTTON1 = 0x05#NOT contiguous with L & RBUTTON
	VK_XBUTTON2 = 0x06#NOT contiguous with L & RBUTTON
VK_BACK = 0x08
VK_TAB = 0x09
VK_CLEAR = 0x0C
VK_RETURN = 0x0D
VK_SHIFT = 0x10
VK_CONTROL = 0x11
VK_MENU =  0x12
VK_PAUSE = 0x13
VK_CAPITAL = 0x14
VK_KANA = 0x15
VK_HANGEUL = 0x15#old name - should be here for compatibility
VK_HANGUL = 0x15
VK_JUNJA = 0x17
VK_FINAL = 0x18
VK_HANJA = 0x19
VK_KANJI = 0x19
VK_ESCAPE = 0x1B
VK_CONVERT = 0x1C
VK_NONCONVERT = 0x1D
VK_ACCEPT = 0x1E
VK_MODECHANGE = 0x1F
VK_SPACE = 0x20
VK_PRIOR = 0x21
VK_NEXT = 0x22
VK_END = 0x23
VK_HOME = 0x24
VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_SELECT = 0x29
VK_PRINT = 0x2A
VK_EXECUTE = 0x2B
VK_SNAPSHOT = 0x2C
VK_INSERT = 0x2D
VK_DELETE = 0x2E
VK_HELP = 0x2F
VK_0 = 0x30
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_6 = 0x36
VK_7 = 0x37
VK_8 = 0x38
VK_9 = 0x39
#0x40 : unassigned
#VK_A - VK_Z are the same as ASCII 'A' - 'Z' (0x41 - 0x5A)
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_I = 0x49
VK_J = 0x4A
VK_K = 0x4B
VK_L = 0x4C
VK_M = 0x4D
VK_N = 0x4E
VK_O = 0x4F
VK_P = 0x50
VK_Q = 0x51
VK_R = 0x52
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_V = 0x56
VK_W = 0x57
VK_X = 0x58
VK_Y = 0x59
VK_Z = 0x5A
VK_LWIN = 0x5B
VK_RWIN = 0x5C
VK_APPS = 0x5D
VK_SLEEP = 0x5F
VK_NUMPAD0 = 0x60
VK_NUMPAD1 = 0x61
VK_NUMPAD2 = 0x62
VK_NUMPAD3 = 0x63
VK_NUMPAD4 = 0x64
VK_NUMPAD5 = 0x65
VK_NUMPAD6 = 0x66
VK_NUMPAD7 = 0x67
VK_NUMPAD8 = 0x68
VK_NUMPAD9 = 0x69
VK_MULTIPLY = 0x6A
VK_ADD = 0x6B
VK_SEPARATOR = 0x6C
VK_SUBTRACT = 0x6D
VK_DECIMAL = 0x6E
VK_DIVIDE = 0x6F
VK_F1 = 0x70
VK_F2 = 0x71
VK_F3 = 0x72
VK_F4 = 0x73
VK_F5 = 0x74
VK_F6 = 0x75
VK_F7 = 0x76
VK_F8 = 0x77
VK_F9 = 0x78
VK_F10 = 0x79
VK_F11 = 0x7A
VK_F12 = 0x7B
VK_F13 = 0x7C
VK_F14 = 0x7D
VK_F15 = 0x7E
VK_F16 = 0x7F
VK_F17 = 0x80
VK_F18 = 0x81
VK_F19 = 0x82
VK_F20 = 0x83
VK_F21 = 0x84
VK_F22 = 0x85
VK_F23 = 0x86
VK_F24 = 0x87
VK_NUMLOCK = 0x90
VK_SCROLL = 0x91
VK_OEM_NEC_EQUAL = 0x92#'=' key on numpad
VK_OEM_FJ_JISHO = 0x92#'Dictionary' key
VK_OEM_FJ_MASSHOU = 0x93#'Unregister word' key
VK_OEM_FJ_TOUROKU = 0x94#'Register word' key
VK_OEM_FJ_LOYA = 0x95#'Left OYAYUBI' key
VK_OEM_FJ_ROYA = 0x96#'Right OYAYUBI' key

#VK_L* & VK_R* - left and right Alt, Ctrl and Shift virtual keys.
#Used only as parameters to GetAsyncKeyState() and GetKeyState().
#No other API or message will distinguish left and right keys in this way.
VK_LSHIFT = 0xA0
VK_RSHIFT = 0xA1
VK_LCONTROL = 0xA2
VK_RCONTROL = 0xA3
VK_LMENU = 0xA4
VK_RMENU = 0xA5

if WINVER >= 0x0500:
	VK_BROWSER_BACK = 0xA6
	VK_BROWSER_FORWARD = 0xA7
	VK_BROWSER_REFRESH = 0xA8
	VK_BROWSER_STOP = 0xA9
	VK_BROWSER_SEARCH = 0xAA
	VK_BROWSER_FAVORITES = 0xAB
	VK_BROWSER_HOME = 0xAC
	VK_VOLUME_MUTE = 0xAD
	VK_VOLUME_DOWN = 0xAE
	VK_VOLUME_UP = 0xAF
	VK_MEDIA_NEXT_TRACK = 0xB0
	VK_MEDIA_PREV_TRACK = 0xB1
	VK_MEDIA_STOP = 0xB2
	VK_MEDIA_PLAY_PAUSE = 0xB3
	VK_LAUNCH_MAIL = 0xB4
	VK_LAUNCH_MEDIA_SELECT = 0xB5
	VK_LAUNCH_APP1 = 0xB6
	VK_LAUNCH_APP2 = 0xB7

VK_OEM_1 = 0xBA#';:' for US
VK_OEM_PLUS = 0xBB#'+' any country
VK_OEM_COMMA = 0xBC#',' any country
VK_OEM_MINUS = 0xBD#'-' any country
VK_OEM_PERIOD = 0xBE#'.' any country
VK_OEM_2 = 0xBF#'/?' for US
VK_OEM_3 = 0xC0#'`~' for US
VK_OEM_4 = 0xDB#'[{' for US
VK_OEM_5 = 0xDC#'\|' for US
VK_OEM_6 = 0xDD#']}' for US
VK_OEM_7 = 0xDE#''"' for US
VK_OEM_8 = 0xDF
VK_OEM_AX = 0xE1#'AX' key on Japanese AX kbd
VK_OEM_102 = 0xE2#"<>" or "\|" on RT 102-key kbd.
VK_ICO_HELP = 0xE3#Help key on ICO
VK_ICO_00 = 0xE4#00 key on ICO
if WINVER >= 0x0400:
	VK_PROCESSKEY = 0xE5
VK_ICO_CLEAR = 0xE6
if WINVER >= 0x0500:
	VK_PACKET = 0xE7

#Nokia/Ericsson definitions
VK_OEM_RESET = 0xE9
VK_OEM_JUMP = 0xEA
VK_OEM_PA1 = 0xEB
VK_OEM_PA2 = 0xEC
VK_OEM_PA3 = 0xED
VK_OEM_WSCTRL = 0xEE
VK_OEM_CUSEL = 0xEF
VK_OEM_ATTN = 0xF0
VK_OEM_FINISH = 0xF1
VK_OEM_COPY = 0xF2
VK_OEM_AUTO = 0xF3
VK_OEM_ENLW = 0xF4
VK_OEM_BACKTAB = 0xF5
VK_ATTN = 0xF6
VK_CRSEL = 0xF7
VK_EXSEL = 0xF8
VK_EREOF = 0xF9
VK_PLAY = 0xFA
VK_ZOOM = 0xFB
VK_NONAME = 0xFC
VK_PA1 = 0xFD
VK_OEM_CLEAR = 0xFE

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
if _WIN32_WINNT >= 0x0500:
	KEYEVENTF_UNICODE = 0x0004
	KEYEVENTF_SCANCODE = 0x0008

#Window Messages

WM_NULL = 0x0000
WM_CREATE = 0x0001
WM_DESTROY = 0x0002
WM_MOVE = 0x0003
WM_SIZE = 0x0005

WM_ACTIVATE = 0x0006
#WM_ACTIVATE state values
WA_INACTIVE = 0
WA_ACTIVE = 1
WA_CLICKACTIVE = 2

WM_SETFOCUS = 0x0007
WM_KILLFOCUS = 0x0008
WM_ENABLE = 0x000A
WM_SETREDRAW = 0x000B
WM_SETTEXT = 0x000C
WM_GETTEXT = 0x000D
WM_GETTEXTLENGTH = 0x000E
WM_PAINT = 0x000F
WM_CLOSE = 0x0010
WM_QUIT = 0x0012
WM_ERASEBKGND = 0x0014
WM_SYSCOLORCHANGE = 0x0015
WM_SHOWWINDOW = 0x0018
WM_WININICHANGE = 0x001A
if WINVER >= 0x0400:
	WM_SETTINGCHANGE = WM_WININICHANGE

WM_DEVMODECHANGE = 0x001B
WM_ACTIVATEAPP = 0x001C
WM_FONTCHANGE = 0x001D
WM_TIMECHANGE = 0x001E
WM_CANCELMODE = 0x001F
WM_SETCURSOR = 0x0020
WM_MOUSEACTIVATE = 0x0021
WM_CHILDACTIVATE = 0x0022
WM_QUEUESYNC = 0x0023

WM_PAINTICON = 0x0026
WM_ICONERASEBKGND = 0x0027
WM_NEXTDLGCTL = 0x0028
WM_SPOOLERSTATUS = 0x002A
WM_DRAWITEM = 0x002B
WM_MEASUREITEM = 0x002C
WM_DELETEITEM = 0x002D
WM_VKEYTOITEM = 0x002E
WM_CHARTOITEM = 0x002F
WM_SETFONT = 0x0030
WM_GETFONT = 0x0031
WM_SETHOTKEY = 0x0032
WM_GETHOTKEY = 0x0033
WM_QUERYDRAGICON = 0x0037
WM_COMPAREITEM = 0x0039
WM_COMPACTING = 0x0041
WM_COMMNOTIFY = 0x0044#no longer suported
WM_WINDOWPOSCHANGING = 0x0046
WM_WINDOWPOSCHANGED = 0x0047

WM_POWER = 0x0048
 #wParam for WM_POWER window message and DRV_POWER driver notification
PWR_OK = 1
PWR_FAIL = (-1)
PWR_SUSPENDREQUEST = 1
PWR_SUSPENDRESUME = 2
PWR_CRITICALRESUME = 3

WM_COPYDATA = 0x004A
WM_CANCELJOURNAL = 0x004B

if WINVER >= 0x0400:
	WM_NOTIFY = 0x004E
	WM_INPUTLANGCHANGEREQUEST = 0x0050
	WM_INPUTLANGCHANGE = 0x0051
	WM_TCARD = 0x0052
	WM_HELP = 0x0053
	WM_USERCHANGED = 0x0054
	WM_NOTIFYFORMAT = 0x0055
	NFR_ANSI = 1
	NFR_UNICODE = 2
	NF_QUERY = 3
	NF_REQUERY = 4
	WM_CONTEXTMENU = 0x007B
	WM_STYLECHANGING = 0x007C
	WM_STYLECHANGED = 0x007D
	WM_DISPLAYCHANGE = 0x007E
	WM_GETICON = 0x007F
	WM_SETICON = 0x0080

WM_NCCREATE = 0x0081
WM_NCDESTROY = 0x0082
WM_NCCALCSIZE = 0x0083
WM_NCHITTEST = 0x0084
WM_NCPAINT = 0x0085
WM_NCACTIVATE = 0x0086
WM_GETDLGCODE = 0x0087
WM_NCMOUSEMOVE = 0x00A0
WM_NCLBUTTONDOWN = 0x00A1
WM_NCLBUTTONUP = 0x00A2
WM_NCLBUTTONDBLCLK = 0x00A3
WM_NCRBUTTONDOWN = 0x00A4
WM_NCRBUTTONUP = 0x00A5
WM_NCRBUTTONDBLCLK = 0x00A6
WM_NCMBUTTONDOWN = 0x00A7
WM_NCMBUTTONUP = 0x00A8
WM_NCMBUTTONDBLCLK = 0x00A9

if _WIN32_WINNT >= 0x0500:
	WM_NCXBUTTONDOWN = 0x00AB
	WM_NCXBUTTONUP = 0x00AC
	WM_NCXBUTTONDBLCLK = 0x00AD

if _WIN32_WINNT >= 0x0501:
	WM_INPUT_DEVICE_CHANGE = 0x00FE
	WM_INPUT = 0x00FF

WM_KEYFIRST = 0x0100
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_CHAR = 0x0102
WM_DEADCHAR = 0x0103
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105
WM_SYSCHAR = 0x0106
WM_SYSDEADCHAR = 0x0107
if _WIN32_WINNT >= 0x0501:
	WM_UNICHAR = 0x0109
	WM_KEYLAST = 0x0109
	UNICODE_NOCHAR = 0xFFFF
else:
	WM_KEYLAST = 0x0108

if WINVER >= 0x0400:
	WM_IME_STARTCOMPOSITION = 0x010D
	WM_IME_ENDCOMPOSITION = 0x010E
	WM_IME_COMPOSITION = 0x010F
	WM_IME_KEYLAST = 0x010F

WM_INITDIALOG = 0x0110
WM_COMMAND = 0x0111
WM_SYSCOMMAND = 0x0112
WM_TIMER = 0x0113
WM_HSCROLL = 0x0114
WM_VSCROLL = 0x0115
WM_INITMENU = 0x0116
WM_INITMENUPOPUP = 0x0117
WM_MENUSELECT = 0x011F
WM_MENUCHAR = 0x0120
WM_ENTERIDLE = 0x0121

IMAGE_BITMAP = 0
IMAGE_ICON = 1
IMAGE_CURSOR = 2
if WINVER >= 0x0400:
	IMAGE_ENHMETAFILE  = 3

	LR_DEFAULTCOLOR = 0x00000000
	LR_MONOCHROME = 0x00000001
	LR_COLOR = 0x00000002
	LR_COPYRETURNORG = 0x00000004
	LR_COPYDELETEORG = 0x00000008
	LR_LOADFROMFILE = 0x00000010
	LR_LOADTRANSPARENT = 0x00000020
	LR_DEFAULTSIZE = 0x00000040
	LR_VGACOLOR = 0x00000080
	LR_LOADMAP3DCOLORS = 0x00001000
	LR_CREATEDIBSECTION = 0x00002000
	LR_COPYFROMRESOURCE = 0x00004000
	LR_SHARED = 0x00008000

	DI_MASK = 0x0001
	DI_IMAGE = 0x0002
	DI_NORMAL = 0x0003
	DI_COMPAT = 0x0004
	DI_DEFAULTSIZE = 0x0008
	if WINVER >= 0x0501:
		DI_NOMIRROR = 0x0010

	RES_ICON = 1
	RES_CURSOR = 2


# OEM Resource Ordinal Numbers
# OEM bitmaps
OBM_CLOSE = 32754
OBM_UPARROW = 32753
OBM_DNARROW = 32752
OBM_RGARROW = 32751
OBM_LFARROW = 32750
OBM_REDUCE = 32749
OBM_ZOOM = 32748
OBM_RESTORE = 32747
OBM_REDUCED = 32746
OBM_ZOOMD = 32745
OBM_RESTORED = 32744
OBM_UPARROWD = 32743
OBM_DNARROWD = 32742
OBM_RGARROWD = 32741
OBM_LFARROWD = 32740
OBM_MNARROW = 32739
OBM_COMBO = 32738
OBM_UPARROWI = 32737
OBM_DNARROWI = 32736
OBM_RGARROWI = 32735
OBM_LFARROWI = 32734

OBM_OLD_CLOSE = 32767
OBM_SIZE = 32766
OBM_OLD_UPARROW = 32765
OBM_OLD_DNARROW = 32764
OBM_OLD_RGARROW = 32763
OBM_OLD_LFARROW = 32762
OBM_BTSIZE = 32761
OBM_CHECK = 32760
OBM_CHECKBOXES = 32759
OBM_BTNCORNERS = 32758
OBM_OLD_REDUCE = 32757
OBM_OLD_ZOOM = 32756
OBM_OLD_RESTORE = 32755

# OEM cursors
OCR_NORMAL = 32512
OCR_IBEAM = 32513
OCR_WAIT = 32514
OCR_CROSS = 32515
OCR_UP = 32516
OCR_SIZE = 32640# OBSOLETE: use OCR_SIZEALL */
OCR_ICON = 32641# OBSOLETE: use OCR_NORMAL */
OCR_SIZENWSE = 32642
OCR_SIZENESW = 32643
OCR_SIZEWE = 32644
OCR_SIZENS = 32645
OCR_SIZEALL = 32646
OCR_ICOCUR = 32647# OBSOLETE: use OIC_WINLOGO */
OCR_NO = 32648
if WINVER >= 0x0500:
	OCR_HAND = 32649
if WINVER >= 0x0400:
	OCR_APPSTARTING = 32650

# OEM icons
OIC_SAMPLE = 32512
OIC_HAND = 32513
OIC_QUES = 32514
OIC_BANG = 32515
OIC_NOTE = 32516
if WINVER >= 0x0400:
	OIC_WINLOGO = 32517
	OIC_WARNING = OIC_BANG
	OIC_ERROR = OIC_HAND
	OIC_INFORMATION = OIC_NOTE
if WINVER >= 0x0600:
	OIC_SHIELD = 32518

# Standard Icon IDs
if RC_INVOKED:
	IDI_APPLICATION = 32512
	IDI_HAND = 32513
	IDI_QUESTION = 32514
	IDI_EXCLAMATION = 32515
	IDI_ASTERISK = 32516
	if WINVER >= 0x0400:
		IDI_WINLOGO = 32517
	if WINVER >= 0x0600:
		IDI_SHIELD = 32518
else:
	IDI_APPLICATION = MAKEINTRESOURCE(32512)
	IDI_HAND = MAKEINTRESOURCE(32513)
	IDI_QUESTION = MAKEINTRESOURCE(32514)
	IDI_EXCLAMATION = MAKEINTRESOURCE(32515)
	IDI_ASTERISK = MAKEINTRESOURCE(32516)
	if WINVER >= 0x0400:
		IDI_WINLOGO = MAKEINTRESOURCE(32517)
	if WINVER >= 0x0600:
		IDI_SHIELD = MAKEINTRESOURCE(32518)

if WINVER >= 0x0400:
	IDI_WARNING = IDI_EXCLAMATION
	IDI_ERROR = IDI_HAND
	IDI_INFORMATION = IDI_ASTERISK

if UNICODE:
	SetWindowText = WINFUNCTYPE(c_bool, c_void_p, c_wchar_p)(('SetWindowTextW', windll.user32))
	GetWindowText = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GetWindowTextW', windll.user32))
	GetWindowTextLength = WINFUNCTYPE(c_int, c_void_p)(('GetWindowTextLengthW', windll.user32))
	#~ LoadIcon = WINFUNCTYPE(HICON, HINSTANCE, c_wchar_p)(('LoadIconW', windll.user32))
	_LoadIcon = WINFUNCTYPE(c_void_p, c_void_p, c_wchar_p)(('LoadIconW', windll.user32))
	_LoadIconP = windll.user32.LoadIconW
	_LoadCursor = WINFUNCTYPE(c_void_p, c_void_p, c_wchar_p)(('LoadCursorW', windll.user32))
	_LoadCursorP = windll.user32.LoadCursorW
	LoadCursorFromFile = WINFUNCTYPE(c_void_p, c_wchar_p)(('LoadCursorFromFileW', windll.user32))
	_LoadImage = WINFUNCTYPE(c_void_p, c_void_p, c_wchar_p, c_uint, c_int, c_int, c_uint)(('LoadImageW', windll.user32))
	_LoadImageP = windll.user32.LoadImageW
	MapVirtualKey = WINFUNCTYPE(c_uint, c_uint, c_uint)(('MapVirtualKeyW', windll.user32))
else:
	SetWindowText = WINFUNCTYPE(c_bool, c_void_p, c_char_p)(('SetWindowTextA', windll.user32))
	GetWindowText = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GetWindowTextA', windll.user32))
	GetWindowTextLength = WINFUNCTYPE(c_int, c_void_p)(('GetWindowTextLengthA', windll.user32))
	#~ LoadIcon = WINFUNCTYPE(HICON, HINSTANCE, c_char_p)(('LoadIconA', windll.user32))
	_LoadIcon = WINFUNCTYPE(c_void_p, c_void_p, c_char_p)(('LoadIconA', windll.user32))
	_LoadIconP = windll.user32.LoadIconA
	_LoadCursor = WINFUNCTYPE(c_void_p, c_void_p, c_char_p)(('LoadCursorA', windll.user32))
	_LoadCursorP = windll.user32.LoadCursorA
	LoadCursorFromFile = WINFUNCTYPE(c_void_p, c_char_p)(('LoadCursorFromFileA', windll.user32))
	_LoadImage = WINFUNCTYPE(c_void_p, c_void_p, c_char_p, c_uint, c_int, c_int, c_uint)(('LoadImageA', windll.user32))
	_LoadImageP = windll.user32.LoadImageA
	MapVirtualKey = WINFUNCTYPE(c_uint, c_uint, c_uint)(('MapVirtualKeyA', windll.user32))

CreateIcon = WINFUNCTYPE(HICON, HINSTANCE, c_int, c_int, c_byte, c_byte, c_void_p, c_void_p)(('CreateIcon', windll.user32))

#WINUSERAPI int WINAPI ExcludeUpdateRgn(__in HDC hDC, __in HWND hWnd);
ExcludeUpdateRgn = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('ExcludeUpdateRgn', windll.user32))

InvalidateRect = WINFUNCTYPE(c_bool, c_void_p, POINTER(RECT), c_bool)(('InvalidateRect', windll.user32))
InvalidateRgn = WINFUNCTYPE(c_bool, c_void_p, c_void_p, c_bool)(('InvalidateRect', windll.user32))
ValidateRect = WINFUNCTYPE(c_bool, c_void_p, POINTER(RECT))(('ValidateRect', windll.user32))
ValidateRgn = WINFUNCTYPE(c_bool, c_void_p, c_void_p)(('ValidateRgn', windll.user32))

#Static Control Constants
SS_LEFT = 0x00000000L
#~ SS_SIMPLE = 0x0000000BL
SS_SIMPLE = 0x0000000B

def LoadIcon(hInstance = None, file_or_resource = 0):
	if isinstance(file_or_resource,  int):
		return _LoadIconP(hInstance, file_or_resource)
	else:
		return _LoadIcon(hInstance, file_or_resource)

def LoadCursor(hInstance = None, file_or_resource = 0):
	if isinstance(file_or_resource,  int):
		return _LoadCursorP(hInstance, file_or_resource)
	else:
		return _LoadCursor(hInstance, file_or_resource)

def LoadImage(hInstance = None, file_or_resource = 0, img_type = 0, x = 0, y = 0, uFlags = 0):
	if isinstance(file_or_resource,  int):
		return _LoadImageP(hInstance, file_or_resource, img_type, x, y, uFlags)
	else:
		return _LoadImage(hInstance, file_or_resource, img_type, x, y, uFlags)

AttachThreadInput = WINFUNCTYPE(c_bool, c_void_p, c_void_p, c_bool)(('AttachThreadInput', windll.user32))
GetWindowThreadProcessId = WINFUNCTYPE(DWORD, c_void_p, c_void_p)(('GetWindowThreadProcessId', windll.user32))

MoveWindow = WINFUNCTYPE(c_bool, c_void_p, c_int, c_int, c_int, c_int, c_bool)(('MoveWindow', windll.user32))

keybd_event = WINFUNCTYPE(None, BYTE, BYTE, DWORD, ULONG_PTR)(('keybd_event', windll.user32))

SetCursor = windll.user32.SetCursor

ShowWindow = windll.user32.ShowWindow
UpdateWindow = windll.user32.UpdateWindow
TranslateMessage = windll.user32.TranslateMessage
GetWindowRect = windll.user32.GetWindowRect
DestroyWindow = windll.user32.DestroyWindow
CloseWindow = windll.user32.CloseWindow
CreateMenu = windll.user32.CreateMenu
CreatePopupMenu = windll.user32.CreatePopupMenu
DestroyMenu = windll.user32.DestroyMenu
EnableMenuItem = windll.user32.EnableMenuItem
GetClientRect = windll.user32.GetClientRect
GetWindowRect = windll.user32.GetWindowRect
IsDialogMessage = windll.user32.IsDialogMessage
GetParent = windll.user32.GetParent
SetWindowPos = windll.user32.SetWindowPos
BeginPaint = windll.user32.BeginPaint
EndPaint = windll.user32.EndPaint
SetCapture = windll.user32.SetCapture
GetCapture = windll.user32.GetCapture
ReleaseCapture = windll.user32.ReleaseCapture
ScreenToClient = windll.user32.ScreenToClient
ClientToScreen = windll.user32.ClientToScreen
