## 	   Copyright (c) 2003 - 2004 Henk Punt

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
##

from ctypes import *
from windows import *
from winuser import *

import wtl_core

class DecoratedWindow(wtl_core.Window):
	def PostMessage(self, nMsg, wParam = 0, lParam = 0):
		return PostMessage(self.handle, nMsg, wParam, lParam)

	def SendMessage(self, nMsg, wParam = 0, lParam = 0):
		return SendMessage(self.handle, nMsg, wParam, lParam)

	def GetClientRect(self):
		rc = RECT()
		GetClientRect(self.handle, byref(rc))
		return rc

	clientRect = property(GetClientRect, None, None, "")

	def SetWindowPos(self, hWndInsertAfter, x, y, cx, cy, uFlags):
		SetWindowPos(self.handle, hWndInsertAfter, x, y, cx, cy, uFlags)

	def GetWindowRect(self):
		rc = RECT()
		GetWindowRect(self.handle, byref(rc))
		return rc

	windowRect = property(GetWindowRect, None, None, "")

	def ChildWindowFromPoint(self, point):
		return windowFromHandle(ChildWindowFromPoint(self.handle, point))

	def ScreenToClient(self, point):
		ScreenToClient(self.handle, byref(point))

	def ClientToScreen(self, point):
		ClientToScreen(self.handle, byref(point))

	def SetRedraw(self, bRedraw):
		self.SendMessage(WM_SETREDRAW, bRedraw, 0)

	def SetFont(self, hFont, bRedraw):
		self.SendMessage(WM_SETFONT, handle(hFont), bRedraw)

	def SetWindowText(self, txt):
		SetWindowText(self.handle, txt)

	def SetText(self, text):
		txt = create_unicode_buffer(text)
		if not UNICODE:
			txt = create_string_buffer(text)
		self.SendMessage(WM_SETTEXT, 0, addressof(txt))

	def GetText(self):
		textLength = self.SendMessage(WM_GETTEXTLENGTH) + 1
		textBuff = create_unicode_buffer(textLength)
		if not UNICODE:
			textBuff = create_string_buffer(textLength)
		self.SendMessage(WM_GETTEXT, textLength, byref(textBuff))
		return textBuff.value

	def MoveWindow(self, x, y, nWidth, nHeight, bRepaint = True):
		MoveWindow(self.handle, x, y, nWidth, nHeight, bRepaint)

	def GetParent(self):
		return instanceOrHandle(GetParent(self.handle))

	parent = property(GetParent)

	def GetMenu(self):
		"""Return a non managed object wrapper for this windows menu,
		the menu is not destroyed when the wrapper goes out of scope (becomes
		garbage)"""
		return Menu(hWnd = GetMenu(self.handle), managed = False)

	def CenterWindow(self, parent = None):
		"""centers this window in its parent window, or the given
		parent window. If no parent window is given or found, the
		window is centered on the desktop"""
		if not parent:
			parent = self.GetParent()
		if not parent:
			parent = Window(hWnd = GetDesktopWindow())
		x = (parent.windowRect.width / 2) - (self.windowRect.width / 2)
		y = (parent.windowRect.height / 2) - (self.windowRect.height / 2)
		self.SetWindowPos(0, parent.windowRect.left + x, parent.windowRect.top + y, 0, 0, SWP_NOACTIVATE | SWP_NOSIZE | SWP_NOZORDER)

	def SetFocus(self):
		SetFocus(self.handle)

	def ShowWindow(self, cmdShow = SW_SHOWNORMAL):
		ShowWindow(self.handle, cmdShow)

	def IsWindowVisible(self):
		return bool(IsWindowVisible(self.handle))

	def IsIconic(self):
		return bool(IsIconic(self.handle))

	def GetClassLong(self, index):
		return GetClassLong(self.handle, index)

	def SetClassLong(self, index, dwNewLong):
		SetClassLong(self.handle, index, dwNewLong)

	def UpdateWindow(self):
		UpdateWindow(self.handle)

	def SetCapture(self):
		SetCapture(self.handle)

	def ExcludeUpdateRgn(self, hdc):
		return ExcludeUpdateRgn(hdc, self.handle)

	def Invalidate(self, bErase = True):
		return InvalidateRect(self.handle, None, bErase)
		#~ return InvalidateRect(self.handle, NULL, bErase)

	def InvalidateRect(self, rc = None, bErase = True):
		return InvalidateRect(self.handle, pointer(rc), bErase)
		#~ return InvalidateRect(self.handle, byref(rc), bErase)

	def InvalidateRgn(self, hRgn = None, bErase = True):
		return InvalidateRgn(self.handle, hRgn, bErase)

	def Validate(self):
		return ValidateRect(self.handle, None)

	def ValidateRect(self, rc = None):
		return ValidateRect(self.handle, pointer(rc))

	def ValidateRgn(self, region = None):
		return ValidateRgn(self.handle, region)

	def GetDCEx(self, hrgnClip, flags):
		return GetDCEx(self.handle, hrgnClip, flags)

	def GetDC(self):
		return GetDC(self.handle)

	def ReleaseDC(self, hdc):
		ReleaseDC(self.handle, hdc)

	def BeginPaint(self, paintStruct):
		return BeginPaint(self.handle, byref(paintStruct))

	def EndPaint(self, paintStruct):
		return EndPaint(self.handle, byref(paintStruct))

	def DestroyWindow(self):
		DestroyWindow(self.handle)

	def CloseWindow(self):
		CloseWindow(self.handle)

	def SetForegroundWindow(self):
		SetForegroundWindow(self.handle)

	def EnumChildWindows(self):
		"""returns a list of this windows child windows"""
		childWindows = []
		def enumChildProc(hWnd, lParam):
			childWindows.append(Window(hWnd = hWnd))
		EnumChildWindows(self.handle, EnumChildProc(enumChildProc), 0)
		return childWindows

	def SetTimer(self, id, elapse, timerProc = NULL):
		return SetTimer(self.handle, id, elapse, timerProc)

	def LockWindowUpdate(self, fLock):
		if fLock:
			LockWindowUpdate(self.handle)
		else:
			LockWindowUpdate(NULL)

	def KillTimer(self, id):
		KillTimer(self.handle, id)

	def GetCursorPos():
		"""gets the position of the mouse cursor in screen coords"""
		pt = POINT()
		GetCursorPos(byref(pt))
		return pt.x, pt.y

	GetCursorPos = staticmethod(GetCursorPos)

	def RedrawWindow(self, lprcUpdate = None, hrgnUpdate = 0, flags = 0):
		return RedrawWindow(self.handle, lprcUpdate, hrgnUpdate, flags)

