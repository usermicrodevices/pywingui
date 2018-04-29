'WinUser.h implementation'

RC_INVOKED = True

from windows import *

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

IMAGE_BITMAP       = 0
IMAGE_ICON         = 1
IMAGE_CURSOR       = 2
if WINVER >= 0x0400:
	IMAGE_ENHMETAFILE  = 3

	LR_DEFAULTCOLOR     = 0x00000000
	LR_MONOCHROME       = 0x00000001
	LR_COLOR            = 0x00000002
	LR_COPYRETURNORG    = 0x00000004
	LR_COPYDELETEORG    = 0x00000008
	LR_LOADFROMFILE     = 0x00000010
	LR_LOADTRANSPARENT  = 0x00000020
	LR_DEFAULTSIZE      = 0x00000040
	LR_VGACOLOR         = 0x00000080
	LR_LOADMAP3DCOLORS  = 0x00001000
	LR_CREATEDIBSECTION = 0x00002000
	LR_COPYFROMRESOURCE = 0x00004000
	LR_SHARED           = 0x00008000

	DI_MASK        = 0x0001
	DI_IMAGE       = 0x0002
	DI_NORMAL      = 0x0003
	DI_COMPAT      = 0x0004
	DI_DEFAULTSIZE = 0x0008
	if WINVER >= 0x0501:
		DI_NOMIRROR = 0x0010

	RES_ICON   = 1
	RES_CURSOR = 2


# OEM Resource Ordinal Numbers
# OEM bitmaps
OBM_CLOSE          = 32754
OBM_UPARROW        = 32753
OBM_DNARROW        = 32752
OBM_RGARROW        = 32751
OBM_LFARROW        = 32750
OBM_REDUCE         = 32749
OBM_ZOOM           = 32748
OBM_RESTORE        = 32747
OBM_REDUCED        = 32746
OBM_ZOOMD          = 32745
OBM_RESTORED       = 32744
OBM_UPARROWD       = 32743
OBM_DNARROWD       = 32742
OBM_RGARROWD       = 32741
OBM_LFARROWD       = 32740
OBM_MNARROW        = 32739
OBM_COMBO          = 32738
OBM_UPARROWI       = 32737
OBM_DNARROWI       = 32736
OBM_RGARROWI       = 32735
OBM_LFARROWI       = 32734

OBM_OLD_CLOSE      = 32767
OBM_SIZE           = 32766
OBM_OLD_UPARROW    = 32765
OBM_OLD_DNARROW    = 32764
OBM_OLD_RGARROW    = 32763
OBM_OLD_LFARROW    = 32762
OBM_BTSIZE         = 32761
OBM_CHECK          = 32760
OBM_CHECKBOXES     = 32759
OBM_BTNCORNERS     = 32758
OBM_OLD_REDUCE     = 32757
OBM_OLD_ZOOM       = 32756
OBM_OLD_RESTORE    = 32755

# OEM cursors
OCR_NORMAL         = 32512
OCR_IBEAM          = 32513
OCR_WAIT           = 32514
OCR_CROSS          = 32515
OCR_UP             = 32516
OCR_SIZE           = 32640   # OBSOLETE: use OCR_SIZEALL */
OCR_ICON           = 32641   # OBSOLETE: use OCR_NORMAL */
OCR_SIZENWSE       = 32642
OCR_SIZENESW       = 32643
OCR_SIZEWE         = 32644
OCR_SIZENS         = 32645
OCR_SIZEALL        = 32646
OCR_ICOCUR         = 32647   # OBSOLETE: use OIC_WINLOGO */
OCR_NO             = 32648
if WINVER >= 0x0500:
	OCR_HAND       = 32649
if WINVER >= 0x0400:
	OCR_APPSTARTING = 32650

# OEM icons
OIC_SAMPLE         = 32512
OIC_HAND           = 32513
OIC_QUES           = 32514
OIC_BANG           = 32515
OIC_NOTE           = 32516
if WINVER >= 0x0400:
	OIC_WINLOGO    = 32517
	OIC_WARNING    = OIC_BANG
	OIC_ERROR      = OIC_HAND
	OIC_INFORMATION = OIC_NOTE
if WINVER >= 0x0600:
	OIC_SHIELD     = 32518


# Standard Icon IDs
if RC_INVOKED:
	IDI_APPLICATION    = 32512
	IDI_HAND           = 32513
	IDI_QUESTION       = 32514
	IDI_EXCLAMATION    = 32515
	IDI_ASTERISK       = 32516
	if WINVER >= 0x0400:
		IDI_WINLOGO    = 32517
	if WINVER >= 0x0600:
		IDI_SHIELD     = 32518
else:
	IDI_APPLICATION    = MAKEINTRESOURCE(32512)
	IDI_HAND           = MAKEINTRESOURCE(32513)
	IDI_QUESTION       = MAKEINTRESOURCE(32514)
	IDI_EXCLAMATION    = MAKEINTRESOURCE(32515)
	IDI_ASTERISK       = MAKEINTRESOURCE(32516)
	if WINVER >= 0x0400:
		IDI_WINLOGO    = MAKEINTRESOURCE(32517)
	if WINVER >= 0x0600:
		IDI_SHIELD     = MAKEINTRESOURCE(32518)

if WINVER >= 0x0400:
	IDI_WARNING     = IDI_EXCLAMATION
	IDI_ERROR       = IDI_HAND
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
