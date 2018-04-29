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

from version_microsoft import WINVER
from sdkddkver import _WIN32_WINNT, _WIN32_WINNT_WIN2K

# Graphics Modes
GM_COMPATIBLE = 1
GM_ADVANCED   = 2
GM_LAST       = 2

# PolyDraw and GetPath point types
PT_CLOSEFIGURE = 0x01
PT_LINETO      = 0x02
PT_BEZIERTO    = 0x04
PT_MOVETO      = 0x06

# Mapping Modes
MM_TEXT        = 1
MM_LOMETRIC    = 2
MM_HIMETRIC    = 3
MM_LOENGLISH   = 4
MM_HIENGLISH   = 5
MM_TWIPS       = 6
MM_ISOTROPIC   = 7
MM_ANISOTROPIC = 8

# Min and Max Mapping Mode values
MM_MIN            = MM_TEXT
MM_MAX            = MM_ANISOTROPIC
MM_MAX_FIXEDSCALE = MM_TWIPS

# Coordinate Modes
ABSOLUTE = 1
RELATIVE = 2

# Stock Logical Objects
WHITE_BRUSH        = 0
LTGRAY_BRUSH       = 1
GRAY_BRUSH         = 2
DKGRAY_BRUSH       = 3
BLACK_BRUSH        = 4
NULL_BRUSH         = 5
HOLLOW_BRUSH       = NULL_BRUSH
WHITE_PEN          = 6
BLACK_PEN          = 7
NULL_PEN           = 8
OEM_FIXED_FONT     = 10
ANSI_FIXED_FONT    = 11
ANSI_VAR_FONT      = 12
SYSTEM_FONT        = 13
DEVICE_DEFAULT_FONT= 14
DEFAULT_PALETTE    = 15
SYSTEM_FIXED_FONT  = 16
if WINVER >= 0x0400:
	DEFAULT_GUI_FONT = 17
if _WIN32_WINNT >= _WIN32_WINNT_WIN2K:
	DC_BRUSH = 18
	DC_PEN = 19
if _WIN32_WINNT >= _WIN32_WINNT_WIN2K:
	STOCK_LAST = 19
elif WINVER >= 0x0400:
	STOCK_LAST = 17
else:
	STOCK_LAST = 16

from ctypes import *
from windows import *
from wtl import *

RASTER_FONTTYPE   = 0x0001
DEVICE_FONTTYPE   = 0x002
TRUETYPE_FONTTYPE = 0x004

def RGB(r,g,b):
    return r | (g<<8) | (b<<16)

def PALETTERGB(r,g,b):
    return 0x02000000 | RGB(r,g,b)

def PALETTEINDEX(i):
    return 0x01000000 | i

class BITMAP(Structure):
    _fields_ = [("bmType", LONG),
    		("bmWidth", LONG),
    		("bmHeight", LONG),
    		("bmWidthBytes", LONG),
    		("bmPlanes", WORD),
    		("bmBitsPixel", WORD),
    		("bmBits", LPVOID)]

LF_FACESIZE = 32

class LOGFONT(Structure):
    _fields_ = [("lfHeight", LONG),
                ("lfWidth", LONG),                
                ("lfEscapement", LONG),
                ("lfOrientation", LONG),
                ("lfWeight", LONG),
                ("lfItalic", BYTE),
                ("lfUnderline", BYTE),
                ("lfStrikeOut", BYTE),
                ("lfCharSet", BYTE),
                ("lfOutPrecision", BYTE),
                ("lfClipPrecision", BYTE),
                ("lfQuality", BYTE), 
                ("lfPitchAndFamily", BYTE),
                ("lfFaceName", TCHAR * LF_FACESIZE)]

class LOGBRUSH(Structure):
    _fields_ = [("lbStyle", UINT),
                ("lbColor", COLORREF),
                ("lbHatch", LONG)]
    
class ENUMLOGFONTEX(Structure):
    _fields_ = [("elfLogFont", LOGFONT),
                ("elfFullName", TCHAR * LF_FACESIZE),
                ("elfStyle", TCHAR * LF_FACESIZE),
                ("elfScript", TCHAR * LF_FACESIZE)]