wtl_core.Window = DecoratedWindow

class EventDecorator(wtl_core.Event):
	handle = property(lambda self: self.hWnd)

	def getSize(self):
		return LOWORD(self.lParam), HIWORD(self.lParam)

	size = property(getSize, None, None, "")

	def getPosition(self):
		x, y = GET_XY_LPARAM(GetMessagePos())
		return POINT(x, y)

	position = property(getPosition)

	def getClientPosition(self):
		x, y = GET_XY_LPARAM(self.lParam)
		return POINT(x, y)

	clientPosition = property(getClientPosition)

wtl_core.Event = EventDecorator

class Icon(wtl_core.WindowsObject):
	__dispose__ = DestroyIcon

	def __init__(self, *args, **kwargs):
		hinst = kwargs.pop('hinst', NULL)
		if not hinst:
			hinst = kwargs.pop('hInstance', NULL)
		lpszName = kwargs.pop('lpszName', 0)
		if not lpszName:
			lpszName = kwargs.pop('lpIconName', 0)
		uType = kwargs.pop('uType', IMAGE_ICON)
		cxDesired = kwargs.pop('cxDesired', 0)
		cyDesired = kwargs.pop('cyDesired', 0)
		fuLoad = kwargs.pop('fuLoad', LR_LOADFROMFILE)
		# useLoadIcon only for the standard exclamation icon
		# and for a custom icon included as a resource in the application's resource-definition file.
		useLoadIcon = kwargs.pop('useLoadIcon', False)
		# now args parser
		if len(args) == len(kwargs) == 0:
			useLoadIcon = True
		elif len(args) == 1:
			if isinstance(args[0], (int, long, HINSTANCE)):
				hinst = args[0]
			else:# for Venster backward compatibility
				lpszName = args[0]
		elif len(args) == 2:
			hinst, lpszName = args
		elif len(args) == 3:
			hinst, lpszName, uType = args
		elif len(args) == 4:
			hinst, lpszName, uType, cxDesired = args
		elif len(args) == 5:
			hinst, lpszName, uType, cxDesired, cyDesired = args
		elif len(args) > 5:
			hinst, lpszName, uType, cxDesired, cyDesired, fuLoad = args
		if isinstance(lpszName, (int, long)):
			lpszName = MAKEINTRESOURCE(lpszName)
		if useLoadIcon:
			wtl_core.WindowsObject.__init__(self, LoadIcon(hinst, lpszName))
		else:
			wtl_core.WindowsObject.__init__(self, LoadImage(hinst, lpszName, uType, cxDesired, cyDesired, fuLoad))

