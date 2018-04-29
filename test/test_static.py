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

from pywingui.lib import form

class Static(Window):
	_window_class_ = 'static'
	_window_style_ = WS_CHILD | WS_VISIBLE

class MyForm(form.Form):
	def __init__(self):
		form.Form.__init__(self, title = "Static windows test (WORKING)")      

		## why can't static be child of other static??
		## why can't ? - YES! YES! can be and must be

		aStatic1 = Static(parent = self)
		aStatic1.SetText('blaat1')

		aStatic2 = Static(parent = self)
		aStatic2.SetText('blaat2')

		aStatic2.MoveWindow(100, 100, 200, 200, 1)

		self.controls.Add(form.CTRL_VIEW, aStatic2)

	def OnSize(self, event):
		form.Form.OnSize(self, event)
		try:
			self.controls[form.CTRL_VIEW].MoveWindow(10,10,100,100,1)
		except:
			print('Error access to non existing child window')
			print(self.controls)

mainForm = MyForm()        
mainForm.ShowWindow()

Run()