EnumFontFamExProc = WINFUNCTYPE(c_int, POINTER(ENUMLOGFONTEX), POINTER(DWORD), DWORD, LPARAM)    

class BITMAPINFOHEADER(Structure):
    _fields_ = [("biSize",  DWORD),
                ("biWidth",   LONG),
                ("biHeight",   LONG),
                ("biPlanes",   WORD),
                ("biBitCount",   WORD),
                ("biCompression",  DWORD),
                ("biSizeImage",  DWORD),
                ("biXPelsPerMeter",   LONG),
                ("biYPelsPerMeter",   LONG),
                ("biClrUsed",  DWORD),
                ("biClrImportant",  DWORD)]

class RGBQUAD(Structure):
  _fields_ = [("rgbBlue",    BYTE),
              ("rgbGreen",    BYTE),
              ("rgbRed",    BYTE),
              ("rgbReserved",    BYTE)]

class BITMAPINFO(Structure):
    _fields_ = [("bmiHeader", BITMAPINFOHEADER),
                ("bmiColors", RGBQUAD)]

class BITMAPFILEHEADER(Structure):
    _fields_ = [
        ("bfType",    WORD),
        ("bfSize",   DWORD),
        ("bfReserved1",    WORD),
        ("bfReserved2",    WORD),
        ("bfOffBits",   DWORD)]

class DISPLAY_DEVICE(Structure):
	_fields_ = [
	('cb', DWORD),
	('DeviceName', c_wchar * 32),
	('DeviceString', c_wchar * 128),
	('StateFlags', DWORD),
	('DeviceID', c_wchar * 128),
	('DeviceKey', c_wchar * 128)]
HDC = POINTER(DISPLAY_DEVICE)

COLOR16 = c_ushort
class TRIVERTEX(Structure):
	_fields_ = [
	('x', c_long),
	('y', c_long),
	('Red', COLOR16),
	('Green', COLOR16),
	('Blue', COLOR16),
	('Alpha', COLOR16)]
PTRIVERTEX = POINTER(TRIVERTEX)

class GRADIENT_RECT(Structure):
	_fields_ = [
	('UpperLeft', c_ulong),
	('LowerRight', c_ulong)]

MONO_FONT = 8
OBJ_FONT = 6
ANSI_FIXED_FONT  = 11
ANSI_VAR_FONT = 12
DEVICE_DEFAULT_FONT= 14
DEFAULT_GUI_FONT= 17
OEM_FIXED_FONT= 10
SYSTEM_FONT= 13
SYSTEM_FIXED_FONT= 16

ANSI_CHARSET          =  0
DEFAULT_CHARSET       =  1
SYMBOL_CHARSET        =  2
SHIFTJIS_CHARSET      =  128
HANGEUL_CHARSET       =  129
HANGUL_CHARSET        =  129
GB2312_CHARSET        =  134
CHINESEBIG5_CHARSET   =  136
OEM_CHARSET           =  255

FIXED_PITCH = 1

CLR_NONE = 0xffffffff

HS_BDIAGONAL   =3
HS_CROSS       =4
HS_DIAGCROSS   =5
HS_FDIAGONAL   =2
HS_HORIZONTAL  =0
HS_VERTICAL    =1

PATINVERT     =  0x5A0049

OUT_DEFAULT_PRECIS  =  0
CLIP_DEFAULT_PRECIS  = 0
DEFAULT_QUALITY      =  0
DEFAULT_PITCH        =  0

FF_DONTCARE   =  (0<<4)
FF_MODERN     =  (3<<4)

PS_GEOMETRIC=   65536
PS_COSMETIC  =  0
PS_ALTERNATE  = 8
PS_SOLID      = 0
PS_DASH       = 1
PS_DOT= 2
PS_DASHDOT    = 3
PS_DASHDOTDOT = 4
PS_NULL       = 5
PS_USERSTYLE  = 7
PS_INSIDEFRAME= 6
PS_ENDCAP_ROUND =       0
PS_ENDCAP_SQUARE=       256
PS_ENDCAP_FLAT= 512
PS_JOIN_BEVEL = 4096
PS_JOIN_MITER = 8192
PS_JOIN_ROUND = 0
PS_STYLE_MASK = 15
PS_ENDCAP_MASK= 3840
PS_TYPE_MASK  = 983040

