#~ ; gdi+ ahk analogue clock example written by derRaphael
#~ ; Parts based on examples from Tic's GDI+ Tutorials and of course on his GDIP.ahk
#~ ; This code has been licensed under the terms of EUPL 1.0
#==========================================
'GDI+ Clock written by derRaphael for AutoIt'

from math import *
from datetime import datetime
from random import seed, randint

from pywingui import gdiplusflat as gdiplus
from pywingui import gdi
from pywingui.wtl import *

class main_window(Window):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)
	pt_size = 11# count points
	set_size = 3# count figures
	graphics = 0
	full_redraw_counter = 0

	ClockDiameter = 180.0
	Width = Height = ClockDiameter + 2  # make width and height slightly bigger to avoid cut away edges
	CenterX = CenterY = floor(ClockDiameter/2) # Center x

	def draw_clock_marks(self, pen, items, r1, r2):
		for i in range(items):
			gdiplus.GdipDrawLine(self.graphics, pen,
			self.CenterX - ceil(r1 * cos(((i-1)*360/items) * atan(1) * 4 / 180)),
			self.CenterY - ceil(r1 * sin(((i-1)*360/items) * atan(1) * 4 / 180)),
			self.CenterX - ceil(r2 * cos(((i-1)*360/items) * atan(1) * 4 / 180)),
			self.CenterY - ceil(r2 * sin(((i-1)*360/items) * atan(1) * 4 / 180)))

	def draw_outer_circle(self):
		Diameter = self.ClockDiameter
		status, pBrush_outer = gdiplus.GdipCreateSolidFill(0x66008000)
		gdiplus.GdipFillEllipse(self.graphics, pBrush_outer, self.CenterX-(Diameter/2), self.CenterY-(Diameter/2), Diameter, Diameter)
		#~ gdiplus.GdipDeleteBrush(pBrush_outer)

	def draw_inner_circle(self):
		Diameter = ceil(self.ClockDiameter - self.ClockDiameter*0.08)  # inner circle is 8 % smaller than clock's diameter
		status, pBrush_inner = gdiplus.GdipCreateSolidFill(0x80008000)
		gdiplus.GdipFillEllipse(self.graphics, pBrush_inner, self.CenterX-(Diameter/2), self.CenterY-(Diameter/2),Diameter, Diameter)
		#~ gdiplus.GdipDeleteBrush(pBrush_inner)

	def draw_second_marks(self):
		Diameter = self.ClockDiameter
		R1 = Diameter/2-1                       # outer position
		R2 = Diameter/2-1-ceil(Diameter/2*0.05) # inner position
		Items = 60                              # we have 60 seconds
		status, pPen = gdiplus.GdipCreatePen1(0xff00a000, floor((self.ClockDiameter/100)*1.2)) # 1.2 % of total diameter is our pen width
		self.draw_clock_marks(pPen, Items, R1, R2)
		#~ gdiplus.GdipDeletePen(pPen)

	def draw_hour_marks(self):
		Diameter = self.ClockDiameter
		R1 = Diameter/2-1                      # outer position
		R2 = Diameter/2-1-ceil(Diameter/2*0.1) # inner position
		Items = 12                             # we have 12 hours
		status, pPen = gdiplus.GdipCreatePen1(0xc0008000, ceil((self.ClockDiameter/100)*2.3)) # 2.3 % of total diameter is our pen width
		self.draw_clock_marks(pPen, Items, R1, R2)
		#~ gdiplus.GdipDeletePen(pPen)

	def draw_arrows(self):
		Diameter = self.ClockDiameter
		CenterX, CenterY = self.CenterX, self.CenterY
		current_time = datetime.now()
		A_Hour, A_Min, A_Sec = current_time.hour, current_time.minute, current_time.second

		# prepare to empty previously drawn stuff
		#~ gdiplus.GdipSetSmoothingMode(self.graphics, 1)   # turn off aliasing
		#~ gdiplus.GdipSetCompositingMode(self.graphics, 1) # set to overdraw

		# delete previous graphic and redraw background
		#~ Diameter = ceil(self.ClockDiameter - self.ClockDiameter*0.18)  # 18 % less than clock's outer diameter

		# delete whatever has been drawn here
		#~ status, pBrush = gdiplus.GdipCreateSolidFill(0x00000000) # fully transparent brush 'eraser'
		#~ gdiplus.GdipFillEllipse(self.graphics, pBrush, CenterX-(Diameter/2), CenterY-(Diameter/2), Diameter, Diameter)
		#~ gdiplus.GdipDeleteBrush(pBrush)

		#~ gdiplus.GdipSetCompositingMode(self.graphics, 0) # switch off overdraw
		#~ status, pBrush = gdiplus.GdipCreateSolidFill(0x66008000)
		#~ gdiplus.GdipFillEllipse(self.graphics, pBrush, CenterX-(Diameter/2), CenterY-(Diameter/2), Diameter, Diameter)
		#~ gdiplus.GdipDeleteBrush(pBrush)
		#~ status, pBrush = gdiplus.GdipCreateSolidFill(0x80008000)
		#~ gdiplus.GdipFillEllipse(self.graphics, pBrush, CenterX-(Diameter/2), CenterY-(Diameter/2), Diameter, Diameter)
		#~ gdiplus.GdipDeleteBrush(pBrush)

		# Draw HoursPointer
		gdiplus.GdipSetSmoothingMode(self.graphics, 4)   # turn on antialiasing
		t = A_Hour*360/12 + (A_Min*360/60)/12 +90 
		R1 = self.ClockDiameter/2-ceil((self.ClockDiameter/2)*0.5) # outer position
		status, pPen = gdiplus.GdipCreatePen1(0xa0008000, floor((self.ClockDiameter/100)*3.5))
		gdiplus.GdipDrawLine(self.graphics, pPen, CenterX, CenterY,
			ceil(CenterX - (R1 * cos(t * atan(1) * 4 / 180))),
			ceil(CenterY - (R1 * sin(t * atan(1) * 4 / 180))))
		gdiplus.GdipDeletePen(pPen)

		# Draw MinutesPointer
		t = A_Min*360/60+90 
		R1 = self.ClockDiameter/2-ceil((self.ClockDiameter/2)*0.25) # outer position
		status, pPen = gdiplus.GdipCreatePen1(0xa0008000, floor((self.ClockDiameter/100)*2.7))
		gdiplus.GdipDrawLine(self.graphics, pPen, CenterX, CenterY,
			ceil(CenterX - (R1 * cos(t * atan(1) * 4 / 180))),
			ceil(CenterY - (R1 * sin(t * atan(1) * 4 / 180))))
		gdiplus.GdipDeletePen(pPen)

		# Draw SecondsPointer
		t = A_Sec*360/60+90 
		R1 = self.ClockDiameter/2-ceil((self.ClockDiameter/2)*0.2) # outer position
		status, pPen = gdiplus.GdipCreatePen1(0xa000FF00, floor((self.ClockDiameter/100)*1.2))
		gdiplus.GdipDrawLine(self.graphics, pPen, CenterX, CenterY,
			ceil(CenterX - (R1 * cos(t * atan(1) * 4 / 180))),
			ceil(CenterY - (R1 * sin(t * atan(1) * 4 / 180))))
		gdiplus.GdipDeletePen(pPen)

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

	def OnDestroy(self, event):
		if self.graphics:
			status = gdiplus.GdipDeleteGraphics(self.graphics)
		application.Quit()

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		ps.fErase = True
		hdc = self.BeginPaint(ps)
		rect = self.GetClientRect()
		self.ClockDiameter = rect.width
		if self.ClockDiameter > rect.height:
			self.ClockDiameter = rect.height
		self.Width = self.Height = self.ClockDiameter + 2
		self.CenterX = self.CenterY = floor(self.ClockDiameter/2)

		# redraw background with new color
		self.Drawing_a_Shaded_Rectangle(hdc, rect)

		status, self.graphics = gdiplus.GdipCreateFromHDC(hdc)
		#~ status = gdiplus.GdipSetSmoothingMode(self.graphics, 4)
		#~ if self.full_redraw_counter == 0:
		#~ self.draw_outer_circle()
		#~ self.draw_inner_circle()
		self.draw_second_marks()
		self.draw_hour_marks()
		self.draw_arrows()
		self.EndPaint(ps)

	def OnTimer(self, event):
		self.InvalidateRect(self.GetClientRect())#, False)
		#~ self.full_redraw_counter += 1
		#~ if self.full_redraw_counter > 60:
			#~ self.full_redraw_counter = 0
		#~ windll.user32.UpdateLayeredWindow(self.m_handle, self.GetDC(), pointer(POINT(0, 0)), pointer(SIZE(self.Width, self.Height)), gdi.CreateCompatibleDC(self.GetDC()), pointer(POINT(0, 0)), 0, None, 0)

	msg_handler(WM_DESTROY)(OnDestroy)
	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_TIMER)(OnTimer)

if __name__ == '__main__':
	# Initialize GDI+
	gdiplusToken = pointer(c_ulong())
	startup_input = gdiplus.GdiplusStartupInput(1, cast(None, gdiplus.DebugEventProc), False, False)
	status = gdiplus.GdiplusStartup(byref(gdiplusToken), startup_input, None)
	if status != gdiplus.Ok:
		print('GdiPlus failed to start. Result code is %d.' % status)
	else:
		seed()

		mw = main_window(rcPos = RECT(0, 0, 180, 200))
		mw.SetTimer(0, 1000)
		application = Application()
		application.Run()

		# Shutdown GDI+
		gdiplus.GdiplusShutdown(gdiplusToken)
