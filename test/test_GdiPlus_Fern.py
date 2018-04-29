'GdiPlus Fern Fractal generator based on pyWinGUI, original was written on ActionScript by Jim Bumgardner 2008'

import math

from pywingui.wtl import *
from pywingui import gdi
from pywingui import gdiplusflat as gdiplus
from pywingui import comctl
from pywingui.lib import form, splitter, trackbar

comctl.InitCommonControls(comctl.ICC_COOL_CLASSES | comctl.ICC_BAR_CLASSES | comctl.ICC_STANDARD_CLASSES)

class fern_canvas(Window):
	_window_style_ = WS_CHILD | WS_VISIBLE | WS_TABSTOP
	_window_background_ = gdi.GetStockObject(gdi.WHITE_BRUSH)
	_window_style_ex_ = WS_EX_CLIENTEDGE

	maxLevels = 6
	initBendAngle = 15
	initBranchAngle = 37
	trunkRatio = 0.1
	branchRatio = 0.4
	heightScale = 1.5
	redrawing = True

	def draw(self, graphics, px, py, a, rad, level):
		cx = int(px + math.cos(a) * rad * self.trunkRatio)
		cy = int(py + math.sin(a) * rad * self.trunkRatio)
		status, pen = gdiplus.GdipCreatePen1(gdiplus.MakeARGB(100, 0, 100 + level * 3, 0), level)
		status = gdiplus.GdipDrawLineI(graphics, pen, px, py, cx, cy)
		if (level > 0):
			a = a + self.bendAngle
			level = level - 1
			self.draw(graphics, cx, cy, a - self.branchAngle, rad * self.branchRatio, level)	  
			status = gdiplus.GdipDrawLineI(graphics, pen, px, py, cx, cy)
			self.draw(graphics, cx, cy, a + self.branchAngle, rad * self.branchRatio, level)	  
			status = gdiplus.GdipDrawLineI(graphics, pen, px, py, cx, cy)
			self.draw(graphics, cx, cy, a, rad * self.antiTrunkRatio, level)

	def redraw(self, hdc, rect):
		w, h = rect.width, rect.height
		status, graphics = gdiplus.GdipCreateFromHDC(hdc)
		if graphics:
			self.bendAngle = self.initBendAngle * math.pi / 180
			self.branchAngle = self.initBranchAngle * math.pi / 180
			self.lastMaxLevels = self.maxLevels
			self.antiTrunkRatio = 1 - self.trunkRatio
			self.startAngle = -math.pi / 2
			px = w / 2
			py = h - 5
			#~ gdiplus.GdipSetCompositingMode(graphics, 1)
			gdiplus.GdipSetSmoothingMode(graphics, 4)# turn on antialiasing
			self.draw(graphics, px, py, self.startAngle, (h - 100) * self.heightScale, self.maxLevels)
			self.redrawing = not self.redrawing

	def OnPaint(self, event):
		if self.redrawing:
			ps = PAINTSTRUCT()
			ps.fErase = True
			hdc = self.BeginPaint(ps)
			rect = self.GetClientRect()
			self.redraw(hdc, rect)
			self.EndPaint(ps)
			self.redrawing = not self.redrawing

	def OnSize(self, event):
		self.InvalidateRect(self.GetClientRect(), True)

	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_SIZE)(OnSize)

class track_bar(Window):
	_window_style_ = WS_VISIBLE | WS_CHILD
	_window_style_ex_ = WS_EX_STATICEDGE
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)

	def __init__(self, *args, **kwargs):
		self.form = kwargs.pop('form', None)
		if not self.form:
			MessageBox('WARNING', 'form parameter must be filled')
		Window.__init__(self, *args, **kwargs)
		caption_pos = RECT(0, 0, self.clientRect.width, self.clientRect.height/3)
		self.caption = comctl.StaticText(title = kwargs['title'] or '', rcPos = caption_pos, parent = self)
		tb_pos = RECT(0, caption_pos.height, self.clientRect.width, self.clientRect.height)
		self.tb = trackbar.TrackBar(rcPos = tb_pos, parent = self)
		self.current_position = self.tb.GetPos()
		self.tb.OnScroll = self.OnScroll

	def SetRange(self, min = 0, max = 0):
		self.tb.SetRange(min, max)

	def SetPos(self, position = 0):
		self.tb.SetPos(position)
		self.current_position = position

	def OnScroll(self, event):
		position = self.tb.GetPos()
		if self.current_position != position:
			self.current_position = position
			title = self.caption.GetText()
			if 'Recursion Levels' in title:
				self.form.fc.maxLevels = position
				self.caption.SetText(self.form.FMT_RECURSION % self.form.fc.maxLevels)
			elif 'Bend Angle' in title:
				self.form.fc.initBendAngle = position - 60
				self.caption.SetText(self.form.FMT_BEND_ANGLE % self.form.fc.initBendAngle)
			elif 'Branch Angle' in title:
				self.form.fc.initBranchAngle = position
				self.caption.SetText(self.form.FMT_BRANCH_ANGLE % self.form.fc.initBranchAngle)
			elif 'Trunk Ratio' in title:
				self.form.fc.trunkRatio = position / 100.0
				self.caption.SetText(self.form.FMT_TRUNK_RATIO % self.form.fc.trunkRatio)
			elif 'Branch Ratio' in title:
				self.form.fc.branchRatio = position / 10.0
				self.caption.SetText(self.form.FMT_BRANCH_RATIO % self.form.fc.branchRatio)
			elif 'Height Scale' in title:
				self.form.fc.heightScale = position / 10.0
				self.caption.SetText(self.form.FMT_HEIGHT_SCALE % self.form.fc.heightScale)
			self.form.fc.InvalidateRect(self.form.fc.GetClientRect(), True)