BS_SOLID     =  0
BS_NULL       = 1
BS_HOLLOW     = 1
BS_HATCHED    = 2
BS_PATTERN    = 3
BS_INDEXED    = 4
BS_DIBPATTERN = 5
BS_DIBPATTERNPT =       6
BS_PATTERN8X8 = 7
BS_DIBPATTERN8X8 =      8

BI_RGB        =0
BI_RLE8       =1
BI_RLE4       =2
BI_BITFIELDS  =3
BI_JPEG       =4
BI_PNG        =5

DIB_RGB_COLORS   =   0
DIB_PAL_COLORS   =   1

GetStockObject = windll.gdi32.GetStockObject
LineTo = windll.gdi32.LineTo
MoveToEx = windll.gdi32.MoveToEx
FillRect = windll.user32.FillRect
DrawEdge = windll.user32.DrawEdge
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
CreateCompatibleDC.restype = ValidHandle
SelectObject = windll.gdi32.SelectObject
GetObject = windll.gdi32.GetObjectA
DeleteObject = windll.gdi32.DeleteObject
BitBlt = windll.gdi32.BitBlt
StretchBlt = windll.gdi32.StretchBlt
GetSysColorBrush = windll.user32.GetSysColorBrush
CreateHatchBrush = windll.gdi32.CreateHatchBrush
CreatePatternBrush = windll.gdi32.CreatePatternBrush
CreateSolidBrush = windll.gdi32.CreateSolidBrush
CreateBitmap = windll.gdi32.CreateBitmap
PatBlt = windll.gdi32.PatBlt
CreateFont = windll.gdi32.CreateFontA
EnumFontFamiliesEx = windll.gdi32.EnumFontFamiliesExA
InvertRect = windll.user32.InvertRect
DrawFocusRect = windll.user32.DrawFocusRect
ExtCreatePen = windll.gdi32.ExtCreatePen
CreatePen = windll.gdi32.CreatePen
DrawText = windll.user32.DrawTextA
TextOut = windll.gdi32.TextOutA
CreateDIBSection = windll.gdi32.CreateDIBSection
DeleteDC = windll.gdi32.DeleteDC
GetDIBits = windll.gdi32.GetDIBits

ExcludeClipRect = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int)(('ExcludeClipRect', windll.gdi32))
IntersectClipRect = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int)(('IntersectClipRect', windll.gdi32))

SetTextColor = WINFUNCTYPE(COLORREF, c_void_p, COLORREF)(('SetTextColor', windll.gdi32))
if WINVER >= 0x0500:
	SetDCBrushColor = WINFUNCTYPE(COLORREF, c_void_p, COLORREF)(('SetDCBrushColor', windll.gdi32))
	SetDCPenColor = WINFUNCTYPE(COLORREF, c_void_p, COLORREF)(('SetDCPenColor', windll.gdi32))
	#~ SetDCBrushColor = WINFUNCTYPE(COLORREF, HDC, COLORREF)(('SetDCBrushColor', windll.gdi32))
	#~ SetDCPenColor = WINFUNCTYPE(COLORREF, HDC, COLORREF)(('SetDCPenColor', windll.gdi32))

GRADIENT_FILL_RECT_H   = 0x00000000
GRADIENT_FILL_RECT_V   = 0x00000001
GRADIENT_FILL_TRIANGLE = 0x00000002
GRADIENT_FILL_OP_FLAG  = 0x000000ff

if WINVER >= 0x0500:
	GdiGradientFill = WINFUNCTYPE(c_byte, c_void_p, PTRIVERTEX, c_ulong, c_void_p, c_ulong, c_ulong)(('GdiGradientFill', windll.gdi32))
	GradientFill = GdiGradientFill# for backward compatibility
else:
	GradientFill = WINFUNCTYPE(c_byte, c_void_p, PTRIVERTEX, c_ulong, c_void_p, c_ulong, c_ulong)(('GradientFill', windll.gdi32))

