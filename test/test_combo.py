from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, "&File", [(MF_STRING, "&Exit", form.ID_EXIT)])]
	_window_title_ = "Venster Combo Box Example"

	def __init__(self):
		form.Form.__init__(self)      
		self.combo = comctl.ComboBox(parent = self, rcPos = RECT(5, 10, 200, 100))
		for i in range(10):
			print('item index %d' % self.combo.AddString('Item %d' % i))
		self.combo.SetCurrentSelection(5)

	def OnCreate(self, event):
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form()
	mainForm.ShowWindow()

	application = Application()
	application.Run()
