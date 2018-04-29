from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl

from pywingui.lib import splitter
from pywingui.lib import form

class MyForm(form.Form):
	_window_title_ = "Splitter Window Test"

	def OnCreate(self, event):
		aSplitter = splitter.Splitter(parent = self, splitPos = self.clientRect.width / 2)

		child1 = comctl.StaticText(parent = aSplitter, orExStyle = WS_EX_STATICEDGE)
		child2 = comctl.StaticText(parent = aSplitter, orExStyle = WS_EX_STATICEDGE)
		child1.SetText('StaticText 0')
		child2.SetText('StaticText 1')

		aSplitter.Add(0, child1)
		aSplitter.Add(1, child2)

		self.controls.Add(child1)
		self.controls.Add(child2)

		self.controls.Add(form.CTRL_VIEW, aSplitter)

if __name__ == '__main__':
	mainForm = MyForm()
	mainForm.ShowWindow()

	application = Application()
	application.Run()