class XFORM(Structure):
	_fields_ = [('eM11', c_float),
	('eM12', c_float),
	('eM21', c_float),
	('eM22', c_float),
	('eDx', c_float),
	('eDy', c_float)]
LPXFORM = POINTER(XFORM)

AngleArc = WINFUNCTYPE(c_bool, c_void_p, c_int, c_int, c_ulong, c_float, c_float)(('AngleArc', windll.gdi32))
AngleArc.__doc__ = '''Draws a line segment and an arc. The line segment is drawn from the current position to the beginning of the arc. The arc is drawn along the perimeter of a circle with the given radius and center. The length of the arc is defined by the given start and sweep angles.
First parameter is handle to the device context. Next parameters x and y of circle's center, circle's radius, start angle, sweep angle.'''
PolyPolyline = WINFUNCTYPE(c_bool, c_void_p, POINTER(POINT), c_void_p, c_ulong)(('PolyPolyline', windll.gdi32))
PolyPolyline.__doc__ = 'Draws multiple series of connected line segments. PolyPolyline(hdc, POINT(2,2), (c_ulong*2)(1, 2), 2)'
_GetWorldTransform = WINFUNCTYPE(c_bool, c_void_p, LPXFORM)(('GetWorldTransform', windll.gdi32))
def GetWorldTransform(hdc):
	'Retrieves the current world-space to page-space transformation.'
	lpXform = XFORM()
	result = _GetWorldTransform(hdc, lpXform)
	return result, lpXform
SetWorldTransform = WINFUNCTYPE(c_bool, c_void_p, LPXFORM)(('SetWorldTransform', windll.gdi32))
SetWorldTransform.__doc__ = 'Sets a two-dimensional linear transformation between world space and page space for the specified device context. This transformation can be used to scale, rotate, shear, or translate graphics output.'
ModifyWorldTransform = WINFUNCTYPE(c_bool, c_void_p, LPXFORM, c_ulong)(('ModifyWorldTransform', windll.gdi32))
CombineTransform = WINFUNCTYPE(c_bool, LPXFORM, LPXFORM, LPXFORM)(('CombineTransform', windll.gdi32))
CreateDIBSection = WINFUNCTYPE(c_void_p, c_void_p, POINTER(BITMAPINFO), c_uint, c_void_p, c_void_p, c_ulong)(('CreateDIBSection', windll.gdi32))

