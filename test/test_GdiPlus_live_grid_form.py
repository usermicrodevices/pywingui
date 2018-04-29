'GdiPlus live grid based on pyWinGUI (Maxim Kolosov)'

from os import getcwd

from pywingui import gdiplusflat as gdiplus
from pywingui import gdi
from pywingui.wtl import *
from pywingui.lib import form
from pywingui.comdlg import OpenFileDialog
from pywingui.shell import ExtractIcon, ExtractIconEx
from pywingui.winuser import LoadCursorFromFile

OPERATION_EMPTY = 0
OPERATION_PASTE_IMAGE = 1
OPERATION_DELETE_IMAGE = 2

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
		self.container_images = {}
		self.current_image = (None, '')

	def add_current_image(self):
		self.container_images[(self.current_cell.left, self.current_cell.top)] = self.current_image

	def delete_image(self):
		if (self.current_cell.left, self.current_cell.top) in self.container_images:
			del self.container_images[(self.current_cell.left, self.current_cell.top)]

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

	def create_brush_cell(self):
		if self.brush_cell:
			status = gdiplus.GdipDeleteBrush(self.brush_cell)
		status, self.brush_cell = gdiplus.GdipCreateSolidFill(self.color_active_cell)
		return status

	def create_pen_cell(self):
		if self.pen_cell:
			status = gdiplus.GdipDeletePen(self.pen_cell)
		status, self.pen_cell = gdiplus.GdipCreatePen1(self.color_active_cell, 16.0)
		return status

	def create_pen_lines(self):
		if self.pen_lines:
			status = gdiplus.GdipDeletePen(self.pen_lines)
		status, self.pen_lines = gdiplus.GdipCreatePen1(self.color_line, self.width_line)
		return status

	def create_pen_points(self):
		if self.pen_points:
			status = gdiplus.GdipDeletePen(self.pen_points)
		status, self.pen_points = gdiplus.GdipCreatePen1(self.color_points, self.size_point)
		return status

	def create_pens(self):
		self.create_pen_cell()
		self.create_pen_lines()
		self.create_pen_points()

	def draw_current_cell(self, graphics):
		if self.current_image[0]:
			status = gdiplus.GdipDrawImageRect(graphics, self.current_image[0], self.current_cell.left, self.current_cell.top, self.cellw, self.cellh)
		status = gdiplus.GdipFillRectangle(graphics, self.brush_cell, self.current_cell.left, self.current_cell.top, self.cellw, self.cellh)

	def draw_lines(self, graphics):
		status = gdiplus.GdipDrawPath(graphics, self.pen_lines, self.path_lines)

	def draw_points(self, graphics):
		status = gdiplus.GdipDrawPath(graphics, self.pen_points, self.path_points)

	def draw_images(self, graphics):
		for key, image in self.container_images.iteritems():
			status = gdiplus.GdipDrawImageRect(graphics, image[0], key[0], key[1], self.cellw, self.cellh)

	def draw(self, graphics):
		self.draw_images(graphics)
		self.draw_current_cell(graphics)
		if self.is_draw_lines:
			self.draw_lines(graphics)
		if self.is_draw_points:
			self.draw_points(graphics)

	def __del__(self):
		if self.brush_cell:
			status = gdiplus.GdipDeleteBrush(self.brush_cell)
		if self.pen_cell:
			status = gdiplus.GdipDeletePen(self.pen_cell)
		if self.pen_lines:
			status = gdiplus.GdipDeletePen(self.pen_lines)
		if self.pen_points:
			status = gdiplus.GdipDeletePen(self.pen_points)

