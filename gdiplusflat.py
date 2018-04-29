# gdiplusflat.py created from gdiplusflat.h
# Copyright (c) 2012 Maxim Kolosov

GDIPVER = 0x0100

# enum Status
Status = 0
Ok = 0
GenericError = 1
InvalidParameter = 2
OutOfMemory = 3
ObjectBusy = 4
InsufficientBuffer = 5
NotImplemented = 6
Win32Error = 7
WrongState = 8
Aborted = 9
FileNotFound = 10
ValueOverflow = 11
AccessDenied = 12
UnknownImageFormat = 13
FontFamilyNotFound = 14
FontStyleNotFound = 15
NotTrueTypeFont = 16
UnsupportedGdiplusVersion = 17
GdiplusNotInitialized = 18
PropertyNotFound = 19
PropertyNotSupported = 20
ProfileNotFound = 21#if GDIPVER >= 0x0110:

container_status = {Ok:'Ok',
GenericError:'GenericError',
InvalidParameter:'InvalidParameter',
OutOfMemory:'OutOfMemory',
ObjectBusy:'ObjectBusy',
InsufficientBuffer:'InsufficientBuffer',
NotImplemented:'NotImplemented',
Win32Error:'Win32Error',
WrongState:'WrongState',
Aborted:'Aborted',
FileNotFound:'FileNotFound',
ValueOverflow:'ValueOverflow',
AccessDenied:'AccessDenied',
UnknownImageFormat:'UnknownImageFormat',
FontFamilyNotFound:'FontFamilyNotFound',
FontStyleNotFound:'FontStyleNotFound',
NotTrueTypeFont:'NotTrueTypeFont',
UnsupportedGdiplusVersion:'UnsupportedGdiplusVersion',
GdiplusNotInitialized:'GdiplusNotInitialized',
PropertyNotFound:'PropertyNotFound',
PropertyNotSupported:'PropertyNotSupported',
ProfileNotFound:'ProfileNotFound'}

def status_as_string(status):
	try:
		return container_status[status]
	except:
		return 'UNKNOWN STATUS %d' % status

# enum Unit constants
#Unit = 0
UnitWorld = 0# World coordinate (non-physical unit)
UnitDisplay = 1# Variable -- for PageTransform only
UnitPixel = 2# Each unit is one device pixel.
UnitPoint = 3# Each unit is a printer's point, or 1/72 inch.
UnitInch = 4# Each unit is 1 inch.
UnitDocument = 5# Each unit is 1/300 inch.
UnitMillimeter = 6# Each unit is 1 millimeter.

# enum GdiplusStartupParams
GdiplusStartupParams = 0
GdiplusStartupDefault = 0
GdiplusStartupNoSetRound = 1
GdiplusStartupSetPSValue = 2
GdiplusStartupTransparencyMask = 0xFF000000

AlphaShift  = 24
RedShift    = 16
GreenShift  = 8
BlueShift   = 0

AlphaMask = 0xff000000
RedMask   = 0x00ff0000
GreenMask = 0x0000ff00
BlueMask  = 0x000000ff

HatchStyle = 0
HatchStyleHorizontal = 0
HatchStyleVertical = 1
HatchStyleForwardDiagonal = 2
HatchStyleBackwardDiagonal = 3
HatchStyleCross = 4
HatchStyleDiagonalCross = 5
HatchStyle05Percent = 6
HatchStyle10Percent = 7
HatchStyle20Percent = 8
HatchStyle25Percent = 9
HatchStyle30Percent = 10
HatchStyle40Percent = 11
HatchStyle50Percent = 12
HatchStyle60Percent = 13
HatchStyle70Percent = 14
HatchStyle75Percent = 15
HatchStyle80Percent = 16
HatchStyle90Percent = 17
HatchStyleLightDownwardDiagonal = 18
HatchStyleLightUpwardDiagonal = 19
HatchStyleDarkDownwardDiagonal = 20
HatchStyleDarkUpwardDiagonal = 21
HatchStyleWideDownwardDiagonal = 22
HatchStyleWideUpwardDiagonal = 23
HatchStyleLightVertical = 24
HatchStyleLightHorizontal = 25
HatchStyleNarrowVertical = 26
HatchStyleNarrowHorizontal = 27
HatchStyleDarkVertical = 28
HatchStyleDarkHorizontal = 29
HatchStyleDashedDownwardDiagonal = 30
HatchStyleDashedUpwardDiagonal = 31
HatchStyleDashedHorizontal = 32
HatchStyleDashedVertical = 33
HatchStyleSmallConfetti = 34
HatchStyleLargeConfetti = 35
HatchStyleZigZag = 36
HatchStyleWave = 37
HatchStyleDiagonalBrick = 38
HatchStyleHorizontalBrick = 39
HatchStyleWeave = 40
HatchStylePlaid = 41
HatchStyleDivot = 42
HatchStyleDottedGrid = 43
HatchStyleDottedDiamond = 44
HatchStyleShingle = 45
HatchStyleTrellis = 46
HatchStyleSphere = 47
HatchStyleSmallGrid = 48
HatchStyleSmallCheckerBoard = 49
HatchStyleLargeCheckerBoard = 50
HatchStyleOutlinedDiamond = 51
HatchStyleSolidDiamond = 52
HatchStyleTotal = 53
HatchStyleLargeGrid = HatchStyleCross
HatchStyleMin = HatchStyleHorizontal
HatchStyleMax = HatchStyleTotal - 1

WrapMode = 0
WrapModeTile = 0
WrapModeTileFlipX = 1
WrapModeTileFlipY = 2
WrapModeTileFlipXY = 3
WrapModeClamp = 4

#GpMatrixOrder
MatrixOrderPrepend = 0
MatrixOrderAppend = 1

#enum CombineMode
CombineModeReplace = 0
CombineModeIntersect = 1
CombineModeUnion = 2
CombineModeXor = 3
CombineModeExclude = 4
CombineModeComplement = 5

def MakeARGB(a, r, g, b):
	return c_ulong((b << BlueShift) | (g << GreenShift) | (r << RedShift) | (a << AlphaShift))

from ctypes import *

GpUnit = c_int
REAL = c_float
ARGB = c_ulong

DebugEventProc = WINFUNCTYPE(None, c_int, c_char_p)
NotificationHookProc = WINFUNCTYPE(c_int, c_void_p)
NotificationUnhookProc = WINFUNCTYPE(None, c_void_p)

class GpPoint(Structure):
	_fields_ = [('x', c_int), ('y', c_int)]

class GpPointF(Structure):
	_fields_ = [('x', REAL), ('y', REAL)]

class GpRect(Structure):
	_fields_ = [("left", c_int), ("top", c_int), ("right", c_int), ("bottom", c_int)]

class GpRectF(Structure):
	_fields_ = [('x', REAL), ('y', REAL), ('width', REAL), ('height', REAL)]

#~ class GpMatrix(Structure):
	#~ _fields_ = [('m11', REAL), ('m12', REAL), ('m21', REAL), ('m22', REAL), ('dx', REAL), ('dy', REAL)]

class GdiplusStartupInput(Structure):
	'startup_input = GdiplusStartupInput(1, None, False, False)'
	_fields_ = [('GdiplusVersion', c_uint),
	('DebugEventCallback', DebugEventProc),
	('SuppressBackgroundThread', c_bool),
	('SuppressExternalCodecs', c_bool)]

class GdiplusStartupOutput(Structure):
	_fields_ = [('NotificationHook', NotificationHookProc),
	('NotificationUnhook', NotificationUnhookProc)]

#extern "C" Status WINAPI GdiplusStartup(OUT ULONG_PTR *token, const GdiplusStartupInput *input, OUT GdiplusStartupOutput *output);
GdiplusStartup = WINFUNCTYPE(c_int, c_void_p, POINTER(GdiplusStartupInput), c_void_p)(('GdiplusStartup', windll.gdiplus))