class IconEx(wtl_core.WindowsObject):
	__dispose__ = DestroyIcon

	def __init__(self, *args, **kwargs):
		hInstance = kwargs.pop('hInstance', NULL)
		nWidth = kwargs.pop('nWidth', 32)
		nHeight = kwargs.pop('nHeight', 32)
		cPlanes = kwargs.pop('cPlanes', 1)
		cBitsPixel = kwargs.pop('cBitsPixel', 1)
		lpbANDbits = kwargs.pop('lpbANDbits', NULL)
		lpbXORbits = kwargs.pop('lpbXORbits', NULL)
		# now args parser
		if len(args) == 1:
			hInstance = args[0]
		elif len(args) == 2:
			hInstance, nWidth = args
		elif len(args) == 3:
			hInstance, nWidth, nHeight = args
		elif len(args) == 4:
			hInstance, nWidth, nHeight, cPlanes = args
		elif len(args) == 5:
			hInstance, nWidth, nHeight, cPlanes, cBitsPixel = args
		elif len(args) == 6:
			hInstance, nWidth, nHeight, cPlanes, cBitsPixel, lpbANDbits = args
		elif len(args) > 6:
			hInstance, nWidth, nHeight, cPlanes, cBitsPixel, lpbANDbits, lpbXORbits = args
		wtl_core.WindowsObject.__init__(self, CreateIcon(hInstance, nWidth, nHeight, cPlanes, cBitsPixel, lpbANDbits, lpbXORbits))

class MenuBase(object):
	def AppendMenu(self, flags = 0, idNewItem = 0, lpNewItem = ''):
		if flags == MF_STRING or flags == MF_SEPARATOR:
			AppendMenu(self.handle, flags, idNewItem, lpNewItem)
		elif flags & MF_POPUP:
			AppendMenu(self.handle, flags, handle(idNewItem), lpNewItem)

	def EnableMenuItem(self, uIDEnableItem, uEnable):
		EnableMenuItem(self.handle, uIDEnableItem, uEnable)

	def GetSubMenu(self, id):
		return instanceFromHandle(GetSubMenu(self.handle, id))

	def GetItemCount(self):
		return GetMenuItemCount(self.handle)

	def SetMenuDefaultItem(self, uItem, fByPos = False):
		SetMenuDefaultItem(self.handle, uItem, 0)

	def __len__(self):
		return self.GetItemCount()

class Menu(MenuBase, wtl_core.WindowsObject):
	__dispose__ = DestroyMenu

	def __init__(self, hWnd = None, **kwargs):
		hWnd = hWnd or CreateMenu()
		wtl_core.WindowsObject.__init__(self, hWnd, **kwargs)

class PopupMenu(MenuBase, wtl_core.WindowsObject):
	__dispose__ = DestroyMenu

	def __init__(self, *args, **kwargs):
		wtl_core.WindowsObject.__init__(self, CreatePopupMenu(), *args, **kwargs)

	def TrackPopupMenuEx(self, fuFlags, x, y, hwnd, lptpm = NULL):
		return TrackPopupMenuEx(self.handle, fuFlags, x, y, handle(hwnd), lptpm)

	def Track(self, hwnd, fuFlags = TPM_LEFTBUTTON):
		x, y = wtl_core.Window.GetCursorPos()
		return self.TrackPopupMenuEx(fuFlags, x, y, hwnd)

from wtl_core import *
