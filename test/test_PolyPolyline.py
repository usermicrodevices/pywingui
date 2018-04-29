'PolyPolyline example based on pyWinGUI (Maxim Kolosov)'

from random import seed, randint

from pywingui import gdi
from pywingui.wtl import *
from pywingui.winuser import *
from pywingui.version_microsoft import WINVER

class main_window(Window):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)
	pt_size = 11# count points
	set_size = 3# count figures
	pt = (POINT*pt_size)((10, 10), (100, 10), (50, 100), (10, 10),# 0 figure (triangle)
		(10, 110), (200, 110), (200, 180), (10, 180), (10, 110),# 1 figure (parallelogram)
		(10, 200), (200, 200))# 2 figure (line)
	pts = (c_ulong*set_size)(4, 5, 2)# count points in every figure

	def OnDestroy(self, event):
		application.Quit()

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		ps.fErase = True
		hdc = self.BeginPaint(ps)
		if WINVER >= 0x0400:
			gdi.SetGraphicsMode(hdc, gdi.GM_ADVANCED)
			gdi.SetMapMode(hdc, gdi.MM_ANISOTROPIC)
		rect = self.GetClientRect()
		self.Drawing_a_Shaded_Rectangle(hdc, rect)
		gdi.SelectObject(hdc, gdi.GetStockObject(gdi.DC_PEN))
		gdi.SetDCPenColor(hdc, gdi.RGB(00, 0xff, 00))
		gdi.SelectObject(hdc, gdi.GetStockObject(gdi.DC_BRUSH))
		gdi.SetDCBrushColor(hdc, gdi.RGB(00, 00, 0xff))
		gdi.PolyPolyline(hdc, self.pt, self.pts, self.set_size)
		self.EndPaint(ps)

	def OnTimer(self, event):
		self.InvalidateRect(self.GetClientRect(), False)

	msg_handler(WM_DESTROY)(OnDestroy)
	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_TIMER)(OnTimer)

	def Drawing_a_Shaded_Rectangle(self, hdc, rc):
		vert = (gdi.TRIVERTEX*2)()
		gRect = gdi.GRADIENT_RECT()
		vert[0].x      = 0
		vert[0].y      = 0
		vert[0].Red    = randint(0x0000, 0xffff)#0xff00
		vert[0].Green  = randint(0x0000, 0xffff)#0xff00
		vert[0].Blue   = randint(0x0000, 0xffff)#0x0000
		vert[0].Alpha  = 0x8000
		vert[1].x      = rc.width
		vert[1].y      = rc.height
		vert[1].Red    = randint(0x0000, 0xffff)#0x0000
		vert[1].Green  = randint(0x0000, 0xffff)#0x0000
		vert[1].Blue   = randint(0x0000, 0xffff)#0xff00
		vert[1].Alpha  = 0x8000
		gRect.UpperLeft  = 0
		gRect.LowerRight = 1
		gdi.GradientFill(hdc, vert, 2, byref(gRect), 1, gdi.GRADIENT_FILL_RECT_H)

if __name__ == '__main__':
	seed()
	mw = main_window(rcPos = RECT(0, 0, 320, 240))
	mw.SetTimer(0, 500)
	application = Application()
	application.Run()
