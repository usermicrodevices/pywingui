'ChooseColor example based on pyWinGUI'

from random import seed, randint

from pywingui.windows import *
from pywingui.wtl import *
from pywingui.lib import form
from pywingui import comctl
from pywingui import gdi
from pywingui.comdlg import ChooseColor, CHOOSECOLOR, COLORREF, LPCOLORREF, CC_FULLOPEN, CC_RGBINIT

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = __doc__
	#~ rgbCurrent = DWORD(0)# initial color selection
	rgbCurrent = 0

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)

	def OnCreate(self, event):
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

		cc = CHOOSECOLOR()# common dialog box structure 
		acrCustClr = (COLORREF*16)()# array of custom colors 
		hwnd = self.handle# owner window
		# Initialize CHOOSECOLOR 
		ZeroMemory(cc, sizeof(CHOOSECOLOR))
		cc.lStructSize = sizeof(CHOOSECOLOR)
		cc.hwndOwner = hwnd
		cc.lpCustColors = cast(acrCustClr, LPCOLORREF)
		cc.rgbResult = self.rgbCurrent
		cc.Flags = CC_FULLOPEN | CC_RGBINIT
		if ChooseColor(byref(cc)):
			#hbrush = gdi.CreateSolidBrush(cc.rgbResult)
			#hbrush = gdi.SolidBrush(cc.rgbResult)
			self.rgbCurrent = cc.rgbResult
			#~ print('Choosed color is %s' % hex(self.rgbCurrent))

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

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		ps.fErase = True
		hdc = self.BeginPaint(ps)
		rect = self.GetClientRect()
		self.Drawing_a_Shaded_Rectangle(hdc, rect)
		gdi.SetTextColor(hdc, self.rgbCurrent)
		msg = 'Choosed color is %s' % hex(self.rgbCurrent)
		point = cast(pointer(rect), LPPOINT)
		gdi.DPtoLP(hdc, point, 2)
		gdi.TextOut(hdc, point[1].x / 2 - 80, point[1].y / 2 - 20, msg, len(msg))
		#~ gdi.TextOut(hdc, rect.width / 2 - 80, rect.height / 2 - 20, msg, len(msg))
		self.EndPaint(ps)
		#~ self.UpdateWindow()
		#~ self.RedrawWindow(rc, 0, RDW_VALIDATE|RDW_ERASE|RDW_FRAME|RDW_ALLCHILDREN)

	def OnTimer(self, event):
		self.InvalidateRect(self.GetClientRect(), False)

	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_TIMER)(OnTimer)

if __name__ == '__main__':
	seed()

	mainForm = Form(rcPos = RECT(0, 0, 320, 240))
	mainForm.SetTimer(0, 1000)
	mainForm.ShowWindow()

	application = Application()
	application.Run()

