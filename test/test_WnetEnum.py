'Enumerating Network Resources Example'

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form

from pywingui.network.winnetwk import *
from pywingui.network.winnetwk import _WNetEnumResource
from pywingui.windows import GlobalAlloc, GlobalFree

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = __doc__
	item_flags = comctl.LVIF_TEXT|comctl.LVIF_DI_SETITEM
	global_index = 0

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)      
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 200, 'Remote Name')
		self.list_view.InsertColumn(0, lvcolumn)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 200, 'Local Name')
		self.list_view.InsertColumn(1, lvcolumn)
		#=========================================
		# Call the WNetOpenEnum function to begin the enumeration.
		dwResult, hEnum = WNetOpenEnum(RESOURCE_GLOBALNET,# all network resources
								RESOURCETYPE_ANY,# all resources
								0,# enumerate all resources
								None)# NULL first time the function is called
		if dwResult != NO_ERROR:
			print('Call to WNetOpenEnum failed with error: %d' % dwResult)
			print('Error description: "%s"' % FormatError(dwResult))
		else:
			# Call the WNetEnumResource function to continue the enumeration.
			#~ dwResultEnum, cEntries, lpnrLocal, cbBuffer = WNetEnumResource(hEnum)
			cEntries = c_ulong(-1)
			cbBuffer = c_ulong(16384)
			lpnrLocal = cast(GlobalAlloc(0, cbBuffer.value), LPNETRESOURCE)
			WNetEnumResource = _WNetEnumResource
			dwResultEnum = WNetEnumResource(hEnum, byref(cEntries), lpnrLocal, byref(cbBuffer))
			if dwResultEnum == NO_ERROR:
				self.ShowResource(cEntries.value, lpnrLocal)
				while dwResultEnum != ERROR_NO_MORE_ITEMS:
					dwResultEnum = WNetEnumResource(hEnum, byref(cEntries), lpnrLocal, byref(cbBuffer))
					if dwResultEnum == NO_ERROR:
						self.ShowResource(cEntries.value, lpnrLocal)
					elif dwResultEnum != ERROR_NO_MORE_ITEMS:
						print('WNetEnumResource failed with error %d' % dwResultEnum)
						break
			elif dwResultEnum != ERROR_NO_MORE_ITEMS:
				print('WNetEnumResource failed with error %d' % dwResultEnum)
			GlobalFree(pointer(lpnrLocal))
		dwResult = WNetCloseEnum(hEnum)
		if dwResult != NO_ERROR:
			print('Call to WNetCloseEnum failed with error: %d' % dwResult)
			print('Error description: "%s"' % FormatError(dwResult))

	def ShowResource(self, count_entries, lpNetResource):
		for i in range(count_entries):
			item = comctl.LVITEM(self.item_flags)
			item.iItem = self.global_index
			item.pszText = lpNetResource[i].lpRemoteName
			self.list_view.InsertItem(item)
			item.iSubItem = 1
			item.pszText = lpNetResource[i].lpLocalName
			self.list_view.SetItem(item)
			self.global_index += 1

	def OnCreate(self, event):
		self.list_view = comctl.ListView(parent = self, rcPos = RECT(5, 10, 200, 100, orExStyle = WS_EX_CLIENTEDGE))
		self.controls.Add(form.CTRL_VIEW, self.list_view)
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form(rcPos = RECT(0, 0, 550, 350))
	mainForm.ShowWindow()

	application = Application()
	application.Run()
