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

from pywingui.windows import *
from pywingui.wtl import *
from pywingui.comctl import *
from pywingui.lib import list
from pywingui.lib import form

#~ from ctypes import *

blinkyIcon = Icon("blinky.ico")

columnDefs = [("blaat", 100), ("col2", 150)]

InitCommonControls(ICC_LISTVIEW_CLASSES)

class MyList(list.List):
	def OnPaint(self, event):
		#print "lpaint", self.handle
		width = self.clientRect.width
		for i in range(len(columnDefs) - 1):
			#self.SetColumnWidth(i, width / len(columnDefs))
			self.SetColumnWidth(i, -2)
		self.SetColumnWidth(len(columnDefs) - 1, -2)

		event.handled = False

	msg_handler(WM_PAINT)(OnPaint)

	def OnWindowPosChanging(self, event):
		event.handled = False

	msg_handler(WM_WINDOWPOSCHANGED)(OnWindowPosChanging)

	def OnSize(self, event):
		#width = self.clientRect.width
		ShowScrollBar(self.handle, SB_HORZ, False)
		self.SetRedraw(0)
		for i in range(len(columnDefs) - 1):
			#self.SetColumnWidth(i, width / len(columnDefs))
			self.SetColumnWidth(i, -2)
		self.SetColumnWidth(len(columnDefs) - 1, -2)
		self.SetRedraw(1)
		event.handled = False

	msg_handler(WM_SIZE)(OnSize)

	def OnColumnClick(self, event):
		nmlv = NMLISTVIEW.from_address(int(event.lParam))
		print "column clicked!", nmlv.iSubItem

	ntf_handler(LVN_COLUMNCLICK)(OnColumnClick)

class MyForm(form.Form):
	_window_icon_ = blinkyIcon
	_window_icon_sm_ = blinkyIcon
	_window_background_ = 0

	_window_title_ = "Test auto column resize (NOT WORKING!)"

	def OnCreate(self, event):
		aList = MyList(parent = self, orExStyle = WS_EX_CLIENTEDGE)
		aList.InsertColumns(columnDefs)
		for i in range(100):
			aList.InsertRow(i, ["blaat %d" % i, "blaat col2 %d" % i])

		self.controls.Add(form.CTRL_VIEW, aList)

	def OnDestroy(self, event):
		application.Quit()
	msg_handler(WM_DESTROY)(OnDestroy)

if __name__ == '__main__':
	mainForm = MyForm()        
	mainForm.ShowWindow()

	application = Application()
	application.Run()