#extern "C" VOID WINAPI GdiplusShutdown(ULONG_PTR token);
GdiplusShutdown = WINFUNCTYPE(None, c_void_p)(('GdiplusShutdown', windll.gdiplus))


#=========
# GraphicsPath APIs

FillMode = 0
FillModeAlternate = 0
FillModeWinding = 1

#GpStatus WINGDIPAPI GdipCreatePath(GpFillMode brushMode, GpPath **path);
_GdipCreatePath = WINFUNCTYPE(c_int, c_int, c_void_p)(('GdipCreatePath', windll.gdiplus))
def GdipCreatePath(fillMode = 0):
	path = c_void_p()
	status = _GdipCreatePath(fillMode, byref(path))
	return status, path

#GpStatus WINGDIPAPI GdipCreatePath2(GDIPCONST GpPointF*, GDIPCONST BYTE*, INT, GpFillMode, GpPath **path);
_GdipCreatePath2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_void_p)(('GdipCreatePath2', windll.gdiplus))
def GdipCreatePath2(points, types, count, fillMode = 0):
	path = c_void_p()
	status = _GdipCreatePath2(points, types, count, fillMode, byref(path))
	return status, path

#GpStatus WINGDIPAPI GdipCreatePath2I(GDIPCONST GpPoint*, GDIPCONST BYTE*, INT, GpFillMode, GpPath **path);
_GdipCreatePath2I = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_void_p)(('GdipCreatePath2I', windll.gdiplus))
def GdipCreatePath2I(points, types, count, fillMode = 0):
	path = c_void_p()
	status = _GdipCreatePath2I(points, types, count, fillMode, byref(path))
	return status, path

#GpStatus WINGDIPAPI GdipClonePath(GpPath* path, GpPath **clonePath);
_GdipClonePath = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipClonePath', windll.gdiplus))
def GdipClonePath(path):
	clone_path = c_void_p()
	status = _GdipClonePath(path, byref(clone_path))
	return status, clone_path

