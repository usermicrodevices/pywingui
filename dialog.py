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

## Thanx to Brad Clements for this contribution!

from version_microsoft import WINVER

from types import IntType, LongType

from ctypes import *

from windows import *
from wtl_core import *
from comctl import *

memcpy = cdll.msvcrt.memcpy

# Dialog Box Template Styles
DS_ABSALIGN         = 0x01L
DS_SYSMODAL         = 0x02L
DS_LOCALEDIT        = 0x20L   # Edit items get Local storage
DS_SETFONT          = 0x40L   # User specified font for Dlg controls
DS_MODALFRAME       = 0x80L   # Can be combined with WS_CAPTION
DS_NOIDLEMSG        = 0x100L  # WM_ENTERIDLE message will not be sent
DS_SETFOREGROUND    = 0x200L  # not in win3.1
if WINVER >= 0x0400:
	DS_3DLOOK           = 0x0004L
	DS_FIXEDSYS         = 0x0008L
	DS_NOFAILCREATE     = 0x0010L
	DS_CONTROL          = 0x0400L
	DS_CENTER           = 0x0800L
	DS_CENTERMOUSE      = 0x1000L
	DS_CONTEXTHELP      = 0x2000L
	DS_SHELLFONT        = DS_SETFONT | DS_FIXEDSYS
#if(_WIN32_WCE >= 0x0500)
#DS_USEPIXELS        = 0x8000L

# Dialog Codes
DLGC_WANTARROWS      = 0x0001      # Control wants arrow keys
DLGC_WANTTAB         = 0x0002      # Control wants tab keys
DLGC_WANTALLKEYS     = 0x0004      # Control wants all keys
DLGC_WANTMESSAGE     = 0x0004      # Pass message to control
DLGC_HASSETSEL       = 0x0008      # Understands EM_SETSEL message
DLGC_DEFPUSHBUTTON   = 0x0010      # Default pushbutton
DLGC_UNDEFPUSHBUTTON = 0x0020      # Non-default pushbutton
DLGC_RADIOBUTTON     = 0x0040      # Radio button
DLGC_WANTCHARS       = 0x0080      # Want WM_CHAR messages
DLGC_STATIC          = 0x0100      # Static item: don't include
DLGC_BUTTON          = 0x2000      # Button item: can be checked

class StringOrOrd:
    """Pack up a string or ordinal"""
    def __init__(self, value):
        if value is None or value == "":
            self.value = c_ushort(0)
        elif type(value) in (IntType, LongType):
            # treat as an atom
            if not value:
                self.value = c_ushort(0)        # 0 is not a valid atom
            else:
                ordinaltype = c_ushort * 2
                ordinal = ordinaltype(0xffff, value)
                self.value = ordinal
        else:
            value = str(value)

            mbLen = MultiByteToWideChar(CP_ACP, 0, value, -1, 0, 0)
            if mbLen < 1:
                raise RuntimeError("Could not determine multibyte string length for %s" % \
                                   repr(value))

            #this does not work for me:, why needed?
            #if (mbLen % 2):
            #    mbLen += 1          # round up to next word in size
                
            stringtype = c_ushort * mbLen
            string = stringtype()
            result = MultiByteToWideChar(CP_ACP, 0, value, -1, addressof(string), sizeof(string))
            if result < 1:
                raise RuntimeError("could not convert multibyte string %s" % repr(value))
            self.value = string


    def __len__(self):
        return sizeof(self.value)

