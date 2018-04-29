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

#TODO wrap shBrowseForFolder directory selection dialog

# Common dialog error return codes
CDERR_DIALOGFAILURE    = 0xFFFF
CDERR_GENERALCODES     = 0x0000
CDERR_STRUCTSIZE       = 0x0001
CDERR_INITIALIZATION   = 0x0002
CDERR_NOTEMPLATE       = 0x0003
CDERR_NOHINSTANCE      = 0x0004
CDERR_LOADSTRFAILURE   = 0x0005
CDERR_FINDRESFAILURE   = 0x0006
CDERR_LOADRESFAILURE   = 0x0007
CDERR_LOCKRESFAILURE   = 0x0008
CDERR_MEMALLOCFAILURE  = 0x0009
CDERR_MEMLOCKFAILURE   = 0x000A
CDERR_NOHOOK           = 0x000B
CDERR_REGISTERMSGFAIL  = 0x000C
PDERR_PRINTERCODES     = 0x1000
PDERR_SETUPFAILURE     = 0x1001
PDERR_PARSEFAILURE     = 0x1002
PDERR_RETDEFFAILURE    = 0x1003
PDERR_LOADDRVFAILURE   = 0x1004
PDERR_GETDEVMODEFAIL   = 0x1005
PDERR_INITFAILURE      = 0x1006
PDERR_NODEVICES        = 0x1007
PDERR_NODEFAULTPRN     = 0x1008
PDERR_DNDMMISMATCH     = 0x1009
PDERR_CREATEICFAILURE  = 0x100A
PDERR_PRINTERNOTFOUND  = 0x100B
PDERR_DEFAULTDIFFERENT = 0x100C
CFERR_CHOOSEFONTCODES  = 0x2000
CFERR_NOFONTS          = 0x2001
CFERR_MAXLESSTHANMIN   = 0x2002
FNERR_FILENAMECODES    = 0x3000
FNERR_SUBCLASSFAILURE  = 0x3001
FNERR_INVALIDFILENAME  = 0x3002
FNERR_BUFFERTOOSMALL   = 0x3003
FRERR_FINDREPLACECODES = 0x4000
FRERR_BUFFERLENGTHZERO = 0x4001
CCERR_CHOOSECOLORCODES = 0x5000

from ctypes import *
from windows import *
from wtl import *
#~ from version_microsoft import WINVER, UNICODE

# UINT_PTR CALLBACK OFNHookProc(
# HWND hdlg,      // handle to child dialog box
# UINT uiMsg,     // message identifier
# WPARAM wParam,  // message parameter
# LPARAM lParam);   // message parameter
OFNHookProc = WINFUNCTYPE(UINT_PTR, HWND, UINT, WPARAM, LPARAM)
LPOFNHOOKPROC = OFNHookProc

class OPENFILENAME(Structure):
	_fields_ = [('lStructSize', DWORD),
		('hwndOwner', HWND),
		('hInstance', HINSTANCE)]
	if UNICODE:
		_fields_ += [('lpstrFilter', c_wchar_p),
			('lpstrCustomFilter', c_wchar_p)]
	else:
		_fields_ += [('lpstrFilter', c_char_p),
			('lpstrCustomFilter', c_char_p)]
	_fields_ += [('nMaxCustFilter', DWORD),
		('nFilterIndex', DWORD)]
	if UNICODE:
		_fields_.append(('lpstrFile', c_wchar_p))
	else:
		_fields_.append(('lpstrFile', c_char_p))
	_fields_.append(('nMaxFile', DWORD))
	if UNICODE:
		_fields_.append(('lpstrFileTitle', c_wchar_p))
	else:
		_fields_.append(('lpstrFileTitle', c_char_p))
	_fields_.append(('nMaxFileTitle', DWORD))
	if UNICODE:
		_fields_ += [('lpstrInitialDir', c_wchar_p),
			('lpstrTitle', c_wchar_p)]
	else:
		_fields_ += [('lpstrInitialDir', c_char_p),
			('lpstrTitle', c_char_p)]
	_fields_ += [('flags', DWORD),
		('nFileOffset', WORD),
		('nFileExtension', WORD)]
	if UNICODE:
		_fields_.append(('lpstrDefExt', c_wchar_p))
	else:
		_fields_.append(('lpstrDefExt', c_char_p))
	_fields_ += [('lCustData', LPARAM),
		('lpfnHook', LPOFNHOOKPROC)]
	if UNICODE:
		_fields_.append(('lpTemplateName', c_wchar_p))
	else:
		_fields_.append(('lpTemplateName', c_char_p))
	_fields_ += [('pvReserved', LPVOID),
		('dwReserved', DWORD),
		('flagsEx', DWORD)]

GetOpenFileName = WINFUNCTYPE(c_bool, POINTER(OPENFILENAME))(('GetOpenFileNameW', windll.comdlg32))
if not UNICODE:
	GetOpenFileName = WINFUNCTYPE(c_bool, POINTER(OPENFILENAME))(('GetOpenFileNameA', windll.comdlg32))