#GpStatus WINGDIPAPI GdipDeletePath(GpPath* path);
GdipDeletePath = WINFUNCTYPE(c_int, c_void_p)(('GdipDeletePath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipResetPath(GpPath* path);
GdipResetPath = WINFUNCTYPE(c_int, c_void_p)(('GdipResetPath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPointCount(GpPath* path, INT* count);
_GdipGetPointCount = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPointCount', windll.gdiplus))
def GdipGetPointCount(path):
	point_count = c_int()
	status = _GdipGetPointCount(path, byref(point_count))
	return status, point_count.value

#GpStatus WINGDIPAPI GdipGetPathTypes(GpPath* path, BYTE* types, INT count);
_GdipGetPathTypes = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipGetPathTypes', windll.gdiplus))
def GdipGetPathTypes(path, count):
	types = c_void_p()
	status = _GdipGetPathTypes(path, byref(types), count)
	return status, types

#GpStatus WINGDIPAPI GdipGetPathPoints(GpPath*, GpPointF* points, INT count);
_GdipGetPathPoints = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipGetPathPoints', windll.gdiplus))
def GdipGetPathPoints(path, count):
	points = GpPointF()
	status = _GdipGetPathPoints(path, points, count)
	return status, points

#GpStatus WINGDIPAPI GdipGetPathPointsI(GpPath*, GpPoint* points, INT count);
_GdipGetPathPointsI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipGetPathPointsI', windll.gdiplus))
def GdipGetPathPointsI(path, count):
	points = GpPoint()
	status = _GdipGetPathPointsI(path, points, count)
	return status, points

#GpStatus WINGDIPAPI GdipGetPathFillMode(GpPath *path, GpFillMode *fillmode);
_GdipGetPathFillMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPathFillMode', windll.gdiplus))
def GdipGetPathFillMode(path):
	fillmode = c_int()
	status = _GdipGetPathFillMode(path, byref(fillmode))
	return status, fillmode.value

#GpStatus WINGDIPAPI GdipSetPathFillMode(GpPath *path, GpFillMode fillmode);
GdipSetPathFillMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetPathFillMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPathData(GpPath *path, GpPathData* pathData);
_GdipGetPathData = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPathData', windll.gdiplus))
def GdipGetPathData(path):
	pathData = c_void_p()
	status = _GdipGetPathData(path, byref(pathData))
	return status, pathData

#GpStatus WINGDIPAPI GdipStartPathFigure(GpPath *path);
GdipStartPathFigure = WINFUNCTYPE(c_int, c_void_p)(('GdipStartPathFigure', windll.gdiplus))

#GpStatus WINGDIPAPI GdipClosePathFigure(GpPath *path);
GdipClosePathFigure = WINFUNCTYPE(c_int, c_void_p)(('GdipClosePathFigure', windll.gdiplus))

#GpStatus WINGDIPAPI GdipClosePathFigures(GpPath *path);
GdipClosePathFigures = WINFUNCTYPE(c_int, c_void_p)(('GdipClosePathFigures', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetPathMarker(GpPath* path);
GdipSetPathMarker = WINFUNCTYPE(c_int, c_void_p)(('GdipSetPathMarker', windll.gdiplus))

#GpStatus WINGDIPAPI GdipClearPathMarkers(GpPath* path);
GdipClearPathMarkers = WINFUNCTYPE(c_int, c_void_p)(('GdipClearPathMarkers', windll.gdiplus))

#GpStatus WINGDIPAPI GdipReversePath(GpPath* path);
GdipReversePath = WINFUNCTYPE(c_int, c_void_p)(('GdipReversePath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPathLastPoint(GpPath* path, GpPointF* lastPoint);
_GdipGetPathLastPoint = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF))(('GdipGetPathLastPoint', windll.gdiplus))
def GdipGetPathLastPoint(path):
	lastPoint = GpPointF()
	status = _GdipGetPathLastPoint(path, lastPoint)
	return status, lastPoint[0]

#GpStatus WINGDIPAPI GdipAddPathLine(GpPath *path, REAL x1, REAL y1, REAL x2, REAL y2);
GdipAddPathLine = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL)(('GdipAddPathLine', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathLine2(GpPath *path, GDIPCONST GpPointF *points, INT count);
GdipAddPathLine2 = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipAddPathLine2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathArc(GpPath *path, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle);
GdipAddPathArc = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipAddPathArc', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathBezier(GpPath *path, REAL x1, REAL y1, REAL x2, REAL y2, REAL x3, REAL y3, REAL x4, REAL y4);
GdipAddPathBezier = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipAddPathBezier', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathBeziers(GpPath *path, GDIPCONST GpPointF *points, INT count);
GdipAddPathBeziers = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipAddPathBeziers', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurve(GpPath *path, GDIPCONST GpPointF *points, INT count);
GdipAddPathCurve = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipAddPathCurve', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurve2(GpPath *path, GDIPCONST GpPointF *points, INT count, REAL tension);
GdipAddPathCurve2 = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int, REAL)(('GdipAddPathCurve2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurve3(GpPath *path, GDIPCONST GpPointF *points, INT count, INT offset, INT numberOfSegments, REAL tension);
GdipAddPathCurve3 = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int, c_int, c_int, REAL)(('GdipAddPathCurve3', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathClosedCurve(GpPath *path, GDIPCONST GpPointF *points, INT count);
GdipAddPathClosedCurve = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipAddPathClosedCurve', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathClosedCurve2(GpPath *path, GDIPCONST GpPointF *points, INT count, REAL tension);
GdipAddPathClosedCurve2 = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int, REAL)(('GdipAddPathClosedCurve2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathRectangle(GpPath *path, REAL x, REAL y, REAL width, REAL height);
GdipAddPathRectangle = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL)(('GdipAddPathRectangle', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathRectangles(GpPath *path, GDIPCONST GpRectF *rects, INT count);
GdipAddPathRectangles = WINFUNCTYPE(c_int, c_void_p, POINTER(GpRectF), c_int)(('GdipAddPathRectangles', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathEllipse(GpPath *path, REAL x, REAL y, REAL width, REAL height);
GdipAddPathEllipse = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL)(('GdipAddPathEllipse', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathPie(GpPath *path, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle);
GdipAddPathPie = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipAddPathPie', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathPolygon(GpPath *path, GDIPCONST GpPointF *points, INT count);
GdipAddPathPolygon = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPointF), c_int)(('GdipAddPathPolygon', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathPath(GpPath *path, GDIPCONST GpPath* addingPath, BOOL connect);
GdipAddPathPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_bool)(('GdipAddPathPath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathString(GpPath *path, GDIPCONST WCHAR *string, INT length, GDIPCONST GpFontFamily *family, INT style, REAL emSize, GDIPCONST GpRectF *layoutRect, GDIPCONST GpStringFormat *format);
GdipAddPathString = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_int, c_void_p, c_int, REAL, POINTER(GpRectF), c_void_p)(('GdipAddPathString', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathStringI(GpPath *path, GDIPCONST WCHAR *string, INT length, GDIPCONST GpFontFamily *family, INT style, REAL emSize, GDIPCONST GpRect *layoutRect, GDIPCONST GpStringFormat *format);
GdipAddPathStringI = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_int, c_void_p, c_int, REAL, POINTER(GpRect), c_void_p)(('GdipAddPathStringI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathLineI(GpPath *path, INT x1, INT y1, INT x2, INT y2);
GdipAddPathLineI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int)(('GdipAddPathLineI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathLine2I(GpPath *path, GDIPCONST GpPoint *points, INT count);
GdipAddPathLine2I = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipAddPathLine2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathArcI(GpPath *path, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle);
GdipAddPathArcI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int, REAL, REAL)(('GdipAddPathArcI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathBezierI(GpPath *path, INT x1, INT y1, INT x2, INT y2, INT x3, INT y3, INT x4, INT y4);
GdipAddPathBezierI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(('GdipAddPathBezierI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathBeziersI(GpPath *path, GDIPCONST GpPoint *points, INT count);
GdipAddPathBeziersI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipAddPathBeziersI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurveI(GpPath *path, GDIPCONST GpPoint *points, INT count);
GdipAddPathCurveI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipAddPathCurveI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurve2I(GpPath *path, GDIPCONST GpPoint *points, INT count, REAL tension);
GdipAddPathCurve2I = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int, REAL)(('GdipAddPathCurve2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathCurve3I(GpPath *path, GDIPCONST GpPoint *points, INT count, INT offset, INT numberOfSegments, REAL tension);
GdipAddPathCurve3I = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int, c_int, c_int, REAL)(('GdipAddPathCurve3I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathClosedCurveI(GpPath *path, GDIPCONST GpPoint *points, INT count);
GdipAddPathClosedCurveI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipAddPathClosedCurveI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathClosedCurve2I(GpPath *path, GDIPCONST GpPoint *points, INT count, REAL tension);
GdipAddPathClosedCurve2I = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int, REAL)(('GdipAddPathClosedCurve2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathRectangleI(GpPath *path, INT x, INT y, INT width, INT height);
GdipAddPathRectangleI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int)(('GdipAddPathRectangleI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathRectanglesI(GpPath *path, GDIPCONST GpRect *rects, INT count);
GdipAddPathRectanglesI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpRect), c_int)(('GdipAddPathRectanglesI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathEllipseI(GpPath *path, INT x, INT y, INT width, INT height);
GdipAddPathEllipseI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int)(('GdipAddPathEllipseI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathPieI(GpPath *path, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle);
GdipAddPathPieI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int, REAL, REAL)(('GdipAddPathPieI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipAddPathPolygonI(GpPath *path, GDIPCONST GpPoint *points, INT count);
GdipAddPathPolygonI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpPoint), c_int)(('GdipAddPathPolygonI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFlattenPath(GpPath *path, GpMatrix* matrix, REAL flatness);
GdipFlattenPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL)(('GdipFlattenPath', windll.gdiplus))


#=========
# Brush APIs

#GpStatus WINGDIPAPI GdipCloneBrush(GpBrush *brush, GpBrush **cloneBrush);
_GdipCloneBrush = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCloneBrush', windll.gdiplus))
def GdipCloneBrush(brush):
	cloneBrush = c_void_p()
	status = _GdipCloneBrush(brush, byref(cloneBrush))
	return status, cloneBrush

#GpStatus WINGDIPAPI GdipDeleteBrush(GpBrush *brush);
GdipDeleteBrush = WINFUNCTYPE(c_int, c_void_p)(('GdipDeleteBrush', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetBrushType(GpBrush *brush, GpBrushType *type);
_GdipGetBrushType = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetBrushType', windll.gdiplus))
def GdipGetBrushType(brush):
	type_brush = c_int()
	status = _GdipGetBrushType(brush, byref(type_brush))
	return status, type_brush.value


#========
# HatchBrush APIs

#GpStatus WINGDIPAPI GdipCreateHatchBrush(GpHatchStyle hatchstyle, ARGB forecol, ARGB backcol, GpHatch **brush);
_GdipCreateHatchBrush = WINFUNCTYPE(c_int, c_int, ARGB, ARGB, c_void_p)(('GdipCreateHatchBrush', windll.gdiplus))
def GdipCreateHatchBrush(hatchstyle = 0, forecol = 0, backcol = 255):
	brush = c_void_p()
	status = _GdipCreateHatchBrush(hatchstyle, forecol, backcol, byref(brush))
	return status, brush

#GpStatus WINGDIPAPI GdipGetHatchStyle(GpHatch *brush, GpHatchStyle *hatchstyle);
_GdipGetHatchStyle = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetHatchStyle', windll.gdiplus))
def GdipGetHatchStyle(brush):
	hatchstyle = c_int()
	status = _GdipGetHatchStyle(brush, byref(hatchstyle))
	return status, hatchstyle.value

#GpStatus WINGDIPAPI GdipGetHatchForegroundColor(GpHatch *brush, ARGB* forecol);
_GdipGetHatchForegroundColor = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetHatchForegroundColor', windll.gdiplus))
def GdipGetHatchForegroundColor(brush):
	forecol = ARGB()
	status = _GdipGetHatchForegroundColor(brush, byref(forecol))
	return status, forecol.value

#GpStatus WINGDIPAPI GdipGetHatchBackgroundColor(GpHatch *brush, ARGB* backcol);
_GdipGetHatchBackgroundColor = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetHatchBackgroundColor', windll.gdiplus))
def GdipGetHatchBackgroundColor(brush):
	backcol = ARGB()
	status = _GdipGetHatchBackgroundColor(brush, byref(backcol))
	return status, backcol.value


#========
# TextureBrush APIs

#GpStatus WINGDIPAPI GdipCreateTexture(GpImage *image, GpWrapMode wrapmode, GpTexture **texture);
_GdipCreateTexture = WINFUNCTYPE(c_int, c_void_p, c_int, c_void_p)(('GdipCreateTexture', windll.gdiplus))
def GdipCreateTexture(image, wrapmode = 0):
	texture = c_void_p()
	status = _GdipCreateTexture(image, wrapmode, byref(texture))
	return status, texture

#GpStatus WINGDIPAPI GdipCreateTexture2(GpImage *image, GpWrapMode wrapmode, REAL x, REAL y, REAL width, REAL height, GpTexture **texture);
_GdipCreateTexture2 = WINFUNCTYPE(c_int, c_void_p, c_int, REAL, REAL, REAL, REAL, c_void_p)(('GdipCreateTexture2', windll.gdiplus))
def GdipCreateTexture2(image, wrapmode = 0, x = 0.0, y = 0.0, width = 32.0, height = 32.0):
	texture = c_void_p()
	status = _GdipCreateTexture2(image, wrapmode, x, y, width, height, byref(texture))
	return status, texture

#GpStatus WINGDIPAPI GdipCreateTextureIA(GpImage *image, GDIPCONST GpImageAttributes *imageAttributes, REAL x, REAL y, REAL width, REAL height, GpTexture **texture);
_GdipCreateTextureIA = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL, c_void_p)(('GdipCreateTextureIA', windll.gdiplus))
def GdipCreateTextureIA(image, imageAttributes, x = 0.0, y = 0.0, width = 32.0, height = 32.0):
	texture = c_void_p()
	status = _GdipCreateTextureIA(image, imageAttributes, x, y, width, height, byref(texture))
	return status, texture

#GpStatus WINGDIPAPI GdipCreateTexture2I(GpImage *image, GpWrapMode wrapmode, INT x, INT y, INT width, INT height, GpTexture **texture);
_GdipCreateTexture2I = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int, c_int, c_void_p)(('GdipCreateTexture2I', windll.gdiplus))
def GdipCreateTexture2I(image, wrapmode = 0, x = 0, y = 0, width = 32, height = 32):
	texture = c_void_p()
	status = _GdipCreateTexture2I(image, wrapmode, x, y, width, height, byref(texture))
	return status, texture

#GpStatus WINGDIPAPI GdipCreateTextureIAI(GpImage *image, GDIPCONST GpImageAttributes *imageAttributes, INT x, INT y, INT width, INT height, GpTexture **texture);
_GdipCreateTextureIAI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, c_void_p)(('GdipCreateTextureIAI', windll.gdiplus))
def GdipCreateTextureIAI(image, imageAttributes, x = 0, y = 0, width = 32, height = 32):
	texture = c_void_p()
	status = _GdipCreateTextureIAI(image, imageAttributes, x, y, width, height, byref(texture))
	return status, texture

#GpStatus WINGDIPAPI GdipGetTextureTransform(GpTexture *brush, GpMatrix *matrix);
_GdipGetTextureTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetTextureTransform', windll.gdiplus))
def GdipGetTextureTransform(texture):
	matrix = c_void_p()
	status = _GdipGetTextureTransform(texture, byref(matrix))
	return status, matrix

#GpStatus WINGDIPAPI GdipSetTextureTransform(GpTexture *brush, GDIPCONST GpMatrix *matrix);
GdipSetTextureTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipSetTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipResetTextureTransform(GpTexture* brush);
GdipResetTextureTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipResetTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipMultiplyTextureTransform(GpTexture* brush, GDIPCONST GpMatrix *matrix, GpMatrixOrder order);
GdipMultiplyTextureTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipMultiplyTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTranslateTextureTransform(GpTexture* brush, REAL dx, REAL dy, GpMatrixOrder order);
GdipTranslateTextureTransform = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, c_int)(('GdipTranslateTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipScaleTextureTransform(GpTexture* brush, REAL sx, REAL sy, GpMatrixOrder order);
GdipScaleTextureTransform = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, c_int)(('GdipScaleTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipRotateTextureTransform(GpTexture* brush, REAL angle, GpMatrixOrder order);
GdipRotateTextureTransform = WINFUNCTYPE(c_int, c_void_p, REAL, c_int)(('GdipRotateTextureTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetTextureWrapMode(GpTexture *brush, GpWrapMode wrapmode);
GdipSetTextureWrapMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetTextureWrapMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetTextureWrapMode(GpTexture *brush, GpWrapMode *wrapmode);
_GdipGetTextureWrapMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetTextureWrapMode', windll.gdiplus))
def GdipGetTextureWrapMode(texture):
	wrapmode = c_int()
	status = _GdipGetTextureWrapMode(texture, byref(wrapmode))
	return status, wrapmode.value

#GpStatus WINGDIPAPI GdipGetTextureImage(GpTexture *brush, GpImage **image);
_GdipGetTextureImage = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetTextureImage', windll.gdiplus))
def GdipGetTextureImage(texture):
	image = c_void_p()
	status = _GdipGetTextureImage(texture, byref(image))
	return status, image


#========
# SolidBrush APIs

#GpStatus WINGDIPAPI GdipCreateSolidFill(ARGB color, GpSolidFill **brush);
_GdipCreateSolidFill = WINFUNCTYPE(c_int, c_ulong, c_void_p)(('GdipCreateSolidFill', windll.gdiplus))
def GdipCreateSolidFill(color = 128):
	brush = c_void_p()
	status = _GdipCreateSolidFill(color, byref(brush))
	return status, brush

#GpStatus WINGDIPAPI GdipSetSolidFillColor(GpSolidFill *brush, ARGB color);
GdipSetSolidFillColor = WINFUNCTYPE(c_int, c_void_p, c_ulong)(('GdipSetSolidFillColor', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetSolidFillColor(GpSolidFill *brush, ARGB *color);
_GdipGetSolidFillColor = WINFUNCTYPE(c_int, c_ulong, c_void_p)(('GdipGetSolidFillColor', windll.gdiplus))
def GdipGetSolidFillColor(brush):
	color = c_ulong()
	status = _GdipGetSolidFillColor(brush, byref(color))
	return status, color.value


#========
# Pen APIs

#GpStatus WINGDIPAPI GdipCreatePen1(ARGB color, REAL width, GpUnit unit, GpPen **pen);
_GdipCreatePen1 = WINFUNCTYPE(c_int, c_ulong, REAL, GpUnit, c_void_p)(('GdipCreatePen1', windll.gdiplus))
def GdipCreatePen1(color = MakeARGB(255, 255, 255, 255), width = 1.0, unit = UnitWorld):
	pen = c_void_p()
	status = _GdipCreatePen1(color, width, unit, byref(pen))
	return status, pen

#GpStatus WINGDIPAPI GdipCreatePen2(GpBrush *brush, REAL width, GpUnit unit, GpPen **pen);
_GdipCreatePen2 = WINFUNCTYPE(c_int, c_void_p, REAL, GpUnit, c_void_p)(('GdipCreatePen2', windll.gdiplus))
def GdipCreatePen2(color = None, width = 1.0, unit = UnitWorld):
	pen = c_void_p()
	status = _GdipCreatePen2(color, width, unit, byref(pen))
	return status, pen

#GpStatus WINGDIPAPI GdipClonePen(GpPen *pen, GpPen **clonepen);
_GdipClonePen = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipClonePen', windll.gdiplus))
def GdipClonePen(pen):
	clonepen = c_void_p()
	status = _GdipClonePen(pen, byref(clonepen))
	return status, clonepen

#GpStatus WINGDIPAPI GdipDeletePen(GpPen *pen);
GdipDeletePen = WINFUNCTYPE(c_int, c_void_p)(('GdipDeletePen', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetPenWidth(GpPen *pen, REAL width);
GdipSetPenWidth = WINFUNCTYPE(c_int, c_void_p, REAL)(('GdipSetPenWidth', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPenWidth(GpPen *pen, REAL *width);
_GdipGetPenWidth = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPenWidth', windll.gdiplus))
def GdipGetPenWidth(pen):
	width = REAL()
	status = _GdipGetPenWidth(pen, byref(width))
	return status, width.value

#GpStatus WINGDIPAPI GdipSetPenUnit(GpPen *pen, GpUnit unit);
GdipSetPenUnit = WINFUNCTYPE(c_int, c_void_p, GpUnit)(('GdipSetPenUnit', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPenUnit(GpPen *pen, GpUnit *unit);
_GdipGetPenUnit = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPenUnit', windll.gdiplus))
def GdipGetPenUnit(pen):
	unit = GpUnit()
	status = _GdipGetPenUnit(pen, byref(unit))
	return status, unit.value


#=========
# Image APIs

#GpStatus WINGDIPAPI GdipLoadImageFromStream(IStream* stream, GpImage **image);
_GdipLoadImageFromStream = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipLoadImageFromStream', windll.gdiplus))
def GdipLoadImageFromStream(stream):
	image = c_void_p()
	status = _GdipLoadImageFromStream(stream, byref(image))
	return status, image

#GpStatus WINGDIPAPI GdipLoadImageFromFile(GDIPCONST WCHAR* filename, GpImage **image);
_GdipLoadImageFromFile = WINFUNCTYPE(c_int, c_wchar_p, c_void_p)(('GdipLoadImageFromFile', windll.gdiplus))
def GdipLoadImageFromFile(filename = ''):
	image = c_void_p()
	status = _GdipLoadImageFromFile(filename, byref(image))
	return status, image

#GpStatus WINGDIPAPI GdipLoadImageFromStreamICM(IStream* stream, GpImage **image);
_GdipLoadImageFromStreamICM = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipLoadImageFromStreamICM', windll.gdiplus))
def GdipLoadImageFromStreamICM(stream):
	image = c_void_p()
	status = _GdipLoadImageFromStreamICM(stream, byref(image))
	return status, image

#GpStatus WINGDIPAPI GdipLoadImageFromFileICM(GDIPCONST WCHAR* filename, GpImage **image);
_GdipLoadImageFromFileICM = WINFUNCTYPE(c_int, c_wchar_p, c_void_p)(('GdipLoadImageFromFileICM', windll.gdiplus))
def GdipLoadImageFromFileICM(filename = ''):
	image = c_void_p()
	status = _GdipLoadImageFromFileICM(filename, byref(image))
	return status, image

#GpStatus WINGDIPAPI GdipCloneImage(GpImage *image, GpImage **cloneImage);
_GdipCloneImage = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCloneImage', windll.gdiplus))
def GdipCloneImage(image):
	cloneImage = c_void_p()
	status = _GdipCloneImage(image, byref(cloneImage))
	return status, cloneImage

#GpStatus WINGDIPAPI GdipDisposeImage(GpImage *image);
GdipDisposeImage = WINFUNCTYPE(c_int, c_void_p)(('GdipDisposeImage', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSaveImageToFile(GpImage *image, GDIPCONST WCHAR* filename, GDIPCONST CLSID* clsidEncoder, GDIPCONST EncoderParameters* encoderParams);
GdipSaveImageToFile = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_void_p)(('GdipSaveImageToFile', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSaveImageToStream(GpImage *image, IStream* stream, GDIPCONST CLSID* clsidEncoder, GDIPCONST EncoderParameters* encoderParams);
GdipSaveImageToStream = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_void_p)(('GdipSaveImageToStream', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSaveAdd(GpImage *image, GDIPCONST EncoderParameters* encoderParams);
GdipSaveAdd = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipSaveAdd', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSaveAddImage(GpImage *image, GpImage* newImage, GDIPCONST EncoderParameters* encoderParams);
GdipSaveAddImage = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipSaveAddImage', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetImageGraphicsContext(GpImage *image, GpGraphics **graphics);
_GdipGetImageGraphicsContext = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageGraphicsContext', windll.gdiplus))
def GdipGetImageGraphicsContext(image):
	graphics = c_void_p()
	status = _GdipGetImageGraphicsContext(image, byref(graphics))
	return status, graphics

#GpStatus WINGDIPAPI GdipGetImageBounds(GpImage *image, GpRectF *srcRect, GpUnit *srcUnit);
_GdipGetImageBounds = WINFUNCTYPE(c_int, c_void_p, POINTER(GpRectF), c_void_p)(('GdipGetImageBounds', windll.gdiplus))
def GdipGetImageBounds(image):
	srcRect = GpRectF()
	srcUnit = GpUnit()
	status = _GdipGetImageBounds(image, srcRect, byref(srcUnit))
	return status, srcRect[0], srcUnit.value

#GpStatus WINGDIPAPI GdipGetImageDimension(GpImage *image, REAL *width, REAL *height);
_GdipGetImageDimension = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipGetImageDimension', windll.gdiplus))
def GdipGetImageDimension(image):
	width = REAL()
	height = REAL()
	status = _GdipGetImageDimension(image, byref(width), byref(height))
	return status, width.value, height.value

#GpStatus WINGDIPAPI GdipGetImageType(GpImage *image, ImageType *type);
_GdipGetImageType = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageType', windll.gdiplus))
def GdipGetImageType(image):
	image_type = c_int()
	status = _GdipGetImageType(image, byref(image_type))
	return status, image_type.value

#GpStatus WINGDIPAPI GdipGetImageWidth(GpImage *image, UINT *width);
_GdipGetImageWidth = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageWidth', windll.gdiplus))
def GdipGetImageWidth(image):
	width = c_uint()
	status = _GdipGetImageWidth(image, byref(width))
	return status, width.value

#GpStatus WINGDIPAPI GdipGetImageHeight(GpImage *image, UINT *height);
_GdipGetImageHeight = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageHeight', windll.gdiplus))
def GdipGetImageHeight(image):
	height = c_uint()
	status = _GdipGetImageHeight(image, byref(height))
	return status, height.value

#GpStatus WINGDIPAPI GdipGetImageHorizontalResolution(GpImage *image, REAL *resolution);
_GdipGetImageHorizontalResolution = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageHorizontalResolution', windll.gdiplus))
def GdipGetImageHorizontalResolution(image):
	resolution = REAL()
	status = _GdipGetImageHorizontalResolution(image, byref(resolution))
	return status, resolution.value

#GpStatus WINGDIPAPI GdipGetImageVerticalResolution(GpImage *image, REAL *resolution);
_GdipGetImageVerticalResolution = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageVerticalResolution', windll.gdiplus))
def GdipGetImageVerticalResolution(image):
	resolution = REAL()
	status = _GdipGetImageVerticalResolution(image, byref(resolution))
	return status, resolution.value

#GpStatus WINGDIPAPI GdipGetImageFlags(GpImage *image, UINT *flags);
_GdipGetImageFlags = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageFlags', windll.gdiplus))
def GdipGetImageFlags(image):
	flags = c_uint()
	status = _GdipGetImageFlags(image, byref(flags))
	return status, flags.value

#GpStatus WINGDIPAPI GdipGetImageRawFormat(GpImage *image, GUID *format);
_GdipGetImageRawFormat = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImageRawFormat', windll.gdiplus))
def GdipGetImageRawFormat(image):
	format = c_int()
	status = _GdipGetImageRawFormat(image, byref(format))
	return status, format.value

#GpStatus WINGDIPAPI GdipGetImagePixelFormat(GpImage *image, PixelFormat *format);
_GdipGetImagePixelFormat = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetImagePixelFormat', windll.gdiplus))
def GdipGetImagePixelFormat(image):
	format = c_int()
	status = _GdipGetImagePixelFormat(image, byref(format))
	return status, format.value

#GpStatus WINGDIPAPI GdipGetImageThumbnail(GpImage *image, UINT thumbWidth, UINT thumbHeight, GpImage **thumbImage, GetThumbnailImageAbort callback, VOID * callbackData);
_GdipGetImageThumbnail = WINFUNCTYPE(c_int, c_void_p, c_uint, c_uint, c_void_p, c_void_p, c_void_p)(('GdipGetImageThumbnail', windll.gdiplus))
def GdipGetImageThumbnail(image, thumbWidth = 32, thumbHeight = 32, callback = 0, callbackData = 0):
	thumbImage = c_void_p()
	status = _GdipGetImageThumbnail(image, thumbWidth, thumbHeight, byref(thumbImage), callback, callbackData)
	return status, thumbImage

#...................

#GpStatus WINGDIPAPI GdipImageForceValidation(GpImage *image);
GdipImageForceValidation = WINFUNCTYPE(c_int, c_void_p)(('GdipImageForceValidation', windll.gdiplus))


# Bitmap APIs

#GpStatus WINGDIPAPI GdipCreateBitmapFromStream(IStream* stream, GpBitmap **bitmap);
_GdipCreateBitmapFromStream = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCreateBitmapFromStream', windll.gdiplus))
def GdipCreateBitmapFromStream(stream):
	bitmap = c_void_p()
	status = _GdipCreateBitmapFromStream(stream, byref(bitmap))
	return status, bitmap

#GpStatus WINGDIPAPI GdipCreateBitmapFromFile(GDIPCONST WCHAR* filename, GpBitmap **bitmap);
_GdipCreateBitmapFromFile = WINFUNCTYPE(c_int, c_wchar_p, c_void_p)(('GdipCreateBitmapFromFile', windll.gdiplus))
def GdipCreateBitmapFromFile(filename):
	bitmap = c_void_p()
	status = _GdipCreateBitmapFromFile(filename, byref(bitmap))
	return status, bitmap

#...........

#GpStatus WINGDIPAPI GdipCreateBitmapFromHICON(HICON hicon, GpBitmap** bitmap);
_GdipCreateBitmapFromHICON = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCreateBitmapFromHICON', windll.gdiplus))
def GdipCreateBitmapFromHICON(hicon):
	bitmap = c_void_p()
	status = _GdipCreateBitmapFromHICON(hicon, byref(bitmap))
	return status, bitmap


#===========
# Graphics APIs

#GpStatus WINGDIPAPI GdipFlush(GpGraphics *graphics, GpFlushIntention intention);
GdipFlush = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipFlush', windll.gdiplus))

#GpStatus WINGDIPAPI GdipCreateFromHDC(HDC hdc, GpGraphics **graphics);
_GdipCreateFromHDC = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCreateFromHDC', windll.gdiplus))
def GdipCreateFromHDC(hdc):
	graphics = c_void_p()
	status = _GdipCreateFromHDC(hdc, byref(graphics))
	return status, graphics

#GpStatus WINGDIPAPI GdipCreateFromHDC2(HDC hdc, HANDLE hDevice, GpGraphics **graphics);
GdipCreateFromHDC2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipCreateFromHDC2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipCreateFromHWND(HWND hwnd, GpGraphics **graphics);
GdipCreateFromHWND = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCreateFromHWND', windll.gdiplus))

#GpStatus WINGDIPAPI GdipCreateFromHWNDICM(HWND hwnd, GpGraphics **graphics);
GdipCreateFromHWNDICM = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipCreateFromHWNDICM', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDeleteGraphics(GpGraphics *graphics);
GdipDeleteGraphics = WINFUNCTYPE(c_int, c_void_p)(('GdipDeleteGraphics', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetDC(GpGraphics* graphics, HDC * hdc);
_GdipGetDC = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetDC', windll.gdiplus))
def GdipGetDC(graphics):
	hdc = c_void_p()
	status = _GdipGetDC(graphics, byref(hdc))
	return status, hdc

#GpStatus WINGDIPAPI GdipReleaseDC(GpGraphics* graphics, HDC hdc);
GdipReleaseDC = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipReleaseDC', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetCompositingMode(GpGraphics *graphics, CompositingMode compositingMode);
GdipSetCompositingMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetCompositingMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetCompositingMode(GpGraphics *graphics, CompositingMode *compositingMode);
_GdipGetCompositingMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetCompositingMode', windll.gdiplus))
def GdipGetCompositingMode(graphics):
	compositingMode = c_int()
	status = _GdipGetCompositingMode(graphics, byref(compositingMode))
	return status, compositingMode.value

#GpStatus WINGDIPAPI GdipSetRenderingOrigin(GpGraphics *graphics, INT x, INT y);
GdipSetRenderingOrigin = WINFUNCTYPE(c_int, c_void_p, c_int, c_int)(('GdipSetRenderingOrigin', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetRenderingOrigin(GpGraphics *graphics, INT *x, INT *y);
_GdipGetRenderingOrigin = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipGetRenderingOrigin', windll.gdiplus))
def GdipGetRenderingOrigin(graphics):
	x, y = c_int(), c_int()
	status = _GdipGetRenderingOrigin(graphics, byref(x), byref(y))
	return status, x.value, y.value

#GpStatus WINGDIPAPI GdipSetCompositingQuality(GpGraphics *graphics, CompositingQuality compositingQuality);
GdipSetCompositingQuality = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetCompositingQuality', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetCompositingQuality(GpGraphics *graphics, CompositingQuality *compositingQuality);
_GdipGetCompositingQuality = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetCompositingQuality', windll.gdiplus))
def GdipGetCompositingQuality(graphics):
	compositingQuality = c_int()
	status = _GdipGetCompositingQuality(graphics, byref(compositingQuality))
	return status, compositingQuality.value

#GpStatus WINGDIPAPI GdipSetSmoothingMode(GpGraphics *graphics, SmoothingMode smoothingMode);
GdipSetSmoothingMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetSmoothingMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetSmoothingMode(GpGraphics *graphics, SmoothingMode *smoothingMode);
_GdipGetSmoothingMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetSmoothingMode', windll.gdiplus))
def GdipGetSmoothingMode(graphics):
	smoothingMode = c_int()
	status = _GdipGetSmoothingMode(graphics, byref(smoothingMode))
	return status, smoothingMode.value

#GpStatus WINGDIPAPI GdipSetPixelOffsetMode(GpGraphics* graphics, PixelOffsetMode pixelOffsetMode);
GdipSetPixelOffsetMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetPixelOffsetMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPixelOffsetMode(GpGraphics *graphics, PixelOffsetMode *pixelOffsetMode);
_GdipGetPixelOffsetMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPixelOffsetMode', windll.gdiplus))
def GdipGetPixelOffsetMode(graphics):
	pixelOffsetMode = c_int()
	status = _GdipGetPixelOffsetMode(graphics, byref(pixelOffsetMode))
	return status, pixelOffsetMode.value

#GpStatus WINGDIPAPI GdipSetTextRenderingHint(GpGraphics *graphics, TextRenderingHint mode);
GdipSetTextRenderingHint = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetTextRenderingHint', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetTextRenderingHint(GpGraphics *graphics, TextRenderingHint *mode);
_GdipGetTextRenderingHint = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetTextRenderingHint', windll.gdiplus))
def GdipGetTextRenderingHint(graphics):
	mode = c_int()
	status = _GdipGetTextRenderingHint(graphics, byref(mode))
	return status, mode.value

#GpStatus  WINGDIPAPI GdipSetTextContrast(GpGraphics *graphics, UINT contrast);
GdipSetTextContrast = WINFUNCTYPE(c_int, c_void_p, c_uint)(('GdipSetTextContrast', windll.gdiplus))

#GpStatus  WINGDIPAPI GdipGetTextContrast(GpGraphics *graphics, UINT * contrast);
_GdipGetTextContrast = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetTextContrast', windll.gdiplus))
def GdipGetTextContrast(graphics):
	contrast = c_uint()
	status = _GdipGetTextContrast(graphics, byref(contrast))
	return status, contrast.value

#GpStatus WINGDIPAPI GdipSetInterpolationMode(GpGraphics *graphics, InterpolationMode interpolationMode);
GdipSetInterpolationMode = WINFUNCTYPE(c_int, c_void_p, c_int)(('GdipSetInterpolationMode', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetInterpolationMode(GpGraphics *graphics, InterpolationMode *interpolationMode);
_GdipGetInterpolationMode = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetInterpolationMode', windll.gdiplus))
def GdipGetInterpolationMode(graphics):
	interpolationMode = c_int()
	status = _GdipGetInterpolationMode(graphics, byref(interpolationMode))
	return status, interpolationMode.value

#GpStatus WINGDIPAPI GdipSetWorldTransform(GpGraphics *graphics, GpMatrix *matrix);
GdipSetWorldTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipSetWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipResetWorldTransform(GpGraphics *graphics);
GdipResetWorldTransform = WINFUNCTYPE(c_int, c_void_p)(('GdipResetWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipMultiplyWorldTransform(GpGraphics *graphics, GDIPCONST GpMatrix *matrix, GpMatrixOrder order);
GdipMultiplyWorldTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipMultiplyWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTranslateWorldTransform(GpGraphics *graphics, REAL dx, REAL dy, GpMatrixOrder order);
GdipTranslateWorldTransform = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, c_int)(('GdipTranslateWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipScaleWorldTransform(GpGraphics *graphics, REAL sx, REAL sy, GpMatrixOrder order);
GdipScaleWorldTransform = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, c_int)(('GdipScaleWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipRotateWorldTransform(GpGraphics *graphics, REAL angle, GpMatrixOrder order);
GdipRotateWorldTransform = WINFUNCTYPE(c_int, c_void_p, REAL, c_int)(('GdipRotateWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetWorldTransform(GpGraphics *graphics, GpMatrix *matrix);
GdipGetWorldTransform = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetWorldTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipResetPageTransform(GpGraphics *graphics);
GdipResetPageTransform = WINFUNCTYPE(c_int, c_void_p)(('GdipResetPageTransform', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPageUnit(GpGraphics *graphics, GpUnit *unit);
GdipGetPageUnit = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPageUnit', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetPageScale(GpGraphics *graphics, REAL *scale);
GdipGetPageScale = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetPageScale', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetPageUnit(GpGraphics *graphics, GpUnit unit);
GdipSetPageUnit = WINFUNCTYPE(c_int, c_void_p, GpUnit)(('GdipSetPageUnit', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetPageScale(GpGraphics *graphics, REAL scale);
GdipSetPageScale = WINFUNCTYPE(c_int, c_void_p, REAL)(('GdipSetPageScale', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetDpiX(GpGraphics *graphics, REAL* dpi);
GdipGetDpiX = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetDpiX', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetDpiY(GpGraphics *graphics, REAL* dpi);
GdipGetDpiY = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetDpiY', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTransformPoints(GpGraphics *graphics, GpCoordinateSpace destSpace, GpCoordinateSpace srcSpace, GpPointF *points, INT count);
GdipTransformPoints = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_void_p, c_int)(('GdipTransformPoints', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTransformPointsI(GpGraphics *graphics, GpCoordinateSpace destSpace, GpCoordinateSpace srcSpace, GpPoint *points, INT count);
GdipTransformPointsI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_void_p, c_int)(('GdipTransformPointsI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetNearestColor(GpGraphics *graphics, ARGB* argb);
GdipGetNearestColor = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetNearestColor', windll.gdiplus))

# Creates the Win9x Halftone Palette (even on NT) with correct Desktop colors
#HPALETTE WINGDIPAPI GdipCreateHalftonePalette();
GdipCreateHalftonePalette = WINFUNCTYPE(c_void_p)(('GdipCreateHalftonePalette', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawLine(GpGraphics *graphics, GpPen *pen, REAL x1, REAL y1, REAL x2, REAL y2);
GdipDrawLine = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipDrawLine', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawLineI(GpGraphics *graphics, GpPen *pen, INT x1, INT y1, INT x2, INT y2);
GdipDrawLineI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipDrawLineI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawLines(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count);
GdipDrawLines = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawLines', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawLinesI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count);
GdipDrawLinesI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawLinesI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawArc(GpGraphics *graphics, GpPen *pen, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle);
GdipDrawArc = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipDrawArc', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawArcI(GpGraphics *graphics, GpPen *pen, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle);
GdipDrawArcI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, REAL, REAL)(('GdipDrawArcI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawBezier(GpGraphics *graphics, GpPen *pen, REAL x1, REAL y1, REAL x2, REAL y2, REAL x3, REAL y3, REAL x4, REAL y4);
GdipDrawBezier = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipDrawBezier', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawBezierI(GpGraphics *graphics, GpPen *pen, INT x1, INT y1, INT x2, INT y2, INT x3, INT y3, INT x4, INT y4);
GdipDrawBezierI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(('GdipDrawBezierI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawBeziers(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count);
GdipDrawBeziers = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawBeziers', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawBeziersI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count);
GdipDrawBeziersI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawBeziersI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawRectangle(GpGraphics *graphics, GpPen *pen, REAL x, REAL y, REAL width, REAL height);
GdipDrawRectangle = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipDrawRectangle', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawRectangleI(GpGraphics *graphics, GpPen *pen, INT x, INT y, INT width, INT height);
GdipDrawRectangleI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipDrawRectangleI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawRectangles(GpGraphics *graphics, GpPen *pen, GDIPCONST GpRectF *rects, INT count);
GdipDrawRectangles = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpRectF), c_int)(('GdipDrawRectangles', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawRectanglesI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpRect *rects, INT count);
GdipDrawRectanglesI = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpRect), c_int)(('GdipDrawRectanglesI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawEllipse(GpGraphics *graphics, GpPen *pen, REAL x, REAL y, REAL width, REAL height);
GdipDrawEllipse = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipDrawEllipse', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawEllipseI(GpGraphics *graphics, GpPen *pen, INT x, INT y, INT width, INT height);
GdipDrawEllipseI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipDrawEllipseI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawPie(GpGraphics *graphics, GpPen *pen, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle);
GdipDrawPie = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipDrawPie', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawPieI(GpGraphics *graphics, GpPen *pen, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle);
GdipDrawPieI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, REAL, REAL)(('GdipDrawPieI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawPolygon(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count);
GdipDrawPolygon = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawPolygon', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawPolygonI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count);
GdipDrawPolygonI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawPolygonI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawPath(GpGraphics *graphics, GpPen *pen, GpPath *path);
GdipDrawPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipDrawPath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurve(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count);
GdipDrawCurve = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawCurve', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurveI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count);
GdipDrawCurveI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawCurveI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurve2(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count, REAL tension);
GdipDrawCurve2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, REAL)(('GdipDrawCurve2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurve2I(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count, REAL tension);
GdipDrawCurve2I = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, REAL)(('GdipDrawCurve2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurve3(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count, INT offset, INT numberOfSegments, REAL tension);
GdipDrawCurve3 = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, c_int, c_int, REAL)(('GdipDrawCurve3', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawCurve3I(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count, INT offset, INT numberOfSegments, REAL tension);
GdipDrawCurve3I = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, c_int, c_int, REAL)(('GdipDrawCurve3I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawClosedCurve(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count);
GdipDrawClosedCurve = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawClosedCurve', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawClosedCurveI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count);
GdipDrawClosedCurveI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int)(('GdipDrawClosedCurveI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawClosedCurve2(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points, INT count, REAL tension);
GdipDrawClosedCurve2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, REAL)(('GdipDrawClosedCurve2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawClosedCurve2I(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points, INT count, REAL tension);
GdipDrawClosedCurve2I = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p, c_int, REAL)(('GdipDrawClosedCurve2I', windll.gdiplus))


#...........
#GpStatus WINGDIPAPI GdipGraphicsClear(GpGraphics *graphics, ARGB color);
GdipGraphicsClear = WINFUNCTYPE(c_int, c_void_p, c_ulong)(('GdipGraphicsClear', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillRectangle(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y, REAL width, REAL height);
GdipFillRectangle = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipFillRectangle', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillRectangleI(GpGraphics *graphics, GpBrush *brush, INT x, INT y, INT width, INT height);
GdipFillRectangleI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipFillRectangleI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillRectangles(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpRectF *rects, INT count);
GdipFillRectangles = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpRectF), c_int)(('GdipFillRectangles', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillRectanglesI(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpRect *rects, INT count);
GdipFillRectanglesI = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpRect), c_int)(('GdipFillRectanglesI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPolygon(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPointF *points, INT count, GpFillMode fillMode);
GdipFillPolygon = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPointF), c_int, c_int)(('GdipFillPolygon', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPolygonI(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPoint *points, INT count, GpFillMode fillMode);
GdipFillPolygonI = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPoint), c_int, c_int)(('GdipFillPolygonI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPolygon2(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPointF *points, INT count);
GdipFillPolygon2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPointF), c_int)(('GdipFillPolygon2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPolygon2I(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPoint *points, INT count);
GdipFillPolygon2I = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPoint), c_int)(('GdipFillPolygon2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillEllipse(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y, REAL width, REAL height);
GdipFillEllipse = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipFillEllipse', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillEllipseI(GpGraphics *graphics, GpBrush *brush, INT x, INT y, INT width, INT height);
GdipFillEllipseI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipFillEllipseI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPie(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle);
GdipFillPie = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL)(('GdipFillPie', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPieI(GpGraphics *graphics, GpBrush *brush, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle);
GdipFillPieI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, REAL, REAL)(('GdipFillPieI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillPath(GpGraphics *graphics, GpBrush *brush, GpPath *path);
GdipFillPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipFillPath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillClosedCurve(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPointF *points, INT count);
GdipFillClosedCurve = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPointF), c_int)(('GdipFillClosedCurve', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillClosedCurveI(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPoint *points, INT count);
GdipFillClosedCurveI = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPoint), c_int)(('GdipFillClosedCurveI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillClosedCurve2(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPointF *points, INT count, REAL tension, GpFillMode fillMode);
GdipFillClosedCurve2 = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPointF), c_int, REAL, c_int)(('GdipFillClosedCurve2', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillClosedCurve2I(GpGraphics *graphics, GpBrush *brush, GDIPCONST GpPoint *points, INT count, REAL tension, GpFillMode fillMode);
GdipFillClosedCurve2I = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPoint), c_int, REAL, c_int)(('GdipFillClosedCurve2I', windll.gdiplus))

#GpStatus WINGDIPAPI GdipFillRegion(GpGraphics *graphics, GpBrush *brush, GpRegion *region);
GdipFillRegion = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(('GdipFillRegion', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImageFX(GpGraphics *graphics, GpImage *image, GpRectF *source, GpMatrix *xForm, CGpEffect *effect, GpImageAttributes *imageAttributes, GpUnit srcUnit);
if GDIPVER >= 0x0110:
	GdipDrawImageFX = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpRectF), c_void_p, c_void_p, c_void_p, GpUnit)(('GdipDrawImageFX', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImage(GpGraphics *graphics, GpImage *image, REAL x, REAL y);
GdipDrawImage = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL)(('GdipDrawImage', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImageI(GpGraphics *graphics, GpImage *image, INT x, INT y);
GdipDrawImageI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int)(('GdipDrawImageI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImageRect(GpGraphics *graphics, GpImage *image, REAL x, REAL y, REAL width, REAL height);
GdipDrawImageRect = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL)(('GdipDrawImageRect', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImageRectI(GpGraphics *graphics, GpImage *image, INT x, INT y, INT width, INT height);
GdipDrawImageRectI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(('GdipDrawImageRectI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImagePoints(GpGraphics *graphics, GpImage *image, GDIPCONST GpPointF *dstpoints, INT count);
GdipDrawImagePoints = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPointF), c_int)(('GdipDrawImagePoints', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImagePointsI(GpGraphics *graphics, GpImage *image, GDIPCONST GpPoint *dstpoints, INT count);
GdipDrawImagePointsI = WINFUNCTYPE(c_int, c_void_p, c_void_p, POINTER(GpPoint), c_int)(('GdipDrawImagePointsI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImagePointRect(GpGraphics *graphics, GpImage *image, REAL x, REAL y, REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight, GpUnit srcUnit);
GdipDrawImagePointRect = WINFUNCTYPE(c_int, c_void_p, c_void_p, REAL, REAL, REAL, REAL, REAL, REAL, GpUnit)(('GdipDrawImagePointRect', windll.gdiplus))

#GpStatus WINGDIPAPI GdipDrawImagePointRectI(GpGraphics *graphics, GpImage *image, INT x, INT y, INT srcx, INT srcy, INT srcwidth, INT srcheight, GpUnit srcUnit);
GdipDrawImagePointRectI = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_int, c_int, c_int, c_int, GpUnit)(('GdipDrawImagePointRectI', windll.gdiplus))

#..........................

#GpStatus WINGDIPAPI GdipSetClipGraphics(GpGraphics *graphics, GpGraphics *srcgraphics, CombineMode combineMode);
GdipSetClipGraphics = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipSetClipGraphics', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetClipRect(GpGraphics *graphics, REAL x, REAL y, REAL width, REAL height, CombineMode combineMode);
GdipSetClipRect = WINFUNCTYPE(c_int, c_void_p, REAL, REAL, REAL, REAL, c_int)(('GdipSetClipRect', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetClipRectI(GpGraphics *graphics, INT x, INT y, INT width, INT height, CombineMode combineMode);
GdipSetClipRectI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, c_int, c_int)(('GdipSetClipRectI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetClipPath(GpGraphics *graphics, GpPath *path, CombineMode combineMode);
GdipSetClipPath = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipSetClipPath', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetClipRegion(GpGraphics *graphics, GpRegion *region, CombineMode combineMode);
GdipSetClipRegion = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipSetClipRegion', windll.gdiplus))

#GpStatus WINGDIPAPI GdipSetClipHrgn(GpGraphics *graphics, HRGN hRgn, CombineMode combineMode);
GdipSetClipHrgn = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipSetClipHrgn', windll.gdiplus))

#GpStatus WINGDIPAPI GdipResetClip(GpGraphics *graphics);
GdipResetClip = WINFUNCTYPE(c_int, c_void_p)(('GdipResetClip', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTranslateClip(GpGraphics *graphics, REAL dx, REAL dy);
GdipTranslateClip = WINFUNCTYPE(c_int, c_void_p, REAL, REAL)(('GdipTranslateClip', windll.gdiplus))

#GpStatus WINGDIPAPI GdipTranslateClipI(GpGraphics *graphics, INT dx, INT dy);
GdipTranslateClipI = WINFUNCTYPE(c_int, c_void_p, c_int, c_int)(('GdipTranslateClipI', windll.gdiplus))

#GpStatus WINGDIPAPI GdipGetClip(GpGraphics *graphics, GpRegion *region);
_GdipGetClip = WINFUNCTYPE(c_int, c_void_p, c_void_p)(('GdipGetClip', windll.gdiplus))
def GdipGetClip(graphics):
	region = c_void_p()
	status = _GdipGetClip(graphics, byref(region))
	return status, region

#GpStatus WINGDIPAPI GdipGetClipBounds(GpGraphics *graphics, GpRectF *rect);
_GdipGetClipBounds = WINFUNCTYPE(c_int, c_void_p, POINTER(GpRectF))(('GdipGetClipBounds', windll.gdiplus))
def GdipGetClipBounds(graphics):
	rect = GpRectF()
	status = _GdipGetClipBounds(graphics, byref(rect))
	return status, rect[0]

#GpStatus WINGDIPAPI GdipGetClipBoundsI(GpGraphics *graphics, GpRect *rect);
_GdipGetClipBoundsI = WINFUNCTYPE(c_int, c_void_p, POINTER(GpRect))(('GdipGetClipBoundsI', windll.gdiplus))
def GdipGetClipBoundsI(graphics):
	rect = GpRect()
	status = _GdipGetClipBoundsI(graphics, byref(rect))
	return status, rect[0]

#GpStatus WINGDIPAPI GdipIsClipEmpty(GpGraphics *graphics, BOOL *result);
_GdipIsClipEmpty = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int)(('GdipIsClipEmpty', windll.gdiplus))
def GdipIsClipEmpty(graphics):
	result = c_bool()
	status = _GdipIsClipEmpty(graphics, byref(result))
	return status, result