class DialogTemplate(WindowsObject):
    __dispose__ = GlobalFree
    _window_class_ = None
    _window_style_ = WS_CHILD
    _window_style_ex_ = 0
    _class_font_size_ = 8
    _class_font_name_ = "MS Sans Serif" 

    def __init__(self,
                 wclass = None,    # the window class
                 title = "",
                 menu=None,
                 style = None,
                 exStyle = None,
                 fontSize=None,
                 fontName=None,
                 rcPos = RCDEFAULT,
                 orStyle = None,
                 orExStyle = None,
                 nandStyle = None,
                 nandExStyle = None,
                 items=[]):


        if wclass is not None:
            wclass = StringOrOrd(wclass)
        else:
            wclass = StringOrOrd(self._window_class_)

        title = StringOrOrd(title)
        menu = StringOrOrd(menu)

        if style is None:
            style = self._window_style_

        if exStyle is None:
            exStyle = self._window_style_ex_

        if orStyle:
            style |= orStyle

        if orExStyle:
            exStyle |= orExStyle


        if nandStyle:
            style &= ~nandStyle

        if rcPos.left == CW_USEDEFAULT:
            cx = 50
            x = 0
        else:
            cx = rcPos.right
            x = rcPos.left

        if rcPos.top == CW_USEDEFAULT:
            cy = 50
            y = 0
        else:
            cy = rcPos.bottom
            y = rcPos.top

        if style & DS_SETFONT:
            if fontSize is None:
                fontSize = self._class_font_size_

            if fontName is None:
                fontName = StringOrOrd(self._class_font_name_)
        else:
            fontSize = None
            fontName = None

        header = DLGTEMPLATE()
        byteCount = sizeof(header)

        byteCount += len(wclass) + len(title) + len(menu)
        if fontName or fontSize:
            byteCount += 2 + len(fontName)

        d, rem = divmod(byteCount, 4)   # align on dword
        byteCount += rem
        itemOffset = byteCount  # remember this for later

        for i in items:
            byteCount += len(i)

        valuetype = c_ubyte * byteCount
        value = valuetype()

        header = DLGTEMPLATE.from_address(addressof(value))
        # header is overlayed on value
        header.exStyle = exStyle
        header.style = style
        header.cDlgItems = len(items)
        header.x = x
        header.y = y
        header.cx = cx
        header.cy = cy

        offset = sizeof(header)

        # now, memcpy over the menu
        memcpy(addressof(value)+offset, addressof(menu.value), len(menu))    # len really returns sizeof menu.value
        offset += len(menu)

        # and the window class
        memcpy(addressof(value)+offset, addressof(wclass.value), len(wclass))    # len really returns sizeof wclass.value
        offset += len(wclass)

        # now copy the title
        memcpy(addressof(value)+offset, addressof(title.value), len(title))
        offset += len(title)

        if fontSize or fontName:
            fsPtr = c_ushort.from_address(addressof(value)+offset)
            fsPtr.value = fontSize
            offset += 2

            # now copy the fontname
            memcpy(addressof(value)+offset, addressof(fontName.value), len(fontName))
            offset += len(fontName)



        # and now the items
        assert offset <= itemOffset, "offset %d beyond items %d" % (offset, itemOffset)
        offset = itemOffset
        for item in items:
            memcpy(addressof(value)+offset, addressof(item.value), len(item))
            offset += len(item)
            assert (offset % 4) == 0, "Offset not dword aligned for item"

        self.m_handle = GlobalAlloc(0, sizeof(value))
        memcpy(self.m_handle, addressof(value), sizeof(value))
        self.value = value

    def __len__(self):
        return sizeof(self.value)


class DialogItemTemplate(object):
    _window_class_ = None
    _window_style_ = WS_CHILD|WS_VISIBLE
    _window_style_ex_ = 0

    def __init__(self,
                 wclass = None,    # the window class
                 id = 0,              # the control id
                 title = "",
                 style = None,
                 exStyle = None,
                 rcPos = RCDEFAULT,
                 orStyle = None,
                 orExStyle = None,
                 nandStyle = None,
                 nandExStyle = None):


        if not self._window_class_ and not wclass:
            raise ValueError("A window class must be specified")

        if wclass is not None:
            wclass = StringOrOrd(wclass)
        else:
            wclass = StringOrOrd(self._window_class_)

        title = StringOrOrd(title)

        if style is None:
            style = self._window_style_

        if exStyle is None:
            exStyle = self._window_style_ex_

        if orStyle:
            style |= orStyle

        if orExStyle:
            exStyle |= orExStyle


        if nandStyle:
            style &= ~nandStyle

        if rcPos.left == CW_USEDEFAULT:
            cx = 50
            x = 0
        else:
            cx = rcPos.right
            x = rcPos.left

        if rcPos.top == CW_USEDEFAULT:
            cy = 50
            y = 0
        else:
            cy = rcPos.bottom
            y = rcPos.top

        header = DLGITEMTEMPLATE()
        byteCount = sizeof(header)
        byteCount += 2  # two bytes for extraCount
        byteCount += len(wclass) + len(title)
        d, rem = divmod(byteCount, 4)
        byteCount += rem            # must be a dword multiple

        valuetype = c_ubyte * byteCount
        value = valuetype()

        header = DLGITEMTEMPLATE.from_address(addressof(value))
        # header is overlayed on value
        header.exStyle = exStyle
        header.style = style
        header.x = x
        header.y = y
        header.cx = cx
        header.cy = cy
        header.id = id

        # now, memcpy over the window class
        offset = sizeof(header)
        memcpy(addressof(value)+offset, addressof(wclass.value), len(wclass))
        # len really returns sizeof wclass.value
        offset += len(wclass)
        # now copy the title
        memcpy(addressof(value)+offset, addressof(title.value), len(title))
        offset += len(title)
        extraCount = c_ushort.from_address(addressof(value)+offset)
        extraCount.value = 0
        self.value = value

    def __len__(self):
        return sizeof(self.value)