# Paths
AbortPath = WINFUNCTYPE(c_bool, c_void_p)(('AbortPath', windll.gdi32))
AbortPath.__doc__ = 'Closes and discards any paths in the specified device context. Parameter is handle to the device context.'
ArcTo = WINFUNCTYPE(c_bool, c_void_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(('ArcTo', windll.gdi32))
ArcTo.__doc__ = '''Draws an elliptical arc. ArcTo is similar to the Arc function, except that the current position is updated.
The points (nLeftRect, nTopRect) and (nRightRect, nBottomRect) specify the bounding rectangle. An ellipse formed by the specified bounding rectangle defines the curve of the arc.
The arc extends counterclockwise from the point where it intersects the radial line from the center of the bounding rectangle to the (nXRadial1, nYRadial1) point.
The arc ends where it intersects the radial line from the center of the bounding rectangle to the (nXRadial2, nYRadial2) point.
If the starting point and ending point are the same, a complete ellipse is drawn.
A line is drawn from the current position to the starting point of the arc. If no error occurs, the current position is set to the ending point of the arc.
The arc is drawn using the current pen; it is not filled.
Parameters:
hdc - Handle to the device context where drawing takes place.
nLeftRect - Specifies the x-coordinate, in logical units, of the upper-left corner of the bounding rectangle.
nTopRect - Specifies the y-coordinate, in logical units, of the upper-left corner of the bounding rectangle.
nRightRect - Specifies the x-coordinate, in logical units, of the lower-right corner of the bounding rectangle.
nBottomRect - Specifies the y-coordinate, in logical units, of the lower-right corner of the bounding rectangle.
nXRadial1 - Specifies the x-coordinate, in logical units, of the endpoint of the radial defining the starting point of the arc.
nYRadial1 - Specifies the y-coordinate, in logical units, of the endpoint of the radial defining the starting point of the arc.
nXRadial2 - Specifies the x-coordinate, in logical units, of the endpoint of the radial defining the ending point of the arc.
nYRadial2 - Specifies the y-coordinate, in logical units, of the endpoint of the radial defining the ending point of the arc.'''
BeginPath = WINFUNCTYPE(c_bool, c_void_p)(('BeginPath', windll.gdi32))
BeginPath.__doc__ = 'Opens a path bracket in the specified device context. Parameter is handle to the device context.'
CloseFigure = WINFUNCTYPE(c_bool, c_void_p)(('CloseFigure', windll.gdi32))
CloseFigure.__doc__ = 'Close an open figure in a path. Parameter is handle to the device context.'
EndPath = WINFUNCTYPE(c_bool, c_void_p)(('EndPath', windll.gdi32))
EndPath.__doc__ = 'Close a path bracket in the specified device context. Parameter is handle to the device context.'
FillPath = WINFUNCTYPE(c_bool, c_void_p)(('FillPath', windll.gdi32))
FillPath.__doc__ = '''Close any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.. Parameter is handle to the device context that contains a valid path.'''
FlattenPath = WINFUNCTYPE(c_bool, c_void_p)(('FlattenPath', windll.gdi32))
FlattenPath.__doc__ = 'Transforms any curves in the path that is selected into the current device context (DC), turning each curve into a sequence of lines. Parameter is handle to the device context that contains a valid path.'
GetPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GetPath', windll.gdi32))
GetPath.__doc__ = 'Retrieves the coordinates defining the endpoints of lines and the control points of curves found in the path that is selected into the specified device context.'
PathToRegion = WINFUNCTYPE(HRGN, c_void_p)(('PathToRegion', windll.gdi32))
PathToRegion.__doc__ = 'Creates a region from the path that is selected into the specified device context. The resulting region uses device coordinates.'
PolyDraw = WINFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p, c_int)(('PolyDraw', windll.gdi32))
PolyDraw.__doc__ = 'Draws a set of line segments and Bezier curves.'
SelectClipPath = WINFUNCTYPE(c_bool, c_void_p, c_int)(('SelectClipPath', windll.gdi32))
SelectClipPath.__doc__ = 'Selects the current path as a clipping region for a device context, combining the new region with any existing clipping region using the specified mode.'
SetArcDirection = WINFUNCTYPE(c_int, c_void_p, c_int)(('SetArcDirection', windll.gdi32))
SetArcDirection.__doc__ = 'Sets the drawing direction to be used for arc and rectangle functions.'
_SetMiterLimit = WINFUNCTYPE(c_bool, c_void_p, c_float, c_void_p)(('SetMiterLimit', windll.gdi32))
def SetMiterLimit(hdc, eNewLimit):
	'Sets the limit for the length of miter joins for the specified device context.'
	peOldLimit = c_float()
	result = _SetMiterLimit(hdc, eNewLimit, byref(peOldLimit))
	return result, peOldLimit.value
StrokeAndFillPath = WINFUNCTYPE(c_bool, c_void_p)(('StrokeAndFillPath', windll.gdi32))
StrokeAndFillPath.__doc__ = 'Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush. Parameter is handle to the device context.'
StrokePath = WINFUNCTYPE(c_bool, c_void_p)(('StrokePath', windll.gdi32))
StrokePath.__doc__ = 'Renders the specified path by using the current pen. Parameter is handle to the device context.'
WidenPath = WINFUNCTYPE(c_bool, c_void_p)(('WidenPath', windll.gdi32))
WidenPath.__doc__ = 'Redefines the current path as the area that would be painted if the path were stroked using the pen currently selected into the given device context. Parameter is handle to the device context.'
ExtCreatePen = WINFUNCTYPE(c_void_p, c_ulong, c_ulong, c_void_p, c_ulong, c_void_p)(('ExtCreatePen', windll.gdi32))
ExtCreatePen.__doc__ = 'Creates a logical cosmetic or geometric pen that has the specified style, width, and brush attributes.'
_GetMiterLimit = WINFUNCTYPE(c_bool, c_void_p, c_void_p)(('GetMiterLimit', windll.gdi32))
def CetMiterLimit(hdc):
	'Retrieves the miter limit for the specified device context.'
	peLimit = c_float()
	result = _GetMiterLimit(hdc, byref(peLimit))
	return result, peLimit.value
