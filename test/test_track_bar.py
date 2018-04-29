from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form, trackbar

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES | comctl.ICC_STANDARD_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = 'pyWinGUI Track Bar Example'
	CAPTION_FMT = 'Track Bar value: %d'

	class myTrackBar(trackbar.TrackBar):
		def OnScroll(self, event):
			self.parent.caption.SetText(self.parent.CAPTION_FMT % self.GetPos())

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)
		position = 50
		self.caption = comctl.StaticText(self.CAPTION_FMT % position, rcPos = RECT(0, 0, 700, 20), parent = self)
		self.track_bar = self.myTrackBar(rcPos = RECT(0, 20, 700, 50), parent = self)
		self.track_bar.SetRange(0, 100)
		self.track_bar.SetPos(position)

	def OnCreate(self, event):
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form()
	mainForm.ShowWindow()

	application = Application()
	application.Run()