PUSHBUTTON = 0x80
EDITTEXT = 0x81
LTEXT = 0x82
LISTBOX  = 0x83
SCROLLBAR = 0x84
COMBOBOX = 0x85

class PushButton(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_TABSTOP

class DefPushButton(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_TABSTOP|BS_DEFPUSHBUTTON

class GroupBox(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|BS_GROUPBOX

class EditText(DialogItemTemplate):
    _window_class_ = EDITTEXT
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_BORDER|WS_TABSTOP

class StaticText(DialogItemTemplate):
    _window_class_ = LTEXT
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_GROUP

class ListBox(DialogItemTemplate):
    _window_class_ = LISTBOX
    _window_style_ = LBS_STANDARD

class ScrollBar(DialogItemTemplate):
    _window_class_ = SCROLLBAR
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_TABSTOP|SBS_VERT|SBS_RIGHTALIGN

class ComboBox(DialogItemTemplate):
	_window_class_ = COMBOBOX
	_window_style_ = WS_VISIBLE|WS_CHILD|WS_OVERLAPPED|WS_VSCROLL|WS_TABSTOP|CBS_DROPDOWNLIST

class RadioButton(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_GROUP|WS_TABSTOP|BS_RADIOBUTTON

class AutoRadioButton(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_GROUP|WS_TABSTOP|BS_AUTORADIOBUTTON

class CheckBox(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_GROUP|WS_TABSTOP|BS_CHECKBOX

class AutoCheckBox(DialogItemTemplate):
    _window_class_ = PUSHBUTTON
    _window_style_ = WS_CHILD|WS_VISIBLE|WS_GROUP|WS_TABSTOP|BS_AUTOCHECKBOX

class Dialog(Window):
    """supports _dialog_id_ and _dialog_module_ class properties or
    use _dialog_template_"""
    _dialog_template_ = None
    _dialog_module_ = None
    _dialog_id_ = None
    
    def __init__(self, template = None, id = None, module = None):
        """module and dlgid can be passed as parameters or be given as class properties"""
        self.module = None
        self.id = None
        self.template = None

        if template or self._dialog_template_:
            self.template = template or self._dialog_template_
        elif module or self._dialog_module_:
            self.module = module or self._dialog_module_
            self.id = id or self._dialog_id_
        
        if self.module and type(self.module) == type(''): #module is given as path name
            self.module = LoadLibrary(self.module)

        self.m_handle = 0 #filled in on init dialog

    def DoModal(self, parent = 0, center = 1):
        self.center = center
        if self.template:
            return DialogBoxIndirectParam(self.module,
                                          self.template.handle,
                                          handle(parent),
                                          DialogProc(self.DlgProc),
                                          0)
        else:
            return DialogBoxParam(self.module, self.id, handle(parent),
                                  DialogProc(self.DlgProc), 0)

    def DlgProc(self, hwnd, uMsg, wParam, lParam):
        handled, result = self._msg_map_.Dispatch(self, hwnd, uMsg, wParam, lParam)
        return result
    
    def GetDlgItem(self, nIDDlgItem, windowClass = None):
        """specify window class to get a 'Venster' wrapped control"""
        hWnd = GetDlgItem(self.handle, nIDDlgItem)
        if hWnd and windowClass:
            return windowClass(hWnd = hWnd)
        else:
            return hWnd            

    def EndDialog(self, exitCode):
        EndDialog(self.handle, exitCode)

    def OnOK(self, event):
        self.EndDialog(IDOK)

    def OnCancel(self, event):
        self.EndDialog(IDCANCEL)

    def OnInitDialog(self, event):
        self.m_handle = event.handle
        if self.center: self.CenterWindow()
        return 0

    _msg_map_ = MSG_MAP([MSG_HANDLER(WM_INITDIALOG, OnInitDialog),
                         CMD_ID_HANDLER(IDOK, OnOK),
                         CMD_ID_HANDLER(IDCANCEL, OnCancel)])