GetArcDirection = WINFUNCTYPE(c_int, c_void_p)(('GetArcDirection', windll.gdi32))
GetArcDirection.__doc__ = 'Retrieves the current arc direction for the specified device context. Arc and rectangle functions use the arc direction. Parameter is handle to the device context.'

# Coordinate Space and Transformation Functions
DPtoLP = WINFUNCTYPE(c_bool, c_void_p, LPPOINT, c_int)(('DPtoLP', windll.gdi32))
DPtoLP.__doc__ = 'Converts device coordinates into logical coordinates. The conversion depends on the mapping mode of the device context, the settings of the origins and extents for the window and viewport, and the world transformation.'
LPtoDP = WINFUNCTYPE(c_bool, c_void_p, LPPOINT, c_int)(('LPtoDP', windll.gdi32))
LPtoDP.__doc__ = 'Converts logical coordinates into device coordinates. The conversion depends on the mapping mode of the device context, the settings of the origins and extents for the window and viewport, and the world transformation.'
SetGraphicsMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('SetGraphicsMode', windll.gdi32))
SetGraphicsMode.__doc__ = 'Sets the graphics mode for the specified device context.'
SetMapMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('SetMapMode', windll.gdi32))
SetMapMode.__doc__ = '''Sets the mapping mode of the specified device context. The mapping mode defines the unit of measure used to transform page-space units into device-space units, and also defines the orientation of the device's x and y axes.'''


class Bitmap(WindowsObject):
    __dispose__ = DeleteObject

    def __init__(self, path):
        WindowsObject.__init__(self, LoadImage(NULL, path, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE))
        bm = BITMAP()
        GetObject(self.handle, sizeof(bm), byref(bm))
        self.m_width, self.m_height = bm.bmWidth, bm.bmHeight

    def getWidth(self):
        return self.m_width

    width = property(getWidth, None, None, "")
    
    def getHeight(self):
        return self.m_height

    height = property(getHeight, None, None, "")
        


#TODO refactor into Brush class with static factory class methods
class SolidBrush(WindowsObject):
    __dispose__ = DeleteObject

    def __init__(self, colorRef):
        WindowsObject.__init__(self, CreateSolidBrush(colorRef))
        
class Pen(WindowsObject):
    __dispose__ = DeleteObject

    def Create(cls, fnPenStyle = PS_SOLID,  nWidth = 1, crColor = 0x00000000):
        return Pen(CreatePen(fnPenStyle, nWidth, crColor))

    Create = classmethod(Create)
    
    def CreateEx(cls, dwPenStyle = PS_COSMETIC | PS_SOLID, dwWidth = 1, lbStyle = BS_SOLID,
                 lbColor = 0x00000000, lbHatch = 0,
                 dwStyleCount = 0, lpStyle = 0):
        lb = LOGBRUSH(lbStyle, lbColor, lbHatch)
        return Pen(ExtCreatePen(dwPenStyle, dwWidth, byref(lb), dwStyleCount, lpStyle))

    CreateEx  = classmethod(CreateEx)
    

class Font(WindowsObject):
    __dispose__ = DeleteObject

    def __init__(self, **kwargs):
        #TODO move these kwargs to init, use default values
        hfont = CreateFont(kwargs.get('height', 0),
                           kwargs.get('width', 0),
                           kwargs.get('escapement', 0),
                           kwargs.get('orientation', 0),
                           kwargs.get('weight', 0),
                           kwargs.get('italic', 0),
                           kwargs.get('underline', 0),
                           kwargs.get('strikeout', 0),
                           kwargs.get('charset', ANSI_CHARSET),
                           kwargs.get('outputPrecision', OUT_DEFAULT_PRECIS),
                           kwargs.get('clipPrecision', CLIP_DEFAULT_PRECIS),
                           kwargs.get('quality', DEFAULT_QUALITY),
                           kwargs.get('pitchAndFamily', DEFAULT_PITCH|FF_DONTCARE),
                           kwargs.get('face', ""))
        WindowsObject.__init__(self, hfont)

