'Simple ChooseColor example based on pyWinGUI'

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import gdi

from pywingui.comdlg import ChooseColor, CHOOSECOLOR, COLORREF, LPCOLORREF, CC_FULLOPEN, CC_RGBINIT

class MyWindow(Window):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.WHITE_BRUSH)
	_window_class_style_ = CS_HREDRAW | CS_VREDRAW
	rgbCurrent = 0# initial color selection
	cc = CHOOSECOLOR()# common dialog box structure 
	acrCustClr = (COLORREF*16)()# array of custom colors 
	ZeroMemory(cc, sizeof(CHOOSECOLOR))
	cc.lStructSize = sizeof(CHOOSECOLOR)
	cc.lpCustColors = cast(acrCustClr, LPCOLORREF)
	cc.rgbResult = rgbCurrent
	cc.Flags = CC_FULLOPEN | CC_RGBINIT
	if ChooseColor(cc):
		rgbCurrent = cc.rgbResult

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		hdc = self.BeginPaint(ps)
		rc = self.GetClientRect()
		gdi.SetTextColor(hdc, self.rgbCurrent)
		msg = 'Choosed color is %s' % hex(self.rgbCurrent)
		gdi.TextOut(hdc, rc.width / 2 - 80, rc.height / 2, msg, len(msg))
		self.EndPaint(ps)

	msg_handler(WM_PAINT)(OnPaint)

	def OnDestroy(self, event):
		PostQuitMessage(NULL)

	msg_handler(WM_DESTROY)(OnDestroy)

if __name__ == '__main__':
	myWindow = MyWindow(rcPos = RECT(0, 0, 320, 240))
	application = Application()
	application.Run()
