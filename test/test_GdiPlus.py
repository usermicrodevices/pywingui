'GdiPlus example based on pyWinGUI (Maxim Kolosov)'

from random import seed, randint

from pywingui import gdiplusflat as gdiplus
from pywingui import gdi
from pywingui.wtl import *
#~ from pywingui.winuser import *
#~ from pywingui.version_microsoft import WINVER

#VOID CALLBACK TimerProc(_In_  HWND hwnd, _In_  UINT uMsg, _In_  UINT_PTR idEvent, _In_  DWORD dwTime);
#~ TimerProc = WINFUNCTYPE(None, c_void_p, c_uint, c_void_p, c_ulong)

class main_window(Window):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)

	#~ def timer(self, hwnd, uMsg, idEvent, dwTime):
		#~ print hwnd, uMsg, idEvent, dwTime

	def OnDestroy(self, event):
		application.Quit()

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		ps.fErase = True
		hdc = self.BeginPaint(ps)
		rect = self.GetClientRect()
		self.Drawing_a_Shaded_Rectangle(hdc, rect)
		status, graphics = gdiplus.GdipCreateFromHDC(hdc)
		status, pen = gdiplus.GdipCreatePen1(gdiplus.MakeARGB(100, randint(0, 255), randint(0, 255), randint(0, 255)), 30.0)
		status = gdiplus.GdipDrawLineI(graphics, pen, 0, 0, rect.width, rect.height)
		status = gdiplus.GdipDrawLineI(graphics, pen, rect.width, 0, 0, rect.height)
		points = [(rect.width/2, 0), (rect.width/2, rect.height), (0, rect.height), (0, rect.height/2), (rect.width, rect.height/2)]
		lines = (POINT*len(points))(*points)
		status = gdiplus.GdipDrawLinesI(graphics, pen, lines, len(lines))
		x, y = rect.width/3, rect.height/3
		status = gdiplus.GdipDrawEllipseI(graphics, pen, x, y, x, y)
		status = gdiplus.GdipDrawRectangleI(graphics, pen, rect.left, rect.top, rect.right, rect.bottom)
		self.EndPaint(ps)

	def OnTimer(self, event):
		self.InvalidateRect(self.GetClientRect(), False)
		#~ self.UpdateWindow()

	msg_handler(WM_DESTROY)(OnDestroy)
	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_TIMER)(OnTimer)

	def Drawing_a_Shaded_Rectangle(self, hdc, rc):
		vert = (gdi.TRIVERTEX*2)()
		gRect = gdi.GRADIENT_RECT()
		vert[0].x      = 0
		vert[0].y      = 0
		vert[0].Red    = randint(0x0000, 0xffff)
		vert[0].Green  = randint(0x0000, 0xffff)
		vert[0].Blue   = randint(0x0000, 0xffff)
		vert[0].Alpha  = 0x8000
		vert[1].x      = rc.width
		vert[1].y      = rc.height
		vert[1].Red    = randint(0x0000, 0xffff)
		vert[1].Green  = randint(0x0000, 0xffff)
		vert[1].Blue   = randint(0x0000, 0xffff)
		vert[1].Alpha  = 0x8000
		gRect.UpperLeft  = 0
		gRect.LowerRight = 1
		gdi.GradientFill(hdc, vert, 2, byref(gRect), 1, gdi.GRADIENT_FILL_RECT_H)

if __name__ == '__main__':
	# Initialize GDI+
	gdiplusToken = pointer(c_ulong())
	startup_input = gdiplus.GdiplusStartupInput(1, cast(None, gdiplus.DebugEventProc), False, False)
	gdiplus.GdiplusStartup(byref(gdiplusToken), startup_input, None)

	seed()

	mw = main_window(rcPos = RECT(0, 0, 320, 240))
	mw.SetTimer(0, 500)
	application = Application()
	application.Run()

	# Shutdown GDI+
	gdiplus.GdiplusShutdown(gdiplusToken)
