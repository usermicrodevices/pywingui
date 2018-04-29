'GdiPlus live grid based on pyWinGUI (Maxim Kolosov)'

from pywingui import gdiplusflat as gdiplus
from pywingui import gdi
from pywingui.wtl import *

class live_grid_2d:
	def __init__(self, *args, **kwargs):
		try:
			self.screen_size = args[0]
		except:
			self.screen_size = POINT(320, 240)
		if 'screen_size' in kwargs:
			self.screen_size = kwargs.pop('screen_size', POINT(320, 240))
		try:
			self.cellw = args[1]
		except:
			self.cellw = 32
		if 'cellw' in kwargs:
			self.cellw = kwargs.pop('cellw', 32)
		try:
			self.cellh = args[2]
		except:
			self.cellh = 32
		if 'cellh' in kwargs:
			self.cellh = kwargs.pop('cellh', 32)
		try:
			self.color_line = args[3]
		except:
			self.color_line = gdiplus.MakeARGB(255, 0, 255, 0)
		if 'color_line' in kwargs:
			self.color_line = kwargs.pop('color_line', gdiplus.MakeARGB(255, 0, 255, 0))
		try:
			self.color_active_cell = args[4]
		except:
			self.color_active_cell = gdiplus.MakeARGB(128, 100, 100, 255)
		if 'color_active_cell' in kwargs:
			self.color_active_cell = kwargs.pop('color_active_cell', gdiplus.MakeARGB(128, 100, 100, 255))
		try:
			self.color_points = args[5]
		except:
			self.color_points = gdiplus.MakeARGB(255, 255, 255, 255)
		if 'color_points' in kwargs:
			self.color_points = kwargs.pop('color_points', gdiplus.MakeARGB(255, 255, 255, 255))
		try:
			self.width_line = args[6]
		except:
			self.width_line = 3
		if 'width_line' in kwargs:
			self.width_line = kwargs.pop('width_line', 3)
		try:
			self.size_point = args[7]
		except:
			self.size_point = 3.0
		if 'size_point' in kwargs:
			self.size_point = kwargs.pop('size_point', 3.0)
		try:
			self.is_draw_lines = args[8]
		except:
			self.is_draw_lines = True
		if 'is_draw_lines' in kwargs:
			self.is_draw_lines = kwargs.pop('is_draw_lines', True)
		try:
			self.is_draw_points = args[9]
		except:
			self.is_draw_points = True
		if 'is_draw_points' in kwargs:
			self.is_draw_points = kwargs.pop('is_draw_points', True)
		self.pen_cell = None
		self.brush_cell = None
		self.pen_lines = None
		self.pen_points = None
		status, self.path_lines = gdiplus.GdipCreatePath()
		status, self.path_points = gdiplus.GdipCreatePath()
		self.current_cell = self.old_cell = RECT(0, 0, self.cellw, self.cellh)
		self.current_point = POINT(0, 0)
		#~ self.create_cells()
		self.create_lines()
		self.create_pens()

	def create_brush_cell(self):
		status, self.brush_cell = gdiplus.GdipCreateSolidFill(self.color_active_cell)
		return status

	def create_cells(self):
		gdiplus.GdipResetPath(self.path_points)
		self.cells = []
		w = self.screen_size.x / self.cellw + 2
		h = self.screen_size.y / self.cellh + 2
		x1, x2, y1, y2 = 0, 0, 0, 0
		d = self.size_point / 2
		for x in range(w):
			x2 = x * self.cellw
			for y in range(h):
				y2 = y * self.cellh
				self.cells.append(RECT(x1, y1, x2, y2))
				status = gdiplus.GdipAddPathEllipse(self.path_points, x1 - d, y1 - d, self.size_point, self.size_point)
				y1 = y2
			x1 = x2

	def create_lines_1(self):
		self.lines = []
		w = self.screen_size.x / self.cellw + 1
		h = self.screen_size.y / self.cellh + 1
		x1 = 0
		for x in range(1, w):
			x1 = x * self.cellw
			self.lines.append((POINT(x1, 0), POINT(x1, self.screen_size.y)))
		y1 = 0
		for y in range(1, h):
			y1 = y * self.cellh
			self.lines.append((POINT(0, y1), POINT(self.screen_size.x, y1)))

	def create_lines_2(self):
		points = []
		w = self.screen_size.x / self.cellw + 1
		h = self.screen_size.y / self.cellh + 1
		x, x1 = 0, 0
		while x < w:
			x += 1
			x1 = x * self.cellw
			points.append((x1, 0))
			points.append((x1, self.screen_size.y))
			x += 1
			x1 = x * self.cellw
			points.append((x1, self.screen_size.y))
			points.append((x1, 0))
		y, y1 = 0, 0
		while y < h:
			y += 1
			y1 = y * self.cellh
			points.append((self.screen_size.x, y1))
			points.append((0, y1))
			y += 1
			y1 = y * self.cellh
			points.append((0, y1))
			points.append((self.screen_size.x, y1))
		self.lines = (POINT*len(points))(*points)

	def create_lines_3(self):
		gdiplus.GdipResetPath(self.path_lines)
		w = self.screen_size.x / self.cellw + 1
		h = self.screen_size.y / self.cellh + 1
		x, x1 = 0, 0
		while x < w:
			x += 1
			x1 = x * self.cellw
			status = gdiplus.GdipAddPathLineI(self.path_lines, x1, 0, x1, self.screen_size.y)
			x += 1
			x1 = x * self.cellw
			status = gdiplus.GdipAddPathLineI(self.path_lines, x1, self.screen_size.y, x1, 0)
		y, y1 = 0, 0
		while y < h:
			y += 1
			y1 = y * self.cellh
			status = gdiplus.GdipAddPathLineI(self.path_lines, self.screen_size.x, y1, 0, y1)
			y += 1
			y1 = y * self.cellh
			status = gdiplus.GdipAddPathLineI(self.path_lines, 0, y1, self.screen_size.x, y1)

	def create_lines(self):
		gdiplus.GdipResetPath(self.path_lines)
		w = self.screen_size.x / self.cellw + 1
		h = self.screen_size.y / self.cellh + 1
		x1 = 0
		for x in range(1, w):
			x1 = x * self.cellw
			status = gdiplus.GdipStartPathFigure(self.path_lines)
			status = gdiplus.GdipAddPathLineI(self.path_lines, x1, 0, x1, self.screen_size.y)
			status = gdiplus.GdipClosePathFigure(self.path_lines)
		y1 = 0
		for y in range(1, h):
			y1 = y * self.cellh
			status = gdiplus.GdipStartPathFigure(self.path_lines)
			status = gdiplus.GdipAddPathLineI(self.path_lines, self.screen_size.x, y1, 0, y1)
			status = gdiplus.GdipClosePathFigure(self.path_lines)

	def get_current_cell(self):
		for rect in self.cells:
			if rect.top < self.current_point.y < rect.bottom and rect.left < self.current_point.x < rect.right:
				return rect
		return self.current_cell

	def is_cell_changed(self):
		result = False
		current_cell = self.get_current_cell()
		if self.current_cell != current_cell:
			self.old_cell = self.current_cell
			self.current_cell = current_cell
			result = True
		return result

	def create_pen_cell(self):
		status, self.pen_cell = gdiplus.GdipCreatePen1(self.color_active_cell, 16.0)
		return status

	def create_pen_lines(self):
		status, self.pen_lines = gdiplus.GdipCreatePen1(self.color_line, self.width_line)
		return status

	def create_pen_points(self):
		status, self.pen_points = gdiplus.GdipCreatePen1(self.color_points, self.size_point)
		return status

	def create_pens(self):
		self.create_pen_cell()
		self.create_pen_lines()
		self.create_pen_points()

	def draw_current_cell_1(self, graphics):
		status = gdiplus.GdipDrawRectangleI(graphics, self.pen_cell, self.current_cell.left, self.current_cell.top, self.cellw, self.cellh)

	def draw_current_cell(self, graphics):
		status = gdiplus.GdipFillRectangle(graphics, self.brush_cell, self.current_cell.left, self.current_cell.top, self.cellw, self.cellh)

	def draw_lines_1(self, graphics):
		for point1, point2 in self.lines:
			status = gdiplus.GdipDrawLineI(graphics, self.pen_lines, point1.x, point1.y, point2.x, point2.y)

	def draw_lines_2(self, graphics):
		status = gdiplus.GdipDrawLinesI(graphics, self.pen_lines, self.lines, len(self.lines))

	def draw_lines(self, graphics):
		'fast drawing lines'
		status = gdiplus.GdipDrawPath(graphics, self.pen_lines, self.path_lines)

	def draw_points_1(self, graphics):
		size_point = int(self.size_point)
		d = int(self.size_point / 2)
		for rect in self.cells:
			status = gdiplus.GdipDrawEllipseI(graphics, self.pen_points, rect.left - d, rect.top - d, size_point, size_point)

	def draw_points(self, graphics):
		'fast drawing points'
		status = gdiplus.GdipDrawPath(graphics, self.pen_points, self.path_points)

	def draw(self, graphics):
		self.draw_current_cell(graphics)
		if self.is_draw_lines:
			self.draw_lines(graphics)
		if self.is_draw_points:
			self.draw_points(graphics)

	def __del__(self):
		if self.pen_cell:
			gdiplus.GdipDeletePen(self.pen_cell)
		if self.pen_lines:
			gdiplus.GdipDeletePen(self.pen_lines)
		if self.pen_points:
			gdiplus.GdipDeletePen(self.pen_points)