class main_form(form.Form):
	_window_title_ = __doc__
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)
	_form_exit_ = form.EXIT_ONLASTDESTROY
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]

	FMT_RECURSION = 'Recursion Levels: %d'
	FMT_BEND_ANGLE = 'Bend Angle: %d'
	FMT_BRANCH_ANGLE = 'Branch Angle: %d'
	FMT_TRUNK_RATIO = 'Trunk Ratio: %.2f'
	FMT_BRANCH_RATIO = 'Branch Ratio: %.1f'
	FMT_HEIGHT_SCALE = 'Height Scale: %.1f'

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)

	def OnCreate(self, event):
		self.sp = splitter.Splitter(splitPos = self.clientRect.width / 2, parent = self)

		self.fc = fern_canvas(parent = self.sp, orExStyle = WS_EX_STATICEDGE)
		self.sp.Add(1, self.fc)
		self.controls.Add(self.fc)

		self.prop = form.Form(parent = self.sp, style = WS_CHILD | WS_VISIBLE, orExStyle = WS_EX_STATICEDGE)
		self.prop._window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)

		tb = track_bar(title = self.FMT_RECURSION % self.fc.maxLevels, rcPos = RECT(5, 0, 300, 50), parent = self.prop, form = self)
		tb.SetRange(1, 10)
		tb.SetPos(self.fc.maxLevels)
		self.controls.Add(tb)

		tb = track_bar(title = self.FMT_BEND_ANGLE % self.fc.initBendAngle, rcPos = RECT(5, 60, 300, 110), parent = self.prop, form = self)
		tb.SetRange(0, 120)
		tb.SetPos(self.fc.initBendAngle + 60)
		self.controls.Add(tb)

		tb = track_bar(title = self.FMT_BRANCH_ANGLE % self.fc.initBranchAngle, rcPos = RECT(5, 120, 300, 170), parent = self.prop, form = self)
		tb.SetRange(0, 90)
		tb.SetPos(self.fc.initBranchAngle)
		self.controls.Add(tb)

		tb = track_bar(title = self.FMT_TRUNK_RATIO % self.fc.trunkRatio, rcPos = RECT(5, 180, 300, 230), parent = self.prop, form = self)
		tb.SetRange(0, 75)
		tb.SetPos(int(self.fc.trunkRatio * 100))
		self.controls.Add(tb)

		tb = track_bar(title = self.FMT_BRANCH_RATIO % self.fc.branchRatio, rcPos = RECT(5, 240, 300, 290), parent = self.prop, form = self)
		tb.SetRange(1, 20)
		tb.SetPos(int(self.fc.branchRatio * 10))
		self.controls.Add(tb)

		tb = track_bar(title = self.FMT_HEIGHT_SCALE % self.fc.heightScale, rcPos = RECT(5, 300, 300, 350), parent = self.prop, form = self)
		tb.SetRange(1, 80)
		tb.SetPos(int(self.fc.heightScale * 10))
		self.controls.Add(tb)

		self.sp.Add(0, self.prop)

		self.controls.Add(form.CTRL_VIEW, self.sp)
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

	def OnDestroy(self, event):
		application.Quit()
	msg_handler(WM_DESTROY)(OnDestroy)

if __name__ == '__main__':
	gdiplusToken = pointer(c_ulong())
	startup_input = gdiplus.GdiplusStartupInput(1, cast(None, gdiplus.DebugEventProc), False, False)
	gdiplus.GdiplusStartup(byref(gdiplusToken), startup_input, None)

	mf = main_form(rcPos = RECT(0, 0, 640, 480))
	mf.ShowWindow()
	application = Application()
	application.Run()

	gdiplus.GdiplusShutdown(gdiplusToken)
