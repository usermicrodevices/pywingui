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

from pywingui import comctl
from pywingui import gdi

from pywingui.lib import tree
from pywingui.lib import form

from ctypes import *

blinkyIcon = Icon("blinky.ico")

comctl.InitCommonControls(comctl.ICC_TREEVIEW_CLASSES)

def as_pointer(obj):
	"Increment the refcount of obj, and return a pointer to it"
	ptr = pythonapi.Py_BuildValue("O", id(obj))
	assert ptr == id(obj)
	return ptr

def from_pointer(ptr):
	"Convert a pointer to a Python object, and decrement the refcount of the ptr"
	l = [None]
	# PyList_SetItem consumes a refcount of its 3. argument
	pythonDll.PyList_SetItem(id(l), 0, ptr)
	return l[0]

class TestItem:
	def __del__(self):
		#print "del ti"
		pass

class Tree(tree.Tree):
	def __init__(self, *args, **kwargs):
		tree.Tree.__init__(self, *args, **kwargs)

		self.iml = comctl.ImageList(16, 16, ILC_COLOR32 | ILC_MASK, 0, 32)
		self.iml.AddIconsFromModule("shell32.dll", 16, 16, LR_LOADMAP3DCOLORS)
		self.iml.SetBkColor(gdi.CLR_NONE)
		self.SetImageList(self.iml)

		self.SetRedraw(0)
		item = comctl.TVITEMEX()
		item.text = "A root"
		item.image = 17
		item.selectedImage = 17
		item.children = 1        
		self.hRoot = self.InsertItem(comctl.TVI_ROOT, comctl.TVI_ROOT, item)
		for i in range(1):
			item = comctl.TVITEMEX()
			item.text = "A child %d" % i
			item.image = 3
			item.selectedImage = 4
			item.children = 0
			hChild = self.InsertItem(self.hRoot, comctl.TVI_LAST, item)
		self.SetRedraw(1)

	def OnItemExpanding(self, event):
		nmtv = event.structure(comctl.NMTREEVIEW)
		if nmtv.action == comctl.TVE_EXPAND:
			print "Expand"
			for i in range(100):
				ti = TestItem()
				item = comctl.TVITEMEX()
				item.text = "A child %d" % i
				item.image = 3
				item.selectedImage = 4
				item.children = 0
				item.param = as_pointer(ti)
				self.InsertItem(self.hRoot, comctl.TVI_LAST, item)
		elif nmtv.action == comctl.TVE_COLLAPSE:
			print "Collapse"
			self.CollapseAndReset(nmtv.itemNew.hItem)

	def OnSelectionChanged(self, event):
		nmtv = event.structure(comctl.NMTREEVIEW)

	def OnDeleteItem(self, event):
		#print "del item"
		nmtv = event.structure(comctl.NMTREEVIEW)
		i = nmtv.itemOld.lParam
		if i != 0:
			ti = from_pointer(i)
			#print ti

	_msg_map_ = MSG_MAP([NTF_HANDLER(comctl.TVN_ITEMEXPANDING, OnItemExpanding), NTF_HANDLER(comctl.TVN_SELCHANGED, OnSelectionChanged), NTF_HANDLER(comctl.TVN_DELETEITEM, OnDeleteItem)])

class MyForm(form.Form):
	_window_icon_ = blinkyIcon
	_window_icon_sm_ = blinkyIcon
	_window_title_ = "Tree Test (Puts references to Python instances in treenodes)"

	def OnCreate(self, event):
		self.controls.Add(form.CTRL_VIEW, Tree(parent = self, orExStyle = WS_EX_CLIENTEDGE))

	def OnDestroy(self, event):
		application.Quit()
	msg_handler(WM_DESTROY)(OnDestroy)

if __name__ == '__main__':
	mainForm = MyForm()        
	mainForm.ShowWindow()

	application = Application()
	application.Run()