class main_window(Window):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)
	color_background = gdiplus.MakeARGB(255, 155, 155, 255)
	#~ grid = live_grid_2d(cellw = 64, cellh = 64, size_point = 5.0)
	grid = live_grid_2d()#is_draw_points = False

	def OnDestroy(self, event):
		application.Quit()

	def OnPaint(self, event):
		ps = PAINTSTRUCT()
		ps.fErase = True
		hdc = self.BeginPaint(ps)
		rect = self.GetClientRect()
		status, graphics = gdiplus.GdipCreateFromHDC(hdc)
		status = gdiplus.GdipGraphicsClear(graphics, self.color_background)
		self.grid.draw(graphics)
		gdiplus.GdipDeleteGraphics(graphics)
		self.EndPaint(ps)

	def OnSize(self, event):
		self.grid.screen_size = POINT(*event.size)
		self.grid.create_cells()
		self.grid.create_lines()

	def OnCreate(self, event):
		if not self.grid.path_lines:
			status, self.grid.path_lines = gdiplus.GdipCreatePath()
		if not self.grid.path_points:
			status, self.grid.path_points = gdiplus.GdipCreatePath()
		self.grid.create_brush_cell()
		self.grid.create_pen_cell()
		self.grid.create_pen_lines()
		self.grid.create_pen_points()

	def OnMouseMove(self, event):
		self.mouse_event = True
		self.grid.current_point = GET_POINT_LPARAM(event.lParam)
		if self.grid.is_cell_changed():
			hdc = self.GetDC()
			status, graphics = gdiplus.GdipCreateFromHDC(hdc)
			clip_rect = self.grid.current_cell + self.grid.old_cell
			status = gdiplus.GdipSetClipRectI(graphics, clip_rect.left, clip_rect.top, clip_rect.width, clip_rect.height, gdiplus.CombineModeReplace)
			status = gdiplus.GdipGraphicsClear(graphics, self.color_background)
			self.grid.draw(graphics)
			gdiplus.GdipDeleteGraphics(graphics)
			self.ReleaseDC(hdc)

	msg_handler(WM_DESTROY)(OnDestroy)
	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_SIZE)(OnSize)
	msg_handler(WM_MOUSEMOVE)(OnMouseMove)
	msg_handler(WM_CREATE)(OnCreate)

if __name__ == '__main__':
	# Initialize GDI+
	gdiplusToken = pointer(c_ulong())
	startup_input = gdiplus.GdiplusStartupInput(1, cast(None, gdiplus.DebugEventProc), False, False)
	gdiplus.GdiplusStartup(byref(gdiplusToken), startup_input, None)

	mw = main_window(rcPos = RECT(0, 0, 320, 240))
	application = Application()
	application.Run()

	# Shutdown GDI+
	gdiplus.GdiplusShutdown(gdiplusToken)