class main_window(form.Form):
	_window_title_ = __doc__
	_window_background_ = gdi.GetStockObject(gdi.LTGRAY_BRUSH)
	_window_icon_ = _window_icon_sm_ = Icon(lpIconName = IDI_ASTERISK)
	color_background = gdiplus.MakeARGB(255, 155, 155, 255)
	grid = live_grid_2d(cellw = 64, cellh = 64, size_point = 5.0)
	current_operation = OPERATION_EMPTY
	color_active_cell_paste = grid.color_active_cell
	current_open_dir = getcwd()
	current_open_filter_index = 1

	_form_menu_ = [(MF_POPUP, "&File",
					[(MF_STRING, "&New Grid\tCtrl+N", form.ID_NEW),
					(MF_STRING, "&Open Image\tCtrl+O", form.ID_OPEN),
					(MF_SEPARATOR,),
					(MF_STRING, "&Exit", form.ID_EXIT)]),
					(MF_POPUP, "&Edit",
					[(MF_STRING, "&Undo\tCtrl+Z", form.ID_UNDO),
					(MF_STRING, "&Redo\tCtrl+Y", form.ID_REDO),
					(MF_SEPARATOR,),
					(MF_STRING, "Cu&t\tCtrl+X", form.ID_CUT),
					(MF_STRING, "&Copy\tCtrl+C", form.ID_COPY),
					(MF_STRING, "&Paste\tCtrl+V", form.ID_PASTE),
					(MF_STRING, "&Delete\tDel", form.ID_CLEAR),
					(MF_SEPARATOR,),
					(MF_STRING, "Select &All\tCtrl+A", form.ID_SELECTALL)])
					]

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
		self.current_operation = OPERATION_PASTE_IMAGE

	def OnLButtonUp(self, event):
		if self.current_operation == OPERATION_PASTE_IMAGE:
			self.grid.add_current_image()
		if self.current_operation == OPERATION_DELETE_IMAGE:
			self.grid.delete_image()

	def OnMouseMove(self, event):
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

	def OnOpenImage(self, event):
		dlg = OpenFileDialog()
		dlg.lpstrInitialDir = getcwd()
		dlg.lpstrInitialDir = self.current_open_dir
		dlg.nFilterIndex = self.current_open_filter_index
		dlg.SetFilter('BMP Image(*.bmp)|*.bmp|PNG Image(*.png)|*.png|JPG Image(*.jpg)|*.jpg|GIF Image(*.gif)|*.gif|Icon Image(*.ico)|*.ico|Cursor Image(*.cur)|*.cur|EMF Image(*.emf)|*.emf|WMF Image(*.wmf)|*.wmf|All files(*.*)|*.*')
		if dlg.DoModal(self):
			self.current_open_dir = dlg.lpstrFile
			self.current_open_filter_index = dlg.nFilterIndex
			status = -1
			if dlg.nFilterIndex == 1:#BMP
				status, image = gdiplus.GdipCreateBitmapFromFile(dlg.lpstrFile)
			elif dlg.nFilterIndex in (5, 6):#ICO#CUR
				hicon = ExtractIcon(None, dlg.lpstrFile, 0)
				if hicon:
					status, image = gdiplus.GdipCreateBitmapFromHICON(hicon)
			else:
				status, image = gdiplus.GdipLoadImageFromFile(dlg.lpstrFile)
			if status == gdiplus.Ok:
				self.grid.current_image = (image, dlg.lpstrFile)
				self.set_paste_property()

	def set_paste_property(self):
		self.current_operation = OPERATION_PASTE_IMAGE
		self.grid.color_active_cell = self.color_active_cell_paste
		self.grid.create_brush_cell()

	def OnGetClear(self, event):
		self.grid.current_image = (None, '')
		self.current_operation = OPERATION_DELETE_IMAGE
		self.grid.color_active_cell = gdiplus.MakeARGB(128, 255, 0, 0)
		self.grid.create_brush_cell()

	cmd_handler(form.ID_OPEN)(OnOpenImage)
	cmd_handler(form.ID_CLEAR)(OnGetClear)

	msg_handler(WM_DESTROY)(OnDestroy)
	msg_handler(WM_PAINT)(OnPaint)
	msg_handler(WM_SIZE)(OnSize)
	msg_handler(WM_LBUTTONUP)(OnLButtonUp)
	msg_handler(WM_MOUSEMOVE)(OnMouseMove)
	msg_handler(WM_CREATE)(OnCreate)

if __name__ == '__main__':
	# Initialize GDI+
	gdiplusToken = pointer(c_ulong())
	startup_input = gdiplus.GdiplusStartupInput(1, cast(None, gdiplus.DebugEventProc), False, False)
	gdiplus.GdiplusStartup(byref(gdiplusToken), startup_input, None)

	mw = main_window(rcPos = RECT(0, 0, 640, 480))
	application = Application()
	application.Run()

	# Shutdown GDI+
	gdiplus.GdiplusShutdown(gdiplusToken)