GetSaveFileName = WINFUNCTYPE(c_bool, POINTER(OPENFILENAME))(('GetSaveFileNameW', windll.comdlg32))
if not UNICODE:
	GetSaveFileName = WINFUNCTYPE(c_bool, POINTER(OPENFILENAME))(('GetSaveFileNameA', windll.comdlg32))

OFN_ALLOWMULTISELECT = 512
OFN_CREATEPROMPT= 0x2000
OFN_ENABLEHOOK =32
OFN_ENABLETEMPLATE= 64
OFN_ENABLETEMPLATEHANDLE= 128
OFN_EXPLORER= 0x80000
OFN_EXTENSIONDIFFERENT= 0x400
OFN_FILEMUSTEXIST =0x1000
OFN_HIDEREADONLY= 4
OFN_LONGNAMES =0x200000
OFN_NOCHANGEDIR= 8
OFN_NODEREFERENCELINKS= 0x100000
OFN_NOLONGNAMES= 0x40000
OFN_NONETWORKBUTTON =0x20000
OFN_NOREADONLYRETURN= 0x8000
OFN_NOTESTFILECREATE= 0x10000
OFN_NOVALIDATE= 256
OFN_OVERWRITEPROMPT= 2
OFN_PATHMUSTEXIST= 0x800
OFN_READONLY= 1
OFN_SHAREAWARE= 0x4000
OFN_SHOWHELP= 16
OFN_SHAREFALLTHROUGH= 2
OFN_SHARENOWARN= 1
OFN_SHAREWARN= 0
OFN_NODEREFERENCELINKS = 0x100000
OPENFILENAME_SIZE_VERSION_400 = 76

class FileDialog(OPENFILENAME):
	def SetFilter(self, filter):
		self.lpstrFilter = filter.replace('|', '\0') + '\0\0'

	filter = property(None, SetFilter, None, "")
	def DoModal(self, parent = None):
		#~ szPath = '\0' * 1024
		if versionInfo.isMajorMinor(4, 0): #fix for NT4.0
			self.lStructSize = OPENFILENAME_SIZE_VERSION_400
		else:
			self.lStructSize = sizeof(OPENFILENAME)
		#~ self.lpstrFile = szPath
		self.nMaxFile = 1024
		self.lpstrFile = '\0' * self.nMaxFile
		self.hwndOwner = handle(parent)
		try:
			#the windows file dialogs change the current working dir of the app
			#if the user selects a file from a different dir
			#this prevents that from happening (it causes al sorts of problems with
			#hardcoded relative paths)
			import os
			cwd = os.getcwd()
			#~ if self.DoIt() != 0:
				#~ return szPath[:szPath.find('\0')].strip()
			#~ else:
				#~ return None
			return self.DoIt()
		finally:
			os.chdir(cwd) #return to old current working dir

class OpenFileDialog(FileDialog):
	def DoIt(self):
		return GetOpenFileName(byref(self))

class SaveFileDialog(FileDialog):
	def DoIt(self):
		return GetSaveFileName(byref(self))


# ======================Choosing a Color
CC_RGBINIT              = 0x00000001
CC_FULLOPEN             = 0x00000002
CC_PREVENTFULLOPEN      = 0x00000004
CC_SHOWHELP             = 0x00000008
CC_ENABLEHOOK           = 0x00000010
CC_ENABLETEMPLATE       = 0x00000020
CC_ENABLETEMPLATEHANDLE = 0x00000040
if WINVER >= 0x0400:
	CC_SOLIDCOLOR       = 0x00000080
	CC_ANYCOLOR         = 0x00000100

# UINT_PTR CALLBACK CCHookProc(
# HWND hdlg,      // handle to dialog box
# UINT uiMsg,     // message identifier
# WPARAM wParam,  // message parameter
# LPARAM lParam);   // message parameter
CCHookProc = WINFUNCTYPE(UINT_PTR, HWND, UINT, WPARAM, LPARAM)
LPCCHOOKPROC = CCHookProc

class CHOOSECOLOR(Structure):
	_fields_ = [('lStructSize', DWORD),
		('hwndOwner', HWND),
		('hInstance', HWND),
		('rgbResult', COLORREF),
		('lpCustColors', LPCOLORREF),
		('Flags', DWORD),
		('lCustData', LPARAM),
		('lpfnHook', LPCCHOOKPROC)]
	if UNICODE:
		_fields_.append(('lpTemplateName', c_wchar_p))
	else:
		_fields_.append(('lpTemplateName', c_char_p))

ChooseColor = WINFUNCTYPE(c_bool, POINTER(CHOOSECOLOR))(('ChooseColorW', windll.comdlg32))
if not UNICODE:
	ChooseColor = WINFUNCTYPE(c_bool, POINTER(CHOOSECOLOR))(('ChooseColorA', windll.comdlg32))

