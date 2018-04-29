from pywingui.windows import *
from pywingui.wtl import *
from ctypes import c_char

try:
	LoadLibrary("SciLexer.DLL")
#except Exception, e:
except:# for compatibility with Python 3 version
	MessageBox(0, "The Scintilla DLL could not be loaded.", "Error loading Scintilla", MB_OK | MB_ICONERROR)
	#~ raise e

from scintilla_constants import *

class SCNotification(Structure):
	_fields_ = [("nmhdr", NMHDR),
				("position", c_int),
				("ch", c_int),
				("modifiers", c_int),
				("modificationType", c_int),
				("text", c_wchar_p),
				("length", c_int),                
				("linesAdded", c_int),
				("message", c_int),
				("wParam", WPARAM),
				("lParam", LPARAM),
				("line", c_int),
				("foldLevelNow", c_int),
				("foldLevelPrev", c_int),
				("margin", c_int),
				("listType", c_int),
				("x", c_int),
				("y", c_int)]

copyright = \
"""
Scintilla
Copyright 1998-2003 by Neil Hodgson <neilh@scintilla.org>
All Rights Reserved
"""

class Scintilla(Window):
	_window_class_ = "Scintilla"
	_window_style_ = WS_VISIBLE | WS_CHILD

	def __init__(self, *args, **kwargs):
		Window.__init__(self, *args, **kwargs)
		self.InterceptParent()

	def GetNotification(self, event):
		return SCNotification.from_address(int(event.lParam))

	def SendScintillaMessage(self, msg, wParam, lParam):
		#TODO use fast path,e.g. retreive direct message fn from
		#scintilla as described in scintilla docs
		return windll.user32.SendMessageA(self.handle, msg, wParam, lParam)
		#~ return self.SendMessage(msg, wParam, lParam)

	def SetText(self, txt):
		self.SendScintillaMessage(SCI_SETTEXT, 0, txt)

	def GetLexer(self):
		return self.SendScintillaMessage(SCI_GETLEXER, 0, 0)

	def SetLexerLanguage(self, lang):
		self.SendScintillaMessage(SCI_SETLEXERLANGUAGE, 0, lang)

	def SetStyleBits(self, key, value):
		self.SendScintillaMessage(SCI_SETSTYLEBITS, key, value)

	def SetMarginWidth(self, width = 0):
		self.SendScintillaMessage(SCI_SETMARGINWIDTHN, 0, width)

	def SetProperty(self, key, value):
		self.SendScintillaMessage(SCI_SETPROPERTY, key, value)

	def SetKeyWords(self, keyWordSet, keyWordList):
		self.SendScintillaMessage(SCI_SETKEYWORDS, keyWordSet, " ".join(keyWordList))

	def StyleSetFore(self, styleNumber, color):
		self.SendScintillaMessage(SCI_STYLESETFORE, styleNumber, color)

	def StyleSetBack(self, styleNumber, color):
		self.SendScintillaMessage(SCI_STYLESETBACK, styleNumber, color)

	def StyleSetSize(self, styleNumber, size):
		self.SendScintillaMessage(SCI_STYLESETSIZE, styleNumber, size)

	def StyleSetFont(self, styleNumber, face):
		self.SendScintillaMessage(SCI_STYLESETFONT, styleNumber, face)

	def StyleClearAll(self):
		self.SendScintillaMessage(SCI_STYLECLEARALL, 0, 0)

	def GetLength(self):
		return self.SendScintillaMessage(SCI_GETLENGTH, 0, 0)

	def GetText(self):
		buff_length = self.GetLength() + 1
		buff = create_string_buffer(buff_length)
		self.SendScintillaMessage(SCI_GETTEXT, buff_length, byref(buff))
		return str(buff.value)

	def GetSelText(self):
		start = self.SendScintillaMessage(SCI_GETSELECTIONSTART, 0, 0)
		end = self.SendScintillaMessage(SCI_GETSELECTIONEND, 0, 0)
		if start == end: return ""
		buff = (c_char * (end - start + 1))()
		self.SendScintillaMessage(SCI_GETSELTEXT, 0, byref(buff))
		return str(buff.value)

	def HasSelection(self):
		start = self.SendScintillaMessage(SCI_GETSELECTIONSTART, 0, 0)
		end = self.SendScintillaMessage(SCI_GETSELECTIONEND, 0, 0)
		return (end - start) > 0

	def AddText(self, text):
		self.SendScintillaMessage(SCI_ADDTEXT, len(text), text)

	def SetTabWidth(self, width):
		self.SendScintillaMessage(SCI_SETTABWIDTH, width, 0)

	def SetUseTabs(self, useTabs):
		self.SendScintillaMessage(SCI_SETUSETABS, int(useTabs), 0)

	def SetEolMode(self, eolMode):
		self.SendScintillaMessage(SCI_SETEOLMODE, eolMode, 0)

	def Undo(self):
		self.SendScintillaMessage(SCI_UNDO, 0, 0)

	def Redo(self):
		self.SendScintillaMessage(SCI_REDO, 0, 0)

	def CanUndo(self):
		return self.SendScintillaMessage(SCI_CANUNDO, 0, 0)

	def CanRedo(self):
		return self.SendScintillaMessage(SCI_CANREDO, 0, 0)

	def Cut(self):
		self.SendScintillaMessage(SCI_CUT, 0, 0)

	def Copy(self):
		self.SendScintillaMessage(SCI_COPY, 0, 0)

	def Clear(self):
		self.SendScintillaMessage(SCI_CLEAR, 0, 0)

	def Paste(self):
		self.SendScintillaMessage(SCI_PASTE, 0, 0)

	def CanPaste(self):
		return self.SendScintillaMessage(SCI_CANPASTE, 0, 0)

	def SelectAll(self):
		self.SendScintillaMessage(SCI_SELECTALL, 0, 0)
